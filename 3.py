#coding:utf-8
import random
poker=[]
num=range(1,14)
color=['rpeach','block','flower','bpeach']
for i in num:
    for j in color:
        k=str(i)+j
        poker.append(k)
poker+=('Joker','joker')
a=random.sample(poker,17)#玩家a的牌
print a
for i in a:
    poker.remove(i)
b=random.sample(poker,17)#玩家b的牌
print b
for j in b:
    poker.remove(j)
c=random.sample(poker,17)#玩家c的牌
print c
for k in c:
    poker.remove(k)
leave=poker#剩余的牌
print leave
