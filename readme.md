# パブリックコメントをslackに投稿させるためのプログラム
#動作環境
Mac
python3.7

## 導入方法
１. まずはじめにrequeirement.txtに入っているパッケージをインストールする。  
1. slack apiのアクセストークンを取得（すでにセットしてあります）。取得したトークンを"slackbot_settings.py"の”API_TOKEN”にセットする。

”python main.py”で起動。

## 使い方
1. 　アプリ"public commentとDMをすることで動作します。　
2.  DMで"list"と打つとパブリックコメントを取得し、1件ずつ返す。
3. "list 3"などのようにlistの後に数字を入れると入れた数字の分だけの日数のパブリックコメントを返します。（最大１週間ほど）
