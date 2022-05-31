
a=input()
print(a)
# b=a.find(",")
# c=a.find(".")

first=a.replace(",",",\n\t")  
second=first.replace("!","!\t")
second=first.replace(" Tha","\nTha")
print (second)