# -*- coding: utf-8 -*-
"""编译管理器 - 业务逻辑层"""

import subprocess
import threading
from pathlib import Path
from typing import Callable, Optional


class BuildMgr:
    """编译管理器"""

    def __init__(self):
        self.IsBuilding: bool = False
        self.BuildSuccess: bool = False
        self.Process: Optional[subprocess.Popen] = None

    def StartBuild(
        self,
        ProjectName: str,
        ProjectPath: Path,
        EnginePath: str,
        OnLog: Callable[[str], None],
        OnSuccess: Callable[[], None],
        OnError: Callable[[str], None]
    ):
        """开始编译（异步）"""
        if self.IsBuilding:
            return

        self.IsBuilding = True
        self.BuildSuccess = False

        Thread = threading.Thread(
            target=self._RunBuild,
            args=(ProjectName, ProjectPath, EnginePath, OnLog, OnSuccess, OnError),
            daemon=True
        )
        Thread.start()

    def _RunBuild(
        self,
        ProjectName: str,
        ProjectPath: Path,
        EnginePath: str,
        OnLog: Callable[[str], None],
        OnSuccess: Callable[[], None],
        OnError: Callable[[str], None]
    ):
        """执行编译（后台线程）"""
        BuildBat = Path(EnginePath) / "Engine/Build/BatchFiles/Build.bat"

        if not BuildBat.exists():
            self.IsBuilding = False
            OnError(f"找不到 Build.bat: {BuildBat}")
            return

        # 构建编译命令
        Cmd = [
            str(BuildBat),
            f"{ProjectName}Editor",
            "Win64",
            "Development",
            f"-Project={ProjectPath}",
            "-WaitMutex",
            "-FromMsBuild"
        ]

        OnLog(f"执行命令: {' '.join(Cmd)}")

        try:
            self.Process = subprocess.Popen(
                Cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding='utf-8',
                errors='replace',
                cwd=str(ProjectPath.parent),
                shell=True
            )

            # 实时读取输出
            for Line in self.Process.stdout:
                Line = Line.strip()
                if Line:
                    OnLog(Line)

            self.Process.wait()

            self.IsBuilding = False
            if self.Process.returncode == 0:
                self.BuildSuccess = True
                OnSuccess()
            else:
                OnError(f"编译失败，返回码: {self.Process.returncode}")

        except Exception as E:
            self.IsBuilding = False
            OnError(f"编译异常: {E}")

    def OpenProject(self, ProjectPath: Path, EnginePath: str) -> tuple[bool, str]:
        """打开项目，返回 (成功, 错误信息)"""
        EditorExe = Path(EnginePath) / "Engine/Binaries/Win64/UnrealEditor.exe"

        # 兼容 UE4
        if not EditorExe.exists():
            EditorExe = Path(EnginePath) / "Engine/Binaries/Win64/UE4Editor.exe"

        if not EditorExe.exists():
            return False, f"找不到编辑器: {EditorExe}"

        try:
            subprocess.Popen([str(EditorExe), str(ProjectPath)], shell=True)
            return True, ""
        except Exception as E:
            return False, f"无法启动编辑器: {E}"
