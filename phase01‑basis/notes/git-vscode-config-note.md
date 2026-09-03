# Git + VSCode 环境配置笔记

## 1. .gitignore 的作用

告诉 Git 哪些文件**不要提交到远程仓库**。

### 语法

- `文件夹名/`：忽略整个文件夹
- `**`：文件夹下所有内容
- `!`：取反，例外，需要纳入版本管理

### 配置说明

```gitignore
# VSCode
.vscode/**  //VSCode 会在.vscode生成一堆本地机器专属文件，不能上传仓库
!.vscode/tasks.json			//不忽略编译任务配置
!.vscode/launch.json		//不忽略F5调试设置
!.vscode/c_cpp_properties.json  //不忽略C/C++ 头文件、智能提示配置
 	Q:为什么要提交这三个进仓库？ A:这三份是项目工程配置

# C编译产物

//编译输出文件夹
build/
Debug/
Release/

*.o 		//中间目标文件夹
*.exe		//Windows可执行程序

//单片机固件
*.elf  
*.hex
*.bin

# Python miniconda
//Python 运行自动生成的字节码缓存文件，运行代码自动产生，不需要保存
__pycache__/
*.pyc

venv/ 		//如果用 python venv 创建的虚拟环境文件夹
.env
*.env 		//存放密钥、密码的环境变量文件，禁止上传仓库，防止泄露

# 系统垃圾
Thumbs.db 	//Windows 缩略图缓存文件
```



## 2. VSCode、MinGW、Miniconda 各自职责

1. VSCode：编辑器操作台，写代码、调试界面、Git 操作，**不自带 C 编译器、不自带 Python 解释器**
2. MinGW‑w64 (gcc/g++)：负责编译、运行 C 语言 PC 程序
3. Miniconda：管理 Python 解释器、虚拟环境、算法库；VSCode 只是调用 conda 里面的 python.exe

## 3. 仓库提交原则

✅需要提交：源码 `.c` `.py`、笔记 `.md`、工程配置 json
❌不要提交：编译产物、运行缓存、本机 IDE 个人设置、二进制固件、虚拟环境本体

## 4. 踩坑记录
