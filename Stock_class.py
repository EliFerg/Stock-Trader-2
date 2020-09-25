class STOCK:
    def __intit__(self, name, basePrice, oldPrice, newPrice, own, up, down, boughtPrice, dex, lmax, lmin, upT, downT, uOver, dOver, buys, sells):
        self.name = name
        self.basePrice = basePrice
        self.oldPrice = oldPrice
        self.newPrice = newPrice
        self.boughtPrice = boughtPrice
        self.own = own
        self.up = up
        self.down = down
        self.lmax = lmax
        self.lmin = lmin
        self.upT = upT
        self.downT = downT
        self.uOver = uOver
        self.dOver = dOver
        self.buys = buys
        self.sells = sells
    
    up = 0
    down = 0
    uOver = False
    dOver = False
