x=int(input('请输入一个整数x='))
i=2
print("因式分解后的结果是x=",end="")
while i < x+1:
    if x % i ==0:
        print(end="*%d" % i)
        x = x/i
        i=2
    else:
        i=i+1