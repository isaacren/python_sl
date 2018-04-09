names=['Michael','Bob','Tracy']
for name in names:
		print(name)
		
#for x in ... 就是把每个元素带入x，然后执行缩进处的语句

sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
		sum+=x
print(sum)

print(list(range(5)))
#range 提供一个range()函数，可生成一个整数序列
#之后用list()将其转换为list
#如上列，生成从0开始小于5的整数序列

sum=0
for x in range(101):
		sum+=x
print(sum)

sum=0
n=99
while n>0:
		sum+=n
		n-=2
print(sum)
#计算100以内的奇数的和

L=['Bart','Lisa','Adam']

print('---for---')
for x in range(3):
		print(L[x])

print('---while---')
x=0
while x<3:
		print(L[x])
		x+=1

print('---break---')
n=1
while n<=100:
		if n>10:
				break
		print(n)
		n=n+1
print('END')

print('---continue---')
n=0
while n<10:
		n=n+1
		if n%2 == 0: # if n is even, execute CONTINUE
				continue # continue会直接继续下一轮循环，后续的print()不会执行
		print(n)

#ctrl+c可以强制退出程序或强制结束python进程
