import requests
import time
from bs4 import BeautifulSoup
from Stocklist import print_watchList, fill_stocklist_auto, auto_stocklist, auto_pricer
from Stock_class import STOCK
from Config_Functions import create_order, sell_order
from Trader_Func import Trader


url = 'https://www.google.com/search?q=autolus+stock&rlz=1C1CHBF_enUS863US863&oq=autolus+stock&aqs=chrome.0.69i59j46j0l3j69i60l3.6551j0j4&sourceid=chrome&ie=UTF-8'
headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

#currentPrice = soup.find(jsname = 'vWLAgc').get_text()
#print(currentPrice)

class totals():
    def __init__(self, tP, cS):
        self.tP = tP
        self.cS = cS
    tP = 0.0
    cS = 0.0



        

def autoTrade(stock):
    
    if current_time != "09:00:00":

        #fill_stocklist_auto()

        firstTime = True

        index = 0
        num = 1
        amount = 20

        while(current_time != "16:00:00"):
            #print_watchList()

            if num == 0:#Bing
                Trader(stock, firstTime, num, amount)

                num = 1

            elif num == 1:#Yahoo
                Trader(stock, firstTime, num, amount)

                num = 2

            elif num == 2:#Yahoo Finacne
                Trader(stock, firstTime, num, amount)

                num = 1
            
            elif num == 3:#Finviz
                Trader(stock, firstTime, num, amount)

                num = 0

            elif num == 4:#Google
                Trader(stock, firstTime, num, amount)

                num = 1


            
            if index == 0:
                index = 1
                firstTime = False

            #print("TP :: $" + str(round(totals.tP, 2)) + " :: ", end = '')
            #print("TS :: $" + str(round(totals.cS, 2)) + "\n")

            time.sleep(5)



fill_stocklist_auto()

response = input("1 for auto and 2 for manual :: ")

if response == "1":
    txxt = open("C:/VS/TEST/Tester.txt", "r")

    s_tx = int(txxt.read())

    #autoTrade(auto_stocklist[s_tx])
elif response == "2":
    s_tx = input("Enter a stock :: ")

    #autoTrade(auto_stocklist[s_tx])