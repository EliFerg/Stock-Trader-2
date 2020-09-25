import os
import time
from Stocklist import auto_stocklist, fill_stocklist_auto



class i:
    def __intit__(self, dex, runner, dx):
        self.dex = dex
        self.runner = runner
        self.dx
    dex = 0
    dx = 0


def automater():
    #fill_stocklist_auto()

    
    while i.dex <= 1:
        txxt = open("C:/VS/TEST/Tester.txt", "w+")
        txxt.write(str(i.dex))


        os.chdir('c:/VS/TEST')
        os.system("start cmd /k python Trader_Func.py")

        txxt.close()

        time.sleep(6)

        #print(i.dex)
        i.dex = i.dex + 1