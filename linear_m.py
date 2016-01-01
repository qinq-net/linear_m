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
##        Version:  1.3
##        Created:  11/25/2015
##
##         Arthor:  Meng Ziyuan (14191050)
##                  Qin Yuhao   (14191033)
##   Organization:  School of Physics and Nuclear Energy Engineering,
##                  Beihang University
##
##====================================================================##

import math
import sys
modes=['linear','square']
submodes=['both','x','y']
from getopt import getopt
opts,args=getopt(sys.argv[1:],'',['err=','mode=','submode='])
#for o,a in opts:
#    if o == '--err':
#        err = float(a)
#        break
#else: err=None
o,a = [],[]
for oi,ai in opts:
    o.append(oi)
    a.append(ai)
#print(o,a)
if '--err' in o: err = float(a[o.index('--err')])
else: err=None
if '--mode' in o: mode = str(a[o.index('--mode')]).lower()
else: mode=None
if mode not in modes: mode = 'linear'
if '--submode' in o: submode = str(a[o.index('--submode')]).lower()
else: submode=None
if submode not in submodes: submode = 'both'

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

if mode=='square':
    if submode != 'y': x=[math.pow(i,2) for i in x]
    if submode != 'x': y=[math.pow(i,2) for i in y]

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
if err: s_sum = err
else: s_sum=math.sqrt(sum([(y[i]-(a+b*x[i]))**2/(n-2) for i in range(n)]))
print('Standard Error of y: s(y)='+str(s_sum))
print('Uncertainties of the coefficients:')
ua_b=math.sqrt(s_sum*s_sum/(sum_x2-sum(x)**2/n))
print("ua(b)="+str(ua_b))
uaa=math.sqrt(sum_x2/n)*ua_b
print("ua(a)="+str(uaa))
