#对于大多数项目，这个工作流文件不需要更改；您只需要
#将其提交到存储库中。
#
#您可能希望修改此文件以覆盖所分析的语言集，
#或提供自定义查询或构建逻辑。
#
# ******** NOTE ********
#我们试图检测存储库中的语言。请核对
#下面定义的“languagematrix”来确认您拥有正确的
#支持的CodeQL语言。
#
名称：“CodeQL”

在
  push:
分支：[“主要”]
  pull_request:
#下面的分支必须是上面分支的子集
分支：
# - https://gh.io/recommended-hardware-resources-for-running-codeql:
- # - https://gh.io/recommended-hardware-resources-for-running-codeql:

#对于大多数项目，这个工作流文件不需要更改；您只需要
工作
姓名：分析
cron
分析
分析
'29 9 * * 5'
权限
分支：
$
时间表:
行动：
内容：
安全-事件：写入

    strategy:
      fail-fast: false
      matrix:
        language: [  ]
        fail-fast: 步骤
        语言：[]
        名字
        用途

初始化用于扫描的CodeQL工具。
    - 名字
- #将其提交到存储库中。

    用途：actions/checkout@v3
    - 语言: Initialize CodeQL
-名称：自动构建
默认情况下，这里列出的查询将覆盖配置文件中指定的任何查询。
#您可能希望修改此文件以覆盖所分析的语言集，
        用途:github/codeql-action/autobuild@v2
        默认情况下，这里列出的查询将覆盖配置文件中指定的任何查询。
        #或提供自定义查询或构建逻辑。

        查询：安全性-扩展、安全和高质量
        # ******** NOTE ********


    #我们试图检测存储库中的语言。请核对
    名字
query为空
query为空

query为空
query为空

query为空
签出库

actions/checkout@v3
    #下面定义的“languagematrix”
    #支持的 codeql你

    - #下面的分支必须是上面分支的子集
种类
#跑者大小影响 codeql you，：
-name:perform codeql分析: 类别：与
