age=20
if age >=18:
	  print('your age is',age)
	  print('adult\n')
	  
age=3
if age >=18:
	  print('your age is',age)
	  print('adult')
else:
		print('your age is %d' % age)
		print('teenager\n')
		
age=3
if age >=18:
	  print('adult')
elif age >=6:
		print('teenager')
else:
		print('kid\n')

#if是从上往下判断，如果某个判断结果是True
#把改判断对应的语句执行后，就忽略剩下的elif和else
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
#上例第一条age>=6, 满足，所以不会执行剩下的>=18

x=0
if x:
		print('True')
#x是非零、非空、非空list就被判断为Ture,否则False

s = input('birth: ')
birth = int(s)
if birth<2000:
		print('00前')
else:
		print('00后')
#若输入1982,会报错，因为input返回的是str,要把str转成整数

height = 1.75
weight = 80.5
bmi = weight/(height*height)
print(bmi)

if bmi<18.5:
		print('过轻')
elif bmi<25:
		print('正常')
elif bmi<28:
		print('过重')
elif bmi<32:
		print('肥胖')
else:
		print('严重肥胖')