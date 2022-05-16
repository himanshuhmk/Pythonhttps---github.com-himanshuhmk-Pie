def compare(num1, num2, num3):
    if num1<num2:
        if num2<num3:
            return num3
        else:
            return num2
    else:
         if num1<num3:
            return num3
         else:
                return num1
a=int(input("Enter: "))
b=int(input("Enter: "))
c=int(input("Enter: "))
print(compare(a, b, c))