import requests
import time
from bs4 import BeautifulSoup
from Stocklist import print_watchList, fill_stocklist_auto, auto_stocklist, auto_pricer
from Stock_class import STOCK
from Config_Functions import create_order, sell_order


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


def price(firstTime):
    currentPrice = soup.find(jsname = 'vWLAgc').get_text()
    print(currentPrice)

    if firstTime == True:
        basePrice = currentPrice
        firstTime = False

    else:
        firstTime = False
        newPrice = currentPrice

        if newPrice > basePrice + 0.10:
            #do the thing

            print("Stock went up :: Sell")

            basePrice = newPrice

        elif newPrice < basePrice + 0.10:
            print("Stock went down :: buy")
            
            basePrice = newPrice
            

        else:
            #do nothing
            print("Stock remains constant :: nothing")
            basePrice = newPrice
        

def auto_check():
    
    if current_time != "09:00:00":
        firstTime = True

        while(current_time != "16:00:00"):
            #print_watchList()
            price(firstTime)
            time.sleep(20)
            print("\n\n")

def trade_func(stock, firstTime, num, amount):
    #print(stock.name)
    #print(stock.basePrice)
    try:
        current = auto_pricer(stock.name, num)
    

        #print(current)

        currentPrice = float(current)
        #print(stock.name + " :: " + current)


        #print(type(stock.basePrice))


        if firstTime == True:
            stock.basePrice = currentPrice
            stock.oldPrice = currentPrice
            print(stock.name + " :: $" + str(stock.basePrice))

        else:
            stock.newPrice = currentPrice

            if (stock.newPrice > (stock.boughtPrice + (stock.boughtPrice * 0.015))):
                if stock.own == True:

                    profit = stock.newPrice - stock.boughtPrice
                    totals.tP = totals.tP + profit
                    totals.cS = totals.cS - currentPrice

                    print(stock.name + " :: Stock U :: Sell    :: $" + str(currentPrice), end = '')
                    print(" :: Own = 0 :: ", end = '')

                    print("TP :: $" + str(round(totals.tP, 2)) + " :: ", end = '')
                    print("TS :: $" + str(round(totals.cS, 2)) + "\n")


                    sell_order(str(stock.name), amount, "sell", "market", "day")

                    stock.up += 1
                    stock.down = 0


                    stock.oldPrice = stock.newPrice
                    stock.own = False
                else:
                    #print(stock.name + " :: Stock U :: Nothing" + " :: $" + str(currentPrice), end = '')

                    stock.oldPrice = stock.newPrice

                    stock.up += 1
                    stock.down = 0
            

            elif (stock.newPrice > stock.oldPrice):
                #print(stock.name + " :: Stock U :: Nothing" + " :: $" + str(currentPrice), end = '')

                stock.oldPrice = stock.newPrice

                stock.up += 1
                stock.down = 0

                '''elif (stock.newPrice == stock.oldPrice):
                #do nothing
                #print(stock.name + " :: Stock C :: Nothing" + " :: $" + str(currentPrice), end = '')'''


            elif (stock.newPrice < (stock.oldPrice - (stock.oldPrice * 0.015))):
                if stock.own == False:
                    print(stock.name + " :: Stock D :: Buy" + "     :: $" + str(currentPrice), end = '')
                    print(" :: Own = " + str(amount) + " :: ", end = '')
                    print("TP :: $" + str(round(totals.tP, 2)) + " :: ", end = '')
                    print("TS :: $" + str(round(totals.cS, 2)) + "\n")

                    
                    totals.cS = totals.cS + currentPrice

                    stock.boughtPrice = currentPrice
                    stock.oldPrice = stock.newPrice
                    stock.own = True
                    stock.down += 1
                    stock.up = 0

                    create_order(str(stock.name), amount, "buy", "market", "day")
                    
                else:
                    #print(stock.name + " :: Stock D :: Nothing" + " :: $" + str(currentPrice), end = '')
                    stock.down += 1
                    stock.up = 0
                    

                    #stock.basePrice = stock.newPrice
            else:
                #print(stock.name + " :: Stock D :: Nothing" + " :: $" + str(currentPrice), end = '')
                stock.oldPrice = stock.newPrice
                stock.down += 1
                stock.up = 0
            
            if(stock.own == True) & (stock.down == 6):
                print("Gave Up", end = '')
                print(" :: Own = 0 :: ")

                print("TP :: $" + str(round(totals.tP, 2)) + " :: ", end = '')
                print("TS :: $" + str(round(totals.cS, 2)) + "\n")

                sell_order(str(stock.name), amount, "sell", "market", "day")
                stock.own = False

            if(stock.own == True) & (currentPrice < stock.boughtPrice - (stock.boughtPrice * 0.03)):
                print("gave up", end = '')
                print(" :: Own = 0 :: ")

                print("TP :: $" + str(round(totals.tP, 2)) + " :: ", end = '')
                print("TS :: $" + str(round(totals.cS, 2)) + "\n")


                sell_order(str(stock.name), amount, "sell", "market", "day")
                stock.own = False


            '''if(stock.own == True):
                print(" :: Own = " + str(amount) + " :: ", end = '')
            else:
                print(" :: Own = 0 :: ", end = '')'''
    except ValueError:
        print("Error with get_text()")

        #trade_func(stock, firstTime, num, amount)

        

def autoTrade(stock):
    
    if current_time != "09:00:00":

        #fill_stocklist_auto()

        firstTime = True

        index = 0
        num = 2
        amount = 20

        while(current_time != "16:00:00"):
            #print_watchList()

            if num == 0:
                trade_func(stock, firstTime, num, amount)

                num = 1

            elif num == 1:
                trade_func(stock, firstTime, num, amount)

                num = 2

            elif num == 2:
                trade_func(stock, firstTime, num, amount)

                num = 4
            
            elif num == 3:
                trade_func(stock, firstTime, num, amount)

                num = 0

            elif num == 4:
                trade_func(stock, firstTime, num, amount)

                num = 2


            
            if index == 0:
                index = 1
                firstTime = False

            #print("TP :: $" + str(round(totals.tP, 2)) + " :: ", end = '')
            #print("TS :: $" + str(round(totals.cS, 2)) + "\n")

            time.sleep(5)



fill_stocklist_auto()

txxt = open("C:/VS/TEST/Tester.txt", "r")

s_tx = int(txxt.read())

autoTrade(auto_stocklist[s_tx])
#autoTrade(auto_stocklist[0])