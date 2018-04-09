#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('---建立dict---')
d={'Michael':95, 'Bob':75, 'Tracy':85}
print(d)
print('---取出Bob的分数---')
print(d['Bob'])

print('---除初始化外，通过key放入值---')
d['Adam']=67
print(d)
# key-value 通过key算出value存放的位置，取得时候根据key直接拿到value

# key - value 1:1, 1k多v，后面的v把前面的冲掉
print('---对一个key，多次赋值，只保留最后一次的value')
d['Jack']=90
print(d)
d['Jack']=88
print(d)
d['Jack']=77
print(d)

# 若key不存在，dict会报错
# 避免不存在错误
# 1 通过in判断key是否存在
print('---#1 用in判断Thomas 是否在dict内---')
print('Thomas' in d)
# 2 dict提供get()方法，若key不存在，返回None或者自己指定返回的value
print('---#2 用dict提供的get()方法判断')
print(d.get('Thomas'))
#返回None的时候，命令行交互环境不显示结果
print('自己指定get()的返回值')
print(d.get('Thomas',-2))

print('---pop(key)方法删除对应value---')
print(d)
print('删除Bob')
d.pop('Bob')
print(d)

#dict内部存放的顺序和key放入的顺序无关

print('dict VS list')
print('dict:')
print('1. 查找、插入速度快，不会随着key数量增加变慢')
print('2. 需要占用大量内存，内存浪费多')
print('list:')
print('1. 查找、插入时间随元素增加而增加')
print('2. 占用空间小，内存浪费少')
print('Conclusion:')
print('dict - 空间换时间')
#dict的key必须是不可变对象
#通过key计算位置的算法叫哈希算法- Hash
#要保证hash正确性，作为key的对象就不能变
#Python中，String,integer等都是不可变的，可以作为key
#list是可变的，不能作为key


print('---创建set---')
s = set([1,2,3])
#创建一个set, 需要提供一个list作为输入集合

print(s)
print('显示的只代表里面有这三个元素，不代表是有序的')
print('-----运行 s1 = set([1,1,2,2,3,3])')
s1=set([1,1,2,2,3,3])
print(s1)
print('会自动去重')

print('-----通过add(key)方法可添元素进去，但重复添加不会有效果-------')
s1.add(4)
s1.add(4)
s1.add(2)
print(s1)

print('---通过remove(key)方法删除元素---')
s1.remove(2)
print(s1)
#set可以看成数学意义上的无序和无重复元素的集合
#因此，两个set可以做数学意义上的交集、并集等

print('------s1和s2做交集和并集运算------')
s2=set([2,3,4])
print('---s1---')
print(s1)
print('---s2---')
print(s2)
print('---s1&s2---交集---')
print(s1 & s2)
print('---s1|s2---并集---')
print(s1|s2)
print('set与dict的唯一区别仅仅在于没有存储对应的value')
print('但set原理和dict一样，不可以放入可变对象')
print('因为无法判断两个可变对象是否相等')
print('也无法保证set内部不会有重复元素')

#可变对象，比如list，对list操作，List内部内容会变
a=['c','b','a']
print('-------初始list-a的状态------')
print(a)
print('-------整理后的list-a的内容------')
a.sort()
print(a)

#不可变对象，比如str,对str进行操作
a='abc'
print('---用A替换a中的小写a---')
print(a.replace('a','A'))
print('---用完replace(key)之后，再显示str - a的值---')
print(a)
#a是变量，'abc'是字符串对象
#对象a的内容是'abc'，其实指a本身是一个变量，它指向的对象的内容才是'abc'
#a.replace('a','A')，实际上调用replace方法，作用在字符串对象'abc'上
#实际上没有改变字符串'abc'的内容
#相反，replace方法创建了一个新字符串'Abc'并返回
#如果用变量b来指向返回字符串，就对了。
print('---用replace方法替换\'a\', a.replace(\'a\',\'A\')')
b=a.replace('a','A')
print('---str-a---')
print(a)
print('---str-b---')
print(b)
#对于不变对象来说，调用对象自身的任意方法也不会改变对象自身的内容
#相反，这些方法会创建新的对象并返回
#这样就保证了不可变对象本身永远是不可变的
