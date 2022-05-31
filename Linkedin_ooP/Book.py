class book:
    def __init__(self, name, author, price):
        self.name=name
        self.author=author
        self.price=price
    def getprice(self):
        if hasattr(self, "discount"):
            return self.price-(self.discount*self.price)
        else:
            return self.price
    def discount(self, discount):
        self.discount=discount

auto=book("Dear", "Ammy", 350)
# auto.name="Dear"
# auto.author="Ammy"
# auto.price=351
print(auto.name)
print(auto.author)
print(auto.price)
auto.discount(0.15)
print(auto.getprice())