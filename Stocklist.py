import requests
from bs4 import BeautifulSoup
from Stock_class import STOCK

stockList = []
auto_stocklist = []

def get_URL():
    query = input("What stock would you like to look up:  ")
    query = query.replace(' ', '+')
    URL = f"https://google.com/search?q={query}"

    headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    currentPrice = soup.find(jsname = 'vWLAgc').get_text()
    print("$" + currentPrice)

def auto_pricer(query, num):
    names = False

    if num == 0 :#Bing
        query = query.replace(' ', '+')
        #URL = f"https://search.bing.com/search?p={query}"
        URL = f"https://www.bing.com/search?q={query}+current+stock+price"
        if (names == True):
            print("Bing")

        headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')


        currentPricer = soup.find(id = "Finance_Quote")
        currentPrice = currentPricer.find('div').get_text()
        currentPrice = round(float(currentPrice), 2)
        
        #print("$" + str(currentPrice))

        num = 1

        return currentPrice

    elif num == 1:#yahoo
        query = query.replace(' ', '+')
        URL = f"https://search.yahoo.com/search?p={query}+stock+price"
        if (names == True):
            print("Yahoo")

        headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        currentPricer = soup.find(class_ = "fin_quotePrice s-price")

        #print(currentPricer)

        currentPrice = currentPricer.get_text()  
        currentPrice = round(float(currentPrice), 2)
     
        
        #print("$" + str(currentPrice))

        num = 0

        return currentPrice    

    elif num == 2:#yahoo finance
        query = query.replace(' ', '+')
        URL = f"https://finance.yahoo.com/chart/{query}"
        if (names == True):
            print("Yahoo Finance")

        headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        lister = []
        lister2 = []

        currentPricer = soup.find(class_ = "Trsdu(0.3s) Fw(b) Fz(14px) Mb(-4px) D(ib)")
        currentPrice = currentPricer.get_text()  
        currentPrice = round(float(currentPrice), 2)


        #print("$" + str(currentPrice))

        num = 0

        return currentPrice    
    
    elif num == 3:#Finviz
        query = query.replace(' ', '+')
        URL = f"https://finviz.com/quote.ashx?t={query}"
        if (names == True):
            print("Finviz")

        headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        lister = []
        lister2 = []

        lister = soup.find_all(class_ = "table-dark-row")

        lister2 = lister[10].find_all(class_ = "snapshot-td2")

        currentPrice = lister2[5].get_text()
        currentPrice = round(float(currentPrice), 2)

        #print("$" + str(currentPrice))


        return currentPrice

    elif num == 4:#Google
        query = query.replace(' ', '+')
        URL_3 = f"https://google.com/search?q={query}+stock+price"
        #print(URL_3)
        if (names == True):
            print("Google")

        headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        page = requests.get(URL_3, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        #print(soup)

        currentPricer = soup.find(jsname = "vWLAgc").get_text()

        #print("$" + str(currentPricer))

        return currentPricer

#auto_pricer('AAPL', 2)

def addToWatchList():
    query = input("What stock would you like to add to watchlist:  ")
    stockList.append(query)

def print_watchList():
    for stock in stockList:
        query = stock
        query = query.replace(' ', '+')
        URL = f"https://google.com/search?q={query}"

        headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        currentPrice = soup.find(jsname = 'vWLAgc').get_text()
        print(stock + ":  $" + currentPrice)

#response = create_order("AAPL", 100, "buy", "market", "gtc")

def fill_stocklist_auto():
    URL_2 = f"https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/"
    #URL_2 = f"https://www.tradingview.com/markets/stocks-usa/market-movers-most-volatile/"

    headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    page = requests.get(URL_2, headers=headers)
    soup_2 = BeautifulSoup(page.content, 'html.parser')

    #print(page.status_code)

    topMovers = soup_2.find_all(class_ = "tv-screener__description")

    topMovers = soup_2.find_all(class_ = "tv-screener__symbol")


    #print(topMovers)

    index = 0
    index2 = 0
    Stock_ = []

    for mover in topMovers:
        
        if index > 12:
            break
        elif index % 2 == 0:
            if len(mover.get_text().strip()) <= 4:
                Stock_.append(STOCK())

                #print(index)

                Stock_[index2].name = mover.get_text().strip()
                Stock_[index2].own = False
                Stock_[index2].boughtPrice = 100000
                Stock_[index2].down = 0
                Stock_[index2].up = 0
                Stock_[index2].upT = False
                Stock_[index2].downT = False
                Stock_[index2].buys = 0
                Stock_[index2].sells = 0

                #print(Stock_[index2].name)

                auto_stocklist.append(Stock_[index2])

                index2 += 1
                index += 1
            else:
                index -= 1
        else:
            index += 1
    
    index = 0

    #print(len(auto_stocklist))
    #print("\n")

    while index < len(auto_stocklist):
        print(Stock_[index].name)
        index += 1
    print("\n\n\n")

#fill_stocklist_auto()