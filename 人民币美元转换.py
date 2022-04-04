def Dollar2RMB(a):
    b=round(a,2)*6
    print("{:.2f}美元={:.2f}人民币".format(a,b))

def RMB2Dollar(a):
    c=round(a,2)/6
    print("{:.2f}人民币={:.2f}美元".format(a,c))

a=eval(input("请输入钱数："))
while(a<0):
    print("输入有误，请重新输入")
    a=eval(input("请输入钱数："))
else:
    Dollar2RMB(a)
    RMB2Dollar(a)