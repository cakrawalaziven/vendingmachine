
print("+" + 16*"-" + "+")
print("|","CHIPS","|","BURGER","|")
print("|","  3  ","|","  2.5 ","|")
print("+" + 16*"-" + "+")
print("|","  1  ","|","  2   ","|")
print("+" + 16*"-" + "+")
print("|","FRIES","|","COFFEE","|")
print("|"," 2.3 ","|","   2  ","|")
print("+" + 16*"-" + "+")
print("|","  3  ","|","   4  ","|")
print("+" + 16*"-" + "+")
print("|","WATER","|"," COLA ","|")
print("|","  1  ","|","  1.5 ","|")
print("+" + 16*"-" + "+")
print("|","  5  ","|","   6  ","|")
print("+" + 16*"-" + "+")

chips = 3
burger = 2.5
fries = 2.3
coffee = 2
water = 1
cola = 1.5

n = float(input("What do you want to buy (Plase enter the number): "))
a = float(input("Enter the amount : "))

p1 = chips
p2 = burger
p3 = fries
p4 = coffee
p5 = water
p6 = cola

if n == 1:
    print("You need to pay $",chips*a)
    m = float(input("Enter your money $"))
    print("This is your change $", m - chips * a)
elif n == 2:
    print("You need to pay $",burger*a)
    m = float(input("Enter your money $"))
    print("This is your change $", m - burger * a)
elif n == 3:
    print("You need to pay $",fries*a)
    m = float(input("Enter your money $"))
    print("This is your change $", m - fries * a)
elif n == 4:
    print("You need to pay $",coffee*a)
    m = float(input("Enter your money $"))
    print("This is your change $", m - coffee * a)
elif n == 5:
    print("You need to pay $",water*a)
    m = float(input("Enter your money $"))
    print("This is your change $", m - water * a)
elif n == 6:
    print("You need to pay $",cola*a)
    m = float(input("Enter your money $"))
    print("This is your change $", m - cola * a)
else:
    print("We don't sell this item")