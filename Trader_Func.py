from Stocklist import auto_pricer, auto_stocklist, fill_stocklist_auto
from Stock_class import STOCK
from Config_Functions import create_order, sell_order



class totals():
    def __init__(self, tP, cS):
        self.tP = totals.tP
        self.cS = totals.cS
    tP = 0.0
    cS = 0.0


def stock_upT(stock, cPrice):
    print("Up T :: ", end = '')

    if (cPrice > stock.oldPrice):

        if (cPrice > stock.lmax):
            stock.lmax = cPrice

        if (stock.up <= 4):
            stock.up += 1

        if (stock.down > 0):
            stock.down -= 1

        print("Stock U :: ", end = '')
    
    elif (cPrice < stock.oldPrice):

        if (stock.down <= 4):
            stock.down += 1

        if(stock.up > 0):
            stock.up -= 1

        print("Stock D :: ", end = '')

    elif(cPrice == stock.oldPrice):
        print("Constant :: ", end = '')

    stock.oldPrice = cPrice

def stock_downT(stock, cPrice):
    print("DownT :: ", end = '')

    stock.lmax = (stock.lmax * .90)
    
    if cPrice < stock.lmin:
        stock.lmin = cPrice

    if (stock.own == True) and (cPrice >= stock.boughtPrice):

        print("Sell :: ", end = '')

        stock.own = False
        sell_order(str(stock.name), 20, "sell", "market", "day")

        totals.tP = totals.tP + (cPrice - stock.boughtPrice)
        totals.cS = totals.cS - cPrice
    
    elif (stock.own == True) and (cPrice < (stock.boughtPrice * 0.93)):

        print("Give Up :: ", end = '')

        stock.sells += 1

        stock.own = False

        totals.tP = totals.tP + (cPrice - stock.boughtPrice)
        totals.cS = totals.cS - cPrice

        sell_order(str(stock.name), 20, "sell", "market", "day")

    elif(cPrice == stock.oldPrice):
        print("Constant :: ", end = '')

    if(cPrice < stock.oldPrice):

        stock.lmin = cPrice

        if (stock.down <= 4):
            stock.down += 1

        if (stock.up > 0):
            stock.up -= 1
    
    elif(cPrice > stock.oldPrice):

        if (stock.up <= 4):
            stock.up += 1
        
        if (stock.down > 0):
            stock.down -= 1

    stock.oldPrice = cPrice

def stock_trade(stock, cPrice):
    print("Trade :: ", end = '')

    if (stock.own == False):

        if ((stock.dOver == True) and (cPrice > stock.lmin)):

            print("Buy :: ", end = '')

            stock.own = True

            stock.buys += 1

            create_order(str(stock.name), 20, "buy", "market", "day")

            stock.boughtPrice = cPrice

            totals.cS = totals.cS + stock.boughtPrice
        

    elif (stock.own == True):

        if (cPrice <= stock.lmax) and (cPrice < stock.boughtPrice):
            
            print("sell :: ", end = '')

            stock.own = False

            stock.sells += 1

            sell_order(str(stock.name), 20, "sell", "market", "day")

            totals.tP = totals.tP + (cPrice - stock.boughtPrice)
            totals.cS = totals.cS - cPrice

        if (stock.uOver == True) and (cPrice >= stock.boughtPrice):

            print("sell :: ", end = '')

            stock.own = False

            stock.sells += 1

            sell_order(str(stock.name), 20, "sell", "market", "day")

            totals.tP = totals.tP + (cPrice - stock.boughtPrice)
            totals.cS = totals.cS - cPrice
        
        elif (stock.downT == True) and (cPrice >= stock.boughtPrice):

            print("Give Up :: ", end = '')

            stock.sells += 1

            stock.own = False

            sell_order(str(stock.name), 20, "sell", "market", "day")

            totals.tP = totals.tP + (cPrice - stock.boughtPrice)
            totals.cS = totals.cS - cPrice
        
    if(cPrice < stock.oldPrice):

        print("Down    :: ", end = '')

        stock.lmin = cPrice

        if (stock.down <= 4):
            stock.down += 1

        if (stock.up > 0):
            stock.up -= 1
    
    elif(cPrice > stock.oldPrice):

        print("Up      :: ", end = '')

        if (stock.up <= 4):
            stock.up += 1
        
        if (stock.down > 0):
            stock.down -= 1
    else:
        print("Constant :: ", end = '')

    stock.oldPrice = cPrice

def Trader(stock, firstTime, num, amount):

    try:
        cPrice = float(auto_pricer(stock.name, num))

        print(str(cPrice) + " :: ", end = '')

        if (stock.up > 2) and (stock.up <= 4):
            stock.downT = False
            stock.dOver = True

        elif (stock.up > 4):
            stock.upT = True
            stock.uOver = False
            
        elif (stock.down > 2) and (stock.down <= 4):
            stock.upT = False
            stock.uOver = True
            
        elif (stock.down > 4):
            stock.downT = True
            stock.dOver = False


        if (firstTime == True):
            #setup base prices and intitialize old price
            stock.basePrice = cPrice
            stock.oldPrice = cPrice
            stock.lmax = cPrice

            firstTime = False

            print("\n\n" + stock.name + " :: $" + str(stock.basePrice))


        else:
            if (stock.upT == True):
                stock_upT(stock, cPrice)

            elif (stock.downT == True):
                stock_downT(stock, cPrice)

            else:
                stock_trade(stock, cPrice)

            print("Up :: " + str(stock.up) + " :: Down :: " + str(stock.down) + " :: B :: " + str(stock.buys) + " :: S :: " + str(stock.sells) + "\n\n")
    except OSError as err:
        print("Error")
        print(str(err))


def Search(stock):

        firstTime = True

        num = 1
        amount = 20
        cont = True

        while(cont == True):
            #print_watchList()

            print(stock.name + " :: ", end = '')

            if num == 0:#Bing
                Trader(stock, firstTime, num, amount)

                num = 1

            elif num == 1:#Yahoo
                Trader(stock, firstTime, num, amount)

                num = 2

            elif num == 2:#Yahoo Finance
                Trader(stock, firstTime, num, amount)

                num = 4
            
            elif num == 3:#Finviz
                Trader(stock, firstTime, num, amount)

                num = 0

            elif num == 4:#Google
                Trader(stock, firstTime, num, amount)

                num = 1
            
            if (firstTime == True):
                firstTime = False

fill_stocklist_auto()

response = input("1 for auto and 2 for manual :: ")

if response == "1":
    txxt = open("C:/VS/TEST/Tester.txt", "r")

    s_tx = int(txxt.read())

    Search(auto_stocklist[s_tx])

elif response == "2":
    s_tx = input("Enter a stock :: ")

    Search(auto_stocklist[s_tx])