#随机选择人物：A+、S、SS
import random
list1 = ["A+","S","SS"]#,"SSR"]
name = list1[random.randint(0,len(list1)-1)]
print("你选中了 %s 级人物" % name)
#游戏规则：
# 1.所有人物初始值为10
num = 10
#A+级没有增益
if name == "A+":
    while True:
        i=0
        list2 = []#数字容器
        while i<3 :# 2.随机生成3个数字
            i= i+1
            a=random.randint(8,30)#随机数字范围
            list2.append(a)
        print("随机到三个数",list2)
        num1 = list2[random.randint(0, len(list2) - 1)]  # 3.随机选择1个数字
        print("帮你选中一个数",num1)
        list3 = [1,2]#判断加减
        name2 = list3[random.randint(0, len(list3) - 1)]# 4.随机选择的数字和初始值进行运算
        if name2 == 1 :#如果随机到1进行加法运算
            num = num1 + num
            print("当前值为 %d" %num)
        elif name2 == 2 :#否则进行减法运算
            num = num1 - num
            print("当前值为 %d" %num)
        if num >100 :# 5.计算后大于100则任务成功
            print("恭喜！任务成功")
            break
        elif num <= 0 :# 6.计算后小于或等于0则任务失败。
            print("遗憾，任务失败")
            break
#S级初始值为30
if name == "S" :
    num =30
    while True:
        i = 0
        list2 = []  # 数字容器
        while i < 3:  # 2.随机生成3个数字
            i = i + 1
            a = random.randint(8, 30)  # 随机数字范围
            list2.append(a)
        print("随机到三个数", list2)
        num1 = list2[random.randint(0, len(list2) - 1)]  # 3.随机选择1个数字
        print("帮你选中一个数", num1)
        list3 = [1, 2]  # 判断加减
        name2 = list3[random.randint(0, len(list3) - 1)]  # 4.随机选择的数字和初始值进行运算
        if name2 == 1:  # 如果随机到1进行加法运算
            num = num1 + num
            print( "当前值为 %d" % num)
        elif name2 == 2:  # 否则进行减法运算
            num = num1 - num
            print( "当前值为 %d" % num)
        if num > 100:  # 5.计算后大于100则任务成功
            print("恭喜！任务成功")
            break
        elif num <= 0:  # 6.计算后小于或等于0则任务失败。
            print("遗憾，任务失败")
            break
#SS级初始值不会减少只会增加
if name == "SS" :
    while True:
        i = 0
        list2 = []  # 数字容器
        while i < 3:  # 2.随机生成3个数字
            i = i + 1
            a = random.randint(8, 30)  # 随机数字范围
            list2.append(a)
        print("随机到三个数", list2)
        num1 = list2[random.randint(0, len(list2) - 1)]  # 3.随机选择1个数字
        print("帮你选中一个数", num1)
        list3 = [1, 2]  # 判断加减
        name2 = list3[random.randint(0, len(list3) - 1)]  # 4.随机选择的数字和初始值进行运算
        if name2 == 1:  # 如果随机到1进行加法运算
            num = num1 + num
            print( "当前值为 %d" % num)
        elif name2 == 2:  # 否则不进行运算
            num = num1 - num + num
            print( "当前值为 %d" % num)
        if num > 100:  # 5.计算后大于100则任务成功
            print("恭喜！任务成功")
            break
        elif num <= 0:  # 6.计算后小于或等于0则任务失败。
            print("遗憾，任务失败")
            break