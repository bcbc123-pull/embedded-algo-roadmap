# Git + VSCode 环境配置笔记

## 1. .gitignore 的作用

告诉 Git 哪些文件**不要提交到远程仓库**。

### 语法规则

| 写法 | 含义 |
| ---- | ---- |
| `文件夹名/` | 忽略整个文件夹 |
| `**` | 文件夹下所有内容 |
| `!` | 取反（例外），重新纳入版本管理 |

### 配置示例

```gitignore
# VSCode 本地机器专属文件，不上传仓库
.vscode/**
# 但以下三份工程配置要提交进仓库
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/c_cpp_properties.json

# C 编译产物
build/
Debug/
Release/
*.o
*.exe
*.elf
*.hex
*.bin

# Python 运行缓存
__pycache__/
*.pyc
venv/

# 密钥、密码等环境变量文件，禁止上传，防止泄露
.env
*.env

# 系统垃圾
Thumbs.db
```

> **为什么三个 `.vscode` json 要提交？** 它们是工程配置：tasks=编译任务、launch=F5 调试、c_cpp_properties=C/C++ 头文件与智能提示。属于项目配置而非个人设置。

## 2. VSCode、MinGW、Miniconda 各自职责

| 工具 | 职责 |
| ---- | ---- |
| **VSCode** | 编辑器操作台：写代码、调试、Git 操作；**不自带 C 编译器，也不自带 Python 解释器** |
| **MinGW-w64 (gcc/g++)** | 负责编译、运行 C 语言 PC 程序 |
| **Miniconda** | 管理 Python 解释器、虚拟环境、算法库；VSCode 只负责调用 conda 里的 `python.exe` |

## 3. 仓库提交原则

- ✅ **需要提交**：源码 `.c` `.py`、笔记 `.md`、工程配置 json
- ❌ **不要提交**：编译产物、运行缓存、本机 IDE 个人设置、二进制固件、虚拟环境本体
