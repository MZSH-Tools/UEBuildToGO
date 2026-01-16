# UEBuildToGO - 开发文档

## 项目大纲

一键编译并打开 UE 项目的 GUI 工具，替代 IDE 编译流程。

### 架构

```
Main.py (入口)
    ↓
Source/UI/MainWindow.py (界面层)
    ↓
Source/Logic/BuildMgr.py (业务逻辑层)
    ↓
Source/Data/ProjectInfo.py (数据访问层)
```

### 核心流程

1. 检测 `.uproject` 文件 → 获取项目名、引擎版本
2. 从注册表/Launcher 配置获取引擎路径
3. 调用 `Engine/Build/BatchFiles/Build.bat` 编译
4. 编译成功后启动 `UnrealEditor.exe` 打开项目

## 功能进度

| 功能 | 状态 | 说明 |
|------|------|------|
| 项目检测 | ✅ 完成 | [链接](编译功能/) |
| 引擎路径获取 | ✅ 完成 | [链接](编译功能/) |
| 编译执行 | ✅ 完成 | [链接](编译功能/) |
| 打开项目 | ✅ 完成 | [链接](编译功能/) |
| 跨平台支持 | ⏳ 待开始 | macOS/Linux |

## 当前任务

- [x] Windows 版本基础功能
- [ ] 实际项目测试验证
- [ ] 打包成 EXE 发布

## 阻塞与待讨论

| 事项 | 类型 | 说明 |
|------|------|------|
| 暂无 | - | - |
