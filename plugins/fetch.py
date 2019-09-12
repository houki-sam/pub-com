import os
import re

from datetime import datetime as dt
from bs4 import BeautifulSoup as bs
import requests

#検索文字の正規表現
pattern = "Public\?CLASSNAME=PCMMSTDETAIL&id=[0-9]+&Mode="

def within_day_judge(page_item):
    #文字列の取得
    
    date = page_item.tr.td.contents[0].strip("\t")
    #datetimeに変換
    tstr = dt.strptime(date,'%Y年%m月%d日')
    #今日の日付
    tdatetime = dt.now()
    return date,(tdatetime-tstr).days
    


#page_id :  0->意見募集中, 2->結果公示案件
#within_day : 何日ぶんの最新データを取り出すかを決める
def scraling_main_page(page_id,within_day):
    #ベースとなるURL
    base_url = "https://search.e-gov.go.jp/servlet"
    #一覧のページ
    list_url = os.path.join(base_url,"Public?CLASSNAME=PCMMSTLIST&Mode={}".format(page_id))

    #get処理
    html = requests.get(list_url).text
    
    
    #bs4による処理
    soup = bs(html, features="html.parser")
    page_list = soup.find_all("table",class_="publicTbl")
    public_list = soup.find_all("h2",class_ = "public")

    
    
    
    ireko = []

    #該当URLの取り出し
    for page in page_list:
        #日時

        date, days = within_day_judge(page) 
        if days < within_day:
            #url
            para_url = re.findall(pattern,page.a.get("onclick"))
            url = os.path.join(base_url,para_url[0])+str(page_id)
            title = ''.join(page.a.contents[0].split())
            

            dic ={
                "title" : title,
                "date" : date,
                "url" : url,
                   
            }
            ireko.append(dic)
         
    return ireko
if __name__ == "__main__":
    scraling_main_page(0,1)
            



    
