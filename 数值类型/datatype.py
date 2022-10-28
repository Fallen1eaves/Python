# -*- coding:utf-8 -*-
 
a = 0o101
print("a="+str(a))
 
b=64
print('b='+str(b))
c=-237
print('c='+str(c))
d=0x80
print('d='+str(d))
e=-0x92
print('e='+str(e))

#布尔型测试
print(bool(1))
print(bool(True))
print(bool('0'))
print(bool([]))
print(bool((1,)))

#双精度浮点型
print(0.0)
print(-777.)
print(-5.555567119)
print(96e3 * 1.0)
print(-1.609E-19)

#复数
print(complex(2,4))
print(1.23e-045+6.7e+089j)

#十进制浮点型
##需要先引入decimal模块
print("十进制浮点....")
dec=Decimal('.1')
print(dec)
print(Decimal(.1))
print(dec +Decimal(.1))

#转换工厂
print("转换工厂....")
print(int(4.2222222))
print(float(4))
print(complex(4))

#进制转换
print("进制转换....")
print(hex(255))
print(oct(255))
print(oct(0x111))

#ASII转换
print("进制转换....")
print(chr(76))
print(ord('L'))