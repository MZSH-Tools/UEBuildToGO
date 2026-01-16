# UEBuildToGO

一键编译并打开 Unreal Engine 项目的 GUI 工具，无需启动 IDE。

## 功能

- 自动检测当前目录的 `.uproject` 文件
- 从 Windows 注册表 / Epic Games Launcher 自动获取引擎路径
- 实时显示编译日志
- 编译成功后一键打开项目

## 界面预览

```
┌─────────────────────────────────────┐
│  项目: MyGame                        │
│  引擎: Unreal Engine 5.3             │
│  状态: ● 编译中...                   │
├─────────────────────────────────────┤
│  [编译日志滚动显示]                  │
├─────────────────────────────────────┤
│  [开始编译]  [打开项目]      [关闭]  │
└─────────────────────────────────────┘
```

## 使用方法

### 方式一：直接运行（需要 Python 环境）

1. 将 `Main.py` 和 `Source/` 目录复制到 UE 项目根目录（与 `.uproject` 同级）
2. 运行：
   ```bash
   python Main.py
   ```

### 方式二：打包成 EXE

1. 安装依赖：
   ```bash
   pip install pyinstaller
   ```

2. 打包：
   ```bash
   pyinstaller --onefile --windowed --name "UEBuildTool" Main.py
   ```

3. 将 `dist/UEBuildTool.exe` 复制到 UE 项目根目录，双击运行

## 项目结构

```
UEBuildToGO/
├── Main.py              # 启动文件
├── Source/
│   ├── UI/              # 界面层
│   │   └── MainWindow.py
│   ├── Logic/           # 业务逻辑层
│   │   └── BuildMgr.py
│   └── Data/            # 数据访问层
│       └── ProjectInfo.py
├── requirements.txt     # pip 依赖
└── environment.yml      # conda 环境
```

## 环境要求

- Python 3.10+
- Windows（macOS/Linux 暂不支持）
- Unreal Engine 通过 Epic Games Launcher 安装

## 许可证

MIT
