class animal:
    def __init__(self,zhonglei,name):
        self.zhonglei=zhonglei
        self.name=name

    def eat(self,food):
        print("{}在吃{}。".format(self.name,food))

    def jump(self):
        print("{}在跳。".format(self.name))

class cat(animal):
    def miaomiaobark(self):
        print("{}在喵喵叫。".format(self.name))

class dog(animal):
    def wangwangbark(self):
        print("{}在汪汪叫。".format(self.name))

cat1=cat("猫","小黑猫")
print("种类为：{}，名字为：{}。".format(cat1.zhonglei,cat1.name))
cat1.miaomiaobark()
cat1.eat("扁鱼")
cat1.jump()
dog1=dog("狗","小黄狗")
print("种类为：{}，名字为：{}。".format(dog1.zhonglei,dog1.name))
dog1.wangwangbark()
dog1.eat("肉骨头")
dog1.jump()