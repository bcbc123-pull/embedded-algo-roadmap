# 如何配置 Miniconda

## 1. 下载安装

- 从**清华源**下载 Miniconda 安装包，安装时勾选**界面提示的前三个选项**。
- 安装后打开 **Anaconda Prompt**，输入 `conda` 回车，能输出帮助信息即安装成功。

## 2. 更换 pip / conda 下载源

将 pip 与 conda 的下载源改为**清华源**（清华源官网有详细教程），加速下载。

## 3. 虚拟环境常用命令

> 先打开 **Anaconda Prompt** 再执行以下命令。

| 操作 | 命令 |
| ---- | ---- |
| **创建环境**（指定 Python 版本） | `conda create -n "环境名" python=3.11` |
| **查看所有环境** | `conda env list` |
| **进入环境** | `conda activate "环境名"` |
| **退出环境** | `exit` |
| **删除环境** | `conda env remove -n "环境名"` |
| **安装库**（以 jieba 为例） | `pip install jieba` |
