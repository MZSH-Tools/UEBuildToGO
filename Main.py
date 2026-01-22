# -*- coding: utf-8 -*-
"""
UE Quick Start - 一键编译并启动 Unreal Engine 项目
将此工具放置于 .uproject 同级目录，双击运行即可
"""

import sys
from pathlib import Path

# 获取脚本/exe 所在目录（兼容 PyInstaller 打包）
if getattr(sys, 'frozen', False):
    ScriptDir = Path(sys.executable).parent.resolve()
else:
    ScriptDir = Path(__file__).parent.resolve()
sys.path.insert(0, str(ScriptDir))

from Source.UI.MainWindow import MainWindow


def Main():
    App = MainWindow(ScriptDir)
    App.Run()


if __name__ == "__main__":
    Main()
