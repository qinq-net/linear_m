#!/usr/bin/python3

##====================================================================##
##
## Copyright (C) 2015 School of Physics and Nuclear Energy Engineering,
## Beihang University
##                                                                      
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
##====================================================================##
##  
##       Filename:  linear_m.py
##    Description:  Perform a simple linear regression from stdin
##                  Input x axis first, then y axis
##        Version:  1.1
##        Created:  10/14/2015
##
##         Arthor:  Meng Ziyuan (14191050)
##                  Qin Yuhao   (14191033)
##   Organization:  School of Physics and Nuclear Energy Engineering,
##                  Beihang University
##
##====================================================================##

import math

def get_table():## Input all in a line from stdin
    # print('input x table first.')
    x,y,n=[],[],0
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
    return x, y, len(x)
x,y,n = get_table()

print("x="+str(x))
print("y="+str(y))
print("n="+str(n))

sum_xy = sum([x[i]*y[i] for i in range(n)]) # sum of x*y
sum_x2 = sum([x[i]*x[i] for i in range(n)]) # sum of x^2

# calculate coefficients
b=(sum(x)*sum(y)-n*sum_xy)/(sum(x)*sum(x)-n*sum_x2)
a=(sum_xy*sum(x)-sum(y)*sum_x2)/(sum(x)*sum(x)-n*sum_x2)
print("b="+str(b))
print("a="+str(a))
print("Regression: " + 'y='+str(b)+'x'+('+' if a>0 else '')+str(a))

# measurement of correlation coefficient
r_sum1=sum([(x[i]-sum(x)/n)*(y[i]-sum(y)/n) for i in range(n)])
r_sum21=sum([(x[i]-sum(x)/n)*(x[i]-sum(x)/n) for i in range(n)])
r_sum22=sum([(y[i]-sum(y)/n)*(y[i]-sum(y)/n) for i in range(n)])
r_sum2=math.sqrt(r_sum21*r_sum22)
r=r_sum1/r_sum2
print('PPMCC r='+str(r))

# measurement of standard error for y
s_sum=sum([(y[i]-(a+b*x[i]))*(y[i]-(a+b*x[i])) for i in range(n)])
print('Uncertainties of the coefficients:')
uab=b*math.sqrt((1/(r*r)-1)/(n-2))
print("ua(b)="+str(uab))
uaa=math.sqrt(sum_x2/n)*uab
print("ua(a)="+str(uaa))
