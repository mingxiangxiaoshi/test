#coding:utf-8
import random
money=int(raw_input('总金额:'))
man=int(raw_input('总人数:'))
def weixinhongba(money,man):
    j = []
    k = 0
    money=100*money
    while k<man:
        a=random.randint(1,money-(4-k))
        j.append(a/100.0)
        money=money-a
        k=k+1
    print j
weixinhongba(money,man)
# import random
# def redPacket(people, money):
#     result = []
#     remain = people
#     for i in range(people):
#         remain -= 1
#         if remain > 0:
#             m = random.randint(1, money - remain)
#         else:
#             m = money
#         money -= m
#         result.append(m / 100.0)
#     print result
# people = int(input('红包个数:\n'))
# money = int(input('总金额:\n') * 100)
# redPacket(people, money)a
