#meraki on more exercise question 4
a=int(input("enter the number: "))
b=int(input("enter the number: "))
c=int(input("enter the number: "))
if a > b and  a > c:
    print(a,"a is maximum number")
elif b > c and b > a:
    print(b,"b is maximum number")
elif c > b and c > a:
    print(c,"c is a maximum number")
else:
    print("invalid number")