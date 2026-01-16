# -*- coding: utf-8 -*-
"""
UE Build Tool - 一键编译并打开 Unreal Engine 项目
将此工具放置于 .uproject 同级目录，双击运行即可
"""

import sys
from pathlib import Path

# 添加项目根目录到路径
ScriptDir = Path(__file__).parent.resolve()
sys.path.insert(0, str(ScriptDir))

from Source.UI.MainWindow import MainWindow


def Main():
    App = MainWindow(ScriptDir)
    App.Run()


if __name__ == "__main__":
    Main()
