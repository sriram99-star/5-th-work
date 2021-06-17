# program to remove a key from  a dictionary
a = {}
while True:
    num1 = int(input("Enter 1 to add elements in dictionary ,2 to remove, 3 to exit "))
    if num1 == 1:
        c = eval(input("enter key :"))
        d = eval(input("enter value :"))
        a[c] = d
    if num1==2 :
        f=eval(input("enter the key to be deleted"))
        if f in a:
            del a[f]
            print("success")
        else:
            print("not found")
    if num1==3:
        break
print(a)
