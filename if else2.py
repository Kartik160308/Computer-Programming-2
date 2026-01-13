a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Ente a number:"))

if a>=b and a>=c:
    print("Largest number", a)
elif b>=a and b>=c:
    print("Largest number", b)
else:
    print("Largest number", c)

if a<=b and a<=c:
    print("Smallest number", a)
elif b<=a and b<=c:
    print("Smallest number", b)
else:
    print("Smallest number", c)
