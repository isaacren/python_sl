#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#list，有序集合，可随时添加和删除其中的元素
classmates = ['Michael', 'Bob', 'Tracy']

print(len(classmates))

print(classmates[0])  #编号从0开始，0->len(list)-1
print(classmates[1])
print(classmates[2])

print(classmates[-1]) #倒数第一个元素索引也可以是-1
print(classmates[-2])
print(classmates[-3]) #第一个就是-len(list)

classmates.append('Adam') #追加元素到末尾

print(classmates)

classmates.insert(1,'Jack')#追加元素到制定位置

print(classmates)

print(classmates[-len(classmates)])

classmates.pop() #删除list末尾元素
print(classmates)

classmates.pop(2)
#pop(i)删除指定索引位置元素

print(classmates)

print(classmates[2])

classmates[1]='Sarah' #替换某元素，直接赋值
print(classmates)

L=['Apple', 123, True]
#List里的元素数据类型可以不同

s = ['python','java',['asp','php'],'scheme']
print(len(s))
print(s[2])

p = ['asp','php']
s1 = ['python','java','p','scheme']
#list元素也可以是另一个list，其中s[2]和p又是一个list
#要拿到php,可以写p[1]或者s[2][1]或者s1[2][1]

print(p[1])

print(s[2][0]) #取asp

ls=[]
print(len(ls))
#ls中一个元素也没有，是个空的List， 长度为0

#tuple，另一种有序表，叫元组
#tuple和list很像，但tuple一旦初始化就不能修改

#例如：
classmates_tuple=('Michael','Bob','Tracy')
#classmates_tuple这个tuple就不能变了，没有append和insert方法。
#但其他获取元素方法和list一样，如tuple_name[0],tuple_name[-1]
#但不能赋值成另外的元素

#tuple不可变，代码更安全，if possible，用tuple代替list

#tuple的陷阱：定义tuple时，元素就必须被确定下来

t=(1,2)

print(t)

t1=()
print(t)

t2=(1)
#定义的不是tuple，是数，因为()可以表示tuple
#又可以是数学公式中的小括号
#所以如果定义只有1个元素的tuple，必须加一个逗号来消除歧义

t3=(1,)

print(t2)
print(t3)

t4=('a','b',['A','B'])

print(t4)

t4[2][0]='X'
t4[2][1]='Y'

print(t4)
#“可变"tuple，但实际上不是t4[2]变了，t4[2]本身是个List
#是list里边的内容变了
#表面上看，tuple的元素确实变了，
#但其实变的不是tuple的元素，
#而是list的元素。
#tuple一开始指向的list并没有改成别的list，
#所以，tuple所谓的“不变”是说，
#tuple的每个元素，指向永远不变。
#即指向'a'，就不能改成指向'b'，
#指向一个list，就不能改成指向其他对象，
#但指向的这个list本身是可变的！

lls=L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(lls[0][0])
print(lls[1][1])
print(lls[2][2])