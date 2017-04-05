#coding:utf-8
height=raw_input('please input your height:')
weight=raw_input('please input your weight:')
BMI=float(weight)/float(height)**2
print BMI
if  BMI<18.5:
    print '体重偏轻'
elif 18.5<=BMI<24:
    print '体重正常'
else:
    print '体重偏重'
