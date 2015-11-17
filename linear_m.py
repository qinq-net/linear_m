#!/usr/bin/python3
import math

x=[]
y=[]
n=0

## Input one by one from stdin
# print("input 'e' to stop input")
# while(True):
#     print("x"+str(n+1)+"=")
#     xn=input()
#     if xn=='e':
#         break
#     else:
#         xn=float(xn)
#         n=n+1
#         x.append(float(xn))
#         print("y"+str(n)+"=")
#         yn=float(input())
#         y.append(float(yn))

## Input all in a line from stdin
# print('input x table first.')
while True:
    try:
        t=input()
        if t!='e': xn=t.split()
        else: break
        for i in range(len(xn)): xn[i] = float(xn[i])
        yn=input().split()
        for i in range(len(yn)): yn[i] = float(yn[i])
        x.extend(xn)
        y.extend(yn)
    except EOFError:
        break
if len(x) != len(y): raise TypeError('items not matched')
n=len(x)

print("x="+str(x))
print("y="+str(y))
print("n="+str(n))

sum_xy=0
for i in range(len(x)):
    sum_xy=sum_xy+x[i]*y[i]
#print(sum_xy)
    
sum_x2=0
for i in range(len(x)):
    sum_x2=sum_x2+x[i]*x[i]
#print(sum_x2)

b=(sum(x)*sum(y)-n*sum_xy)/(sum(x)*sum(x)-n*sum_x2)
a=(sum_xy*sum(x)-sum(y)*sum_x2)/(sum(x)*sum(x)-n*sum_x2)

print("b="+str(b))
print("a="+str(a))
if(a<0):
    print("一元线性回归：y="+str(b)+"x"+str(a))
else:
    print("一元线性回归：y="+str(b)+"x+"+str(a))

r_sum1=0
r_sum21=0
r_sum22=0
for i in range(len(x)):
    r_sum1=r_sum1+((x[i]-sum(x)/n)*(y[i]-sum(y)/n))
    r_sum21=r_sum21+(x[i]-sum(x)/n)*(x[i]-sum(x)/n)
    r_sum22=r_sum22+(y[i]-sum(y)/n)*(y[i]-sum(y)/n)
r_sum2=math.sqrt(r_sum21*r_sum22)
r=r_sum1/r_sum2
print("相关系数r="+str(r))

s_sum=0
for i in range(len(x)):
    s_sum=s_sum+(y[i]-(a+b*x[i]))*(y[i]-(a+b*x[i]))
print("yi的不确定度s(y)="+str(math.sqrt(s_sum/(n-2))))

print("回归系数的不确定度估计：")
uab=b*math.sqrt((1/(r*r)-1)/(n-2))
print("ua(b)="+str(uab))
uaa=math.sqrt(sum_x2/n)*uab
print("ua(a)="+str(uaa))

# wait=input()
