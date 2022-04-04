class cat:
    def __init__(self,zhonglei,name):
        self.zhonglei=zhonglei
        self.name=name

    def miaomiaobark(self):
        print("{}在喵喵叫。".format(self.name))

    def eat(self,food):
        print("{}在吃{}。".format(self.name,food))

    def jump(self):
        print("{}在跳。".format(self.name))

cat1=cat("猫","小白猫")
print("种类为：{}，名字为：{}。".format(cat1.zhonglei,cat1.name))
cat1.miaomiaobark()
cat1.eat("鲈鱼")
cat1.jump()
cat2=cat("猫","小红猫")
print("种类为：{}，名字为：{}。".format(cat2.zhonglei,cat2.name))
cat2.miaomiaobark()
cat2.eat("带鱼")
cat2.jump()
cat3=cat("猫","小蓝猫")
print("种类为：{}，名字为：{}。".format(cat3.zhonglei,cat3.name))
cat3.miaomiaobark()
cat3.eat("红烧鱼")
cat3.jump()