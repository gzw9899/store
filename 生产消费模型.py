'''
    多线程：
        1. 子类必须继承threading类

        2.重写run方法：
            写程序的任务代码，写在run方法里

        3.启动线程： start()

    厨师：
    三个厨师(ca,cb,cc)同时在造面包，当篮子中的面包=500，
    厨师稍等2秒，然后继续判断篮子是否已满，若不满继续造

    客户：
    客户有6位（ra,rb,rc,rd,re,rf），分别有3000元，同时在抢面包，当篮子面包不够的时候，
    稍等2秒然后再去买。一直到3000花完为止。

    篮子中只能装500只面包，每个3元
'''

from threading import Thread
import time

# 全局变量面包总量
bakery = 0

class Chef(Thread):
    chef_name = ""
    def run(self) -> None:
        global bakery,chef_name
        while True:
            if bakery >= 0 and bakery < 500 :
                bakery += 1
                print("%s制作了一个面包,篮子中有%s个面包" % (self.chef_name, bakery))
            elif bakery >= 500:
                print("篮子满了")
                time.sleep(5)


class Client(Thread):
    client_name = ""
    def run(self) -> None:
        global bakery, client_name
        money = 3000
        while True:
            if bakery != 0:
                money -= 3
                bakery -= 1
                print(self.client_name, "购买了一个面包,还剩%s元" % money)
                if money <= 0:
                    print("没钱了")
                    break
            elif bakery == 0:
                print("面包没有了")
                time.sleep(2)





# 创建对象
c1 = Chef()
c2 = Chef()
c3 = Chef()
r1 = Client()
r2 = Client()
r3 = Client()
r1.client_name = "ra"
r1.client_name = "rb"
r1.client_name = "rc"
c1.chef_name = "ca"
c2.chef_name = "cb"
c3.chef_name = "cc"
# 启动线程
c1.start()
c2.start()
c3.start()
r1.start()
r2.start()
r3.start()
