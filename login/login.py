init_username=input("请输入用户名")
init_password=input("请输入用户密码")

flag0=0 #用于显示登陆成功
flag1=0 #用于标记密码剩余尝试次数

print("用户登录")
while True:
    user=input("请输入用户名")
    if user==init_username:
        while flag1<3:
            password = input("请输入用户密码")
            if password==init_password:
                print("登陆成功")
                flag0=1
                break
            else:
                if 2-flag1!=0:
                    print("密码错误，你还有",2-flag1,"次机会")
                else:
                    print("密码三次输入错误，请重新输入用户名")
                flag1+=1
    else:
        print("用户名不存在，请重新输入")
    if flag0==1:
        break
    else:
        flag1=0





