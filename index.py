# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import smtplib
import time
def send_mail(content):
    sent_from = "hungthunghiem1@gmail.com"
    sent_to = ['sf.zing.vn@gmail.com']
    sent_subject = "Có đơn hàng rẻ"
    sent_body = content
    email_text = """\
From: %s
To: %s
Subject: %s

    %s
    """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login("hungthunghiem1@gmail.com", "jltkcxmfcfwwbjyu")
        email_text = email_text.encode('utf-8')
        server.sendmail(sent_from, sent_to, email_text)
        server.close()
    except Exception as exception:
        print("Error: %s!\n\n" % exception)
chrome_options = Options()
chrome_options.headless=True
chrome_options.add_argument("log-level=3")
driver = webdriver.Chrome(options=chrome_options)
listItem = []
listItem.append({"link":"https://shopee.vn/Ph%E1%BA%A7n-m%E1%BB%81m-Microsoft-365-Family-12-th%C3%A1ng-D%C3%A0nh-cho-6-ng%C6%B0%E1%BB%9Di-5-thi%E1%BA%BFt-b%E1%BB%8B-ng%C6%B0%E1%BB%9Di-Tr%E1%BB%8Dn-b%E1%BB%99-%E1%BB%A9ng-d%E1%BB%A5ng-Office-1TB-OneDrive-i.286157142.5444276298?position=0","XPATH":'#main > div > div._193wCc > div.page-product.page-product--mall > div.container > div.product-briefing.flex.card.zINA0e > div.flex.flex-auto._3-GQHh > div > div:nth-child(3) > div > div > div > div > div.flex.items-center > div.Ybrg9j',"type":1})
listItem.append({"link":"https://tiki.vn/phan-mem-microsoft-365-family-english-apac-em-subscr-1yr-medialess-p6-6gq-01144-hang-chinh-hang-p53056161.html?spid=53056293","XPATH":'#__next > div:nth-child(1) > main > div:nth-child(3) > div > div.indexstyle__ProductContent-sc-qd1z2k-2.hnvYGq > div.body > div > div.left > div.price-and-icon > div.style__StyledProductPrice-sc-15mbtqi-0.hlBZfh > div > div.product-price__current-price',"type":2})
listItem.append({"link":"https://www.lazada.vn/products/phan-mem-microsoft-365-family-12-thang-danh-cho-6-nguoi-5-thiet-binguoi-tron-bo-ung-dung-office-1tb-luu-tru-onedrive-i985996017-s3129618664.html?spm=a2o4n.searchlist.list.1.5e6c6d50rtkAYo&search=1","XPATH":'#module_product_price_1 > div > div > span',"type":2})
while True:
    for x in listItem:
        try:
            driver.get(x["link"])
            elem = driver.find_element_by_css_selector(x["XPATH"])
            if(x["type"] == 1):
                result = elem.text[1:]
                result= result.replace(".","")
                result = int(result)
            else:
                result = elem.text[:-2]
                result= result.replace(".","")
                result = int(result)
            if result < 1250000:
                content = "Có key office 365 family rẻ hơn tại:" + x["link"]
                send_mail(content)
        except:
            pass
    time.sleep(3600)

driver.quit()