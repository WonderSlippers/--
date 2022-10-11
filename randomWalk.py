import random
import time
import matplotlib.pyplot as plt

import numpy as np

# n为走的步数，xy为起始角度,d为死亡距离

class Plot:


    x =  np.pi
    y =  np.pi/2
    death = False
    step_x = [x]
    step_y = [y]
    # 每个点最多能走的步数
    leftsteps=50;
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.step_x = [x]
        self.step_y = [y]


    def randWalkOneStep(self):

        move = random.randint(0, 3)
        if move == 0:
            self.x += np.pi / 100
        if move == 1:
            self.x += -np.pi / 100
        if move == 2:
            self.y += np.pi / 200
        if move == 3:
            self.y += -np.pi / 200

        self.step_x.append(self.x)
        self.step_y.append(self.y)
        self.leftsteps-=1
        if self.leftsteps<1:
            self.death=True

            return True

    def detectDistance(self, allPlot):
        n = len(allPlot)

        for i in range(n):
            p = allPlot[i]
            if not p.death:

                d = getTwoPlotDistance(self.x, self.y, p.x, p.y)
                if (0.0 < d) & (d <= np.pi / 100):
                    print("太近了太近了")
                    return True
        return False


def getTwoPlotDistance(u0, v0, u1, v1):
    x1 = np.cos(u0) * np.sin(v0)

    y1 = np.sin(u0)*np.sin(v0)

    z1 = np.sin(u0)

    x2 = np.cos(u1) * np.sin(v1)

    y2 = np.sin(u1) * np.sin(v1)

    z2 = np.sin(u1)

    # 利用pow()函数计算两点间夹角
    x = np.array((x1, y1, z1))
    y = np.array([x2, y2, z2])

    # 分别计算两个向量的模：
    l_x = np.sqrt(x.dot(x))
    l_y = np.sqrt(y.dot(y))

    # 计算两个向量的点积
    dian = x.dot(y)

    # 计算夹角的cos值：
    cos_ = dian / (l_x * l_y)

    # 求得夹角（弧度制）：
    angle_hu = np.arccos(cos_)

    return angle_hu




'''Plotting the 2-D Random Walks'''

#创建n个点
n=100
#记录n的变化
markn=n;
allPlot=[Plot]
# 存活的点的个数
aliveNow=n
aliveBefore=n
for i in range(1,n+1):
    #随机生成点的角度
    allPlot.append(Plot(random.randint(0, 7),random.randint(0,4)))


step = 0
while(aliveNow>0):
    # 每个点对周围进行探测
    dead=[]

    for i in range(1,n+1):
        p=allPlot[i]
        if(p.death==False):

            if( p.detectDistance(allPlot)):
                aliveNow -= 1
                dead.append(i)

    # 集中处死
    for i in range(len(dead)):
        allPlot[dead[i]].death=True
        print("点"+str(dead[i])+"死亡")



    #活着的点走一步
    for i in range(1, n + 1):
        if allPlot[i].death==False :
            if allPlot[i].randWalkOneStep():
                aliveNow -= 1
                print("点"+str(i)+"老死了")

    # 生成非自然死亡数/2个数的点
    for j in range(round(len(dead) / 2)):
        allPlot.append(Plot(random.randint(0, 7), random.randint(0, 4)))
        aliveNow += 1
        n += 1
        print("生成新的点...")
    step += 1

    print(step)

#画画
    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    c = colors[random.randint(0, 6)]

    for i in range(1, n + 1):
        if allPlot[i].death==False :

            # Make data

            u = allPlot[i].step_x

            v = allPlot[i].step_y
            x1 = []
            y1=[]
            z1=[]
            x1.append( np.cos(allPlot[i].x) * np.sin(allPlot[i].y))

            y1.append( np.sin(allPlot[i].x) * np.sin(allPlot[i].y))

            z1.append(  np.sin(allPlot[i].x))


            ax.scatter(x1, y1, z1, c)

    ax.set_xlabel('X Label')

    ax.set_ylabel('Y Label')

    ax.set_zlabel('Z Label')

    plt.show()
    time.sleep(0.1)
print("ALL DEAD")


