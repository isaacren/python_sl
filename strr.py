#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Hello, %s' % '中文')
print('Hi, %s, you have $%d.' % ('Michael',100000))

print('%d - %02d'%(3,15))
print('%.2f' % 3.1415926)

print('Hello, {0}, 成绩提高了{1:.1f}%'.format('小明', 17.125))

s1=72
s2=85

r=(s2-s1)/s1*100

print ('小明成绩提高了%.1f%%' % r)

print('小明成绩提高了{0:.1f}%'.format(r))