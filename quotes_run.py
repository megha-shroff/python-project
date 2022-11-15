import requests
from bs4 import BeautifulSoup
from lxml import etree
import re
from plyer import notification  
import time
import schedule
import random

notification_title = 'You\'re bored right ? Have a read here ! ' 
done_icon = "D:/Google search/army.ico"
  
def notification_fun(msg):

    notification.notify(
        title = notification_title,  
        message = msg,  
        app_icon = done_icon,  
        timeout = 10,
        toast=True
    )  

url = "https://everydaypower.com/short-inspirational-quotes/"
data = requests.get(url)

html = BeautifulSoup(data.text, 'html.parser')

print(html)

documentObjectModel = etree.HTML(str(html))
quotes = documentObjectModel.xpath('//*[@id="h-short-inspirational-quotes-about-happiness"]/following-sibling::p')

# while True:
#     for q in quotes:
#         text = q.text
#         try :
#             quote = re.findall("\“(.*?)\”", text)
#             ran_num = random.randint(0, len(quotes)-1)
#             # print(ran_num)
#             notification_fun(quote[ran_num])
#             for i in range(3600):
#                 time.sleep(1)

#         except Exception as e :
#             # print(e)
#             pass
#         # print(quote[0])
    
