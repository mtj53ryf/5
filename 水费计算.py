def money(a):
    if (a>0 and a<=220):
        b=3.45*a
    elif (a>220 and a<=300):
        b=3.45*220+(a-220)*4.83
    elif (a>300):
        b=3.45*220+80*4.83+(a-300)*5.83
    else:
        print("输入有误")
        quit()
    print("总水费：{:.2f}元".format(b))

a=eval(input("请输入用水量："))
while(a<0):
    print("输入有误，请重新输入")
    a=eval(input("请输入用水量："))
else:
    money(a)