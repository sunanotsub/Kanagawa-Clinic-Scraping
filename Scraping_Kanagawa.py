import csv
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

# WebサイトのURLを指定
url = 'http://www.iryo-kensaku.jp/kanagawa/kensaku/IryoSisetsuInfo.aspx?sy=m&cm=k&di=n&id=14058251&ir=02'

# Requestsを利用してWebページを取得する
r = requests.get(url)

# BeautifulSoupを利用してWebページを解析する
soup = BeautifulSoup(r.content, 'html.parser')

# クリニックの名前
elem1 = soup.findAll(id="ctl00_ContentPlaceHolderContents_ctl58_lblShisetsuName")

i = 0
for e1 in elem1:
    if i == 2:
        print(e1.text)
    i = i+1

# クリニックの名前(英語)
elem2 = soup.findAll(id="ctl00_ContentPlaceHolderContents_ctl58_lblShisetsuNameEng")

for e2 in elem2:
    print(e2.text)

# 院長氏名
elem3 = soup.findAll(id="ctl00_ContentPlaceHolderContents_lblKanName")

for e3 in elem3:
    print(e3.text)

# 都道府県,市区町村
elem4 = soup.findAll(id="ctl00_ContentPlaceHolderContents_ctl58_lblAddress")

for e4 in elem4:
    print(e4.text)

# 電話番号
elem5 = soup.findAll(id="ctl00_ContentPlaceHolderContents_ctl58_lblAnnaiTelephoneNo0")

for e5 in elem5:
    print(e5.text)

# 予約方法：電話、ネット、完全予約制か
elem6 = soup.findAll(id="ctl00_ContentPlaceHolderContents_lblYoyaku")

for e6 in elem6:
    print(e6.text)

# 予約手段
elem7 = soup.findAll(id="ctl00_ContentPlaceHolderContents_lblYoyakuShudan")

for e7 in elem7:
    print(e7.text)

# 予約を実施している診療科目
elem8 = soup.findAll(id="ctl00_ContentPlaceHolderContents_lblYoyakuKamoku")

for e8 in elem8:
    print(e8.text)

# 診療曜日, 遅くまで診療可能（19:00~）9

# 診療時間 10

# 日曜または休日/祝日診察可能 11

# 近隣駐車場の有無 12

# 駐車場の台数
elem13 = soup.findAll(id="ctl00_ContentPlaceHolderContents_lblParking")

for e13 in elem13:
    print(e13.text)

# クリニックURL
elem14 = soup.findAll(id="ctl00_ContentPlaceHolderContents_hlHomePageAddress")

for e14 in elem14:
    print(e14.text)

# クリニックの英語以外の外国語対応 # バリアフリー
elem15 = soup.findAll(id="ctl00_ContentPlaceHolderContents_tblData3")

for e15 in elem15:
    print(e15.text)

# 自由診療等の料金 16

# クレジットカード対応可かどうか
elem17 = soup.findAll(id="ctl00_ContentPlaceHolderContents_tblData4")

for e17 in elem17:
    print(e17.text)

# 医師の資格 18

# 可能な治療・特色・専門（漢方処方） 19

# 診察可能な難病 20

# 自由診療・人間ドック・健康診断 予防接種 オンライン診療の有無
elem21 = soup.findAll(id="ctl00_ContentPlaceHolderContents_tblData7")

for e21 in elem21:
    print(e21.text)

# 往診・在宅 22
elem22 = soup.findAll(id="ctl00_ContentPlaceHolderContents_tblData8")

for e22 in elem22:
    print(e22.text)

# 診療科目
elem23 = soup.findAll(id="ctl00_ContentPlaceHolderContents_lblShinryoKamoku")

for e23 in elem23:
    print(e23.text)

# 女医の有無 24

# 配列の作成。
csvlist = [elem23]

# CSVファイルを開く。ファイルがなければ新規作成する。
f = open("output.csv", "w")
writecsv = csv.writer(f, lineterminator='\n')

# 出力
writecsv.writerow(csvlist)

# CSVファイルを閉じる。
f.close()