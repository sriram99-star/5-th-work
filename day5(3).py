#python program to map two list into  a dictionary
print("enter 2 list of equal length to map into dictionary")
a=eval(input("enter a list1 : "))
b=eval(input("enter a list2 : "))
c={}
for i in range(len(a)):
    c[a[i]]=b[i]
print(c)
