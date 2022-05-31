from re import X


x=89
def num():
    x=20
    def num2():
        global x
        x=88
    num2()
num()
print (x)