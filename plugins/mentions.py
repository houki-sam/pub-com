from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
from .fetch import scraling_main_page as smp

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない
@respond_to('メンション')
def mention_func(message):
    message.reply('こんにちは') # メンション

@respond_to(r'list')
def listen_func(message):
    number = 1 #デフォルト値
    text = message.body['text'].split()
    
    if len(text)>1:
        number = int(text[1])
    result = smp(0,number) 
    for x in result:
        text ="``` 公示日：{}\n 題名：{}\n url：{}```".format(x["date"],x["title"],x["url"])
        message.send(text)

@respond_to(r'help')
def ping_func(message):
    message.reply('list:一覧を表示します。\npllit:過去の結果の一覧を表示します。')
