#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_author_ = 'shirunqi'

# 1.代码缩进问题一定要注意
# 2.使用的变量应进行初始化

def least_squares_function(x,y):
	n = len(x)
	a1 = a2 = a3 = a4 = 0
	a11 = a12 = a21 = a22 = a31 = a32 = 0
	w0 = w1 = 0
	for i in range(0,n):
		a1 += x[i] * y[i]
		a2 += x[i]
		a3 += y[i]
		a4 += x[i] * x[i]
	a11 = n * a1
	a12 = a2 * a3
	a21 = n * a4
	a22 = a2 * a2
	a31 = a4 * a3
	a32 = a2 * a1
	w0 = (a31 - a32) / (a21 - a22)
	w1 = (a11 - a12) / (a21 - a22)
	w0 = round(w0,2)
	w1 = round(w1,2)
	return w0,w1

x = [1,2,3,4]
y = [4,5,6,7]
w0,w1 = least_squares_function(x,y)
print(w0,w1)	