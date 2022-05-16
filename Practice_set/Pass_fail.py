def average(z):
   
    v = (z/80)*100
   
    return v 
    
    


a = int(input("Score in Maths: "))
if a <= 80 and a < 0:
    print("Invalid Maths Marks")


b = int(input("Score in Science: "))
if b <= 80 and b < 0:
    print("Invalid Maths Marks")


c = int(input("Score in Social Science: "))
if c <= 80 and c < 0:
    print("Invalid Maths Marks")
if (average(a)) >= 33:
    print("Pass")
else:
    print("Fail")
if (average(b)) >= 33:
    print("Pass")
else:
    print("Fail")
if (average(c)) >= 33:
    print("Pass")
else:
    print("Fail")
# print(average(a))
# print(average(b))
# print(average(c))
