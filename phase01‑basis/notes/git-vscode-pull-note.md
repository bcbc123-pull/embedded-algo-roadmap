# Git 从保存更改到完成推送完整操作笔记

## 1. 三个关键概念

| 概念 | 含义 | 存储位置 |
| ---- | ---- | ---- |
| **暂存 (stage)** | 挑选要提交的文件 | `.git/index`，关 VSCode 不丢失 |
| **commit (本地提交)** | 把暂存文件生成一个版本记录 | 只在本机，网页仓库看不到 |
| **push (推送)** | 把本地 commit 上传到远程仓库 | GitHub/Gitee 云端 |

> 流程：**本地文件修改 → 文件+暂存 → 生成本地 commit → push 推送远程。**

## 2. 现象：空消息点提交，弹出 COMMIT_EDITMSG

**触发条件**：VSCode 源代码管理顶部输入框为空，直接点【提交】按钮。
Git 会打开内部临时文件 `.git/COMMIT_EDITMSG` 要求填写提交信息，同时顶部输入框被锁为只读。

> ⚠️ `.git/COMMIT_EDITMSG` 属于 Git 内部临时文件，**禁止提交到仓库**。

### 方法一：编辑 COMMIT_EDITMSG 完成本地 commit

1. 打开 `.git/COMMIT_EDITMSG` 文件。
2. **第一行写入提交信息**；`#` 开头的注释行保留即可，Git 会自动忽略。
   示例：`docs (phase01): 新增 git 全套操作学习笔记`
3. `Ctrl+S` 保存。
4. 关闭标签页，Git 读取文件自动执行本地 commit。
   **成功判断**：更改列表文件全部消失，Git 历史面板出现本次提交记录。

> ⚠️ Windows 下 `.git` 目录文件可能只读无法保存，则改用方法二。

### 方法二：终端命令完成 commit（推荐，规避只读弹窗）

文件已提前暂存，无需重新暂存。打开 VSCode 内置终端，在仓库根目录执行：

```bash
git commit -m "docs(phase01): 新增git全套操作学习笔记"
```

执行成功即完成本地 commit。

## 3. 本地 commit 之后：推送 Push

| 方式 | 操作 |
| ---- | ---- |
| 图形界面 | 源代码管理面板右上角 `...` → `Push` |
| 终端 | `git push` |

### 推送弹出 GitHub Sign in 登录弹窗

1. 选择 `Browser/Device` 标签，点 `Sign in with your browser`。
2. 浏览器登录 GitHub 并授权 VSCode。
3. 返回 VSCode，弹窗自动关闭，推送继续。

> 授权成功后 VSCode 会缓存凭据，后续推送不再弹窗；Token 选项为高级手动模式，新手忽略。

## 4. 如何判断执行结果

- **本地 commit 成功**：Git 历史图表出现提交记录，更改列表文件消失。
  > ⚠️ **出现提交记录 ≠ 推送成功**，断网也能生成本地 commit。
- **推送真正成功**：网页仓库刷新后能看到新增文件；VSCode 底部状态栏分支显示 `0↑ 0↓`。

## 5. 根治配置：彻底禁用 COMMIT_EDITMSG 弹窗

`Ctrl+Shift+P` →「首选项：打开设置 (JSON)」，添加：

```json
"git.useEditorAsCommitInput": false
```

保存并重载 VSCode 窗口。

> 作用：不再唤起 COMMIT_EDITMSG 编辑模式，强制使用顶部输入框填写提交消息；空消息点提交直接报错，不会锁输入框。

## 6. 踩坑记录

1. **COMMIT_EDITMSG 空白直接关标签页**：本次提交作废，临时文件销毁，不生成 commit，文件回到暂存前状态（标签消失 ≠ 提交成功）。
2. **`.git` 文件夹是 Git 内部数据库**，绝对不要修改、提交其中任何文件。
3. **提交 ≠ 推送**：提交保存在本机，推送才同步云端。
