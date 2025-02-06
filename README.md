# Pylitsearch
 系統的文献調査の支援ツールです．AIを使ったアブストラクトスクリーニングまで行うことができます．個人的な意見ですがフルテキストレビューは自分でやるほうがいいと思うのでそれ以降の支援機能は作成していません．

# Description

系統的文献調査を支援するパッケージです．ブラウザベースのアプリケーションとして動作します．主な機能としては以下です．

- 検索クエリと検索式を定義できる
- inclusion条件とexclusion条件を定義できる
- 検索式をもとにGoogle Scholarから論文を検索
- 検索した論文の総数を表示
- 論文はデータベースに保存
- inclusion条件とexclusion条件からAIでアブストラクトスクリーニング
- スクリーニング後の総数を表示

ユーザはスクリーニング後の論文のフルテキストレビューから始めることができます（ここはツールで簡略化してはいけないと思いました）．

# Commit Message Guidelines

| **Type**     | **Description**                                                                 |
|--------------|---------------------------------------------------------------------------------|
| feat         | A new feature                                                                   |
| fix          | A bug fix                                                                       |
| docs         | Documentation only changes                                                      |
| style        | Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc) |
| refactor     | A code change that neither fixes a bug nor adds a feature                       |
| perf         | A code change that improves performance                                         |
| test         | Adding missing or correcting existing tests                                     |
| chore        | Changes to the build process or auxiliary tools and libraries such as documentation generation |


# Installation

プロジェクトルートで以下を実行

```shell
pip install .
```

# Usage

コマンドプロンプトで以下を実行

```shell
pylitsearch
```
