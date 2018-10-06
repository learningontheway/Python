import math
x=int(input("please input x= "))
y=int(input("please input y= "))
z=int(input("please input z= "))
if x+y>z and x-y<z:
    print("this is a tringle of"),
    if x==y or x==z or y==z:
        if x==y and x==z:
            print("等边三角形")
            exit(0)
        else:
            print("等腰三角形")
            exit(0)
    if x*x+y*y==z*z or x*x+z*z==y*y or y*y+z*z==x*x:
        print("直角三角形")
        exit(0)
    print("一般三角形")
else:
    print("不是三角形")


