# 如何配置miniconda

## 1.下载miniconda

先到清华源下载miniconda，安装，勾选安装界面前三个选项

安装好后打开anaconda prompt，输入conda检查是否安装成功

## 2.更改pip和conda下载源

更改pip和conda下载源为清华源，在清华源网站有详细教程

## 3.配置conda虚拟环境

先安装一个虚拟环境版本的python，打开anaconda prompt

输入代码：conda create -n “虚拟环境名字” python=3.11		//下载3.11版本python

确定安装：y

查看conda虚拟环境		代码：conda env list

切换到新的虚拟环境		代码：conda activate “虚拟环境名字”

退出虚拟环境				代码：exit

删除虚拟环境				代码：conda env remove -n “虚拟环境名字”

pip下载jieba				代码：pip install jieba

下载python库				代码：pip install "库名称“
