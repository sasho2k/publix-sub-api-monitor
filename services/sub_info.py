class sub:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.savingMsg = ""
        self.description = ""
        self.productID = ""
        self.itemCode = 0

    def __iter__(self):
        return iter((self.name, self.price, self.savingMsg, self.description, self.productID, self.itemCode))

    def set_sub(self, name=None, price=None, savingMsg=None, description=None, productID=None, itemCode=None):
        if name:
            self.name = name
        else:
            self.name = ""

        if price:
            self.price = price
        else:
            self.price = ""

        if savingMsg:
            self.savingMsg = savingMsg
        else:
            self.savingMsg = ""

        if description:
            self.description = description
        else:
            self.description = ""

        if productID:
            self.productID = productID
        else:
            self.productID = ""

        if itemCode:
            self.itemCode = itemCode
        else:
            self.itemCode = ""

        return self
