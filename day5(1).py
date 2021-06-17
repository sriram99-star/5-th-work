# program for adding two dictionaries
a = {}
b = {}
while True:
    num1 = int(input(
        "Enter 1 to add elements in dictionary 1,enter 2 to add elements in dictionary 2, 3 to exit and merge two dictionaries:"))
    if num1 == 1:
        c = eval(input("enter key :"))
        d = eval(input("enter value :"))
        a[c] = d
    if num1 == 2:
        e = eval(input("enter key :"))
        f = eval(input("enter value :"))
        b[e] = f
    if num1 == 3:
        break

a.update(b)
print(a)
print("merged successfully")
