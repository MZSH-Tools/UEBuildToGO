# UEBuildToGO 使用教程

## 快速开始

### 准备工作

1. 确保 Unreal Engine 通过 **Epic Games Launcher** 安装
2. 确保已安装 Python 3.10+（打包后无需）

### 使用步骤

1. 将工具放置到 UE 项目根目录（与 `.uproject` 同级）
2. 双击运行 `UEBuildTool.exe`（或 `python Main.py`）
3. 点击「开始编译」
4. 等待编译完成，点击「打开项目」

## 配置说明

本工具无需配置，自动检测：

| 项目 | 来源 |
|------|------|
| 项目名称 | `.uproject` 文件名 |
| 引擎版本 | `.uproject` 中的 `EngineAssociation` |
| 引擎路径 | Windows 注册表 / Epic Games Launcher 配置 |

## 打包成 EXE

```bash
# 安装打包工具
pip install pyinstaller

# 打包
pyinstaller --onefile --windowed --name "UEBuildTool" Main.py

# 输出位置
dist/UEBuildTool.exe
```

## 常见问题

### Q: 提示"未找到 .uproject 文件"

**原因**：工具没有放在 UE 项目根目录

**解决**：将 `UEBuildTool.exe` 或 `Main.py` + `Source/` 复制到 `.uproject` 文件所在目录

---

### Q: 提示"无法找到引擎安装路径"

**原因**：引擎不是通过 Epic Games Launcher 安装，或注册表信息丢失

**解决**：
1. 确认引擎是通过 Launcher 安装
2. 尝试在 Launcher 中验证引擎文件
3. 重新安装引擎

---

### Q: 编译失败

**原因**：代码错误或环境问题

**解决**：
1. 查看日志窗口中的具体错误信息
2. 在 IDE 中打开项目查看详细错误
3. 确认 Visual Studio 已正确安装（UE 编译依赖）

---

### Q: 支持 UE4 吗？

**支持**。工具会自动检测编辑器：
- UE5: `UnrealEditor.exe`
- UE4: `UE4Editor.exe`

---

### Q: 支持 macOS / Linux 吗？

**暂不支持**。当前仅支持 Windows，跨平台功能待开发。
