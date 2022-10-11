import random
import time

import matplotlib.pyplot as plt


# n为走的步数，xy为起始坐标,d为死亡距离

class Plot:
    x = 0
    y = 0
    death = False
    step_x = [x]
    step_y = [y]
    # 每个点最多能走的步数
    leftsteps=10;
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.step_x = [x]
        self.step_y = [y]


    def randWalkOneStep(self):

        move = random.randint(0, 3)
        if move == 0:
            self.x += 1
        if move == 1:
            self.x += -1
        if move == 2:
            self.y += 1
        if move == 3:
            self.y += -1

        self.step_x.append(self.x)
        self.step_y.append(self.y)
        self.leftsteps-=1
        if self.leftsteps<1:
            self.death=True
    @classmethod
    def detectDistance(self, allPlot):
        n = len(allPlot)
        for i in range(n):
            p = allPlot[i]
            d = getTwoPlotDistance(self.x, self.y, p.x, p.y)
            if (0.0 < d) & (d <= 1.0):

                return True
        return False


def getTwoPlotDistance(x0, y0, x1, y1):

    # 利用pow()函数计算两点间距离
    r = pow(pow(x1 - x0, 2) + pow(y1 - y0, 2), 0.5)

    return r




'''Plotting the 2-D Random Walks'''

#创建n个点
n=10
#记录n的变化
markn=n;
allPlot=[Plot]
# 存活的点的个数
aliveNow=n
aliveBefore=n
for i in range(1,n+1):
    #在-n到n之间生成点
    allPlot.append(Plot(random.randint(-n, n),random.randint(-n, n)))


step = 0
while(aliveNow>0):
    # 每个点对周围进行探测
    dead=[]
    for i in range(1,n+1):
        if(allPlot[i].death==False):
            if( allPlot[i].detectDistance(allPlot)):
                aliveNow -= 1
                dead.append(i)

    # 集中处死
    for i in range(len(dead)):
        allPlot[dead[i]].death=True


    #活着的点走一步
    for i in range(1, n + 1):
        if allPlot[i].death==False :
            allPlot[i].randWalkOneStep()

    #生成死亡数/2个数的点
    for j in range(1,round((aliveBefore-aliveNow)/2)):
        allPlot.append(Plot(random.randint(-3*n, 3*n),random.randint(-3*n, 3*n)))
        aliveNow+=1
        n+=1
    aliveBefore=aliveNow

    step += 1

    # 开始画图，画一次一帧，0.5秒播放一帧
    # 第一上色
    flag = 0
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    markers = ['+', '*', ',', 'o', '.', '1', 'p']
    if flag == 0:
        linecolor = []
        linecolor.append(" ")
        for i in range(1, n + 1):
            if not allPlot[i].death:
                c = colors[random.randint(0, 6)]
                m = markers[random.randint(0, 6)]
                s = c + m
                linecolor.append(s)
    flag = 1
    # 如果有新的点产生
    if not n == markn:
        for i in range(1, markn - n):
            c = colors[random.randint(0, 6)]
            m = markers[random.randint(0, 6)]
            s = c + m
            linecolor.append(s)
        markn = n

    for i in range(1, n + 1):
        if not allPlot[i].death:
            plt.plot(allPlot[i].step_x, allPlot[i].step_y, linecolor[i], label="randwalk" + str(i))

    plt.title("2-D Random Walks")
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True)
    plt.show()
    time.sleep(0.5)

    print(step)
print("ALL DEAD")


