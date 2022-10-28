# 数值类型

## 标准整型和长整型

整型字面值的表示方法有3种：十进制（常用）、八进制（以数字“0o”开头）和十六进制（以“0x”或“0X”开头）。

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
    print("a="+str(a))

## 布尔型和布尔对象

布尔型数值：True/False，分别对应整数型的1和0

以下对象的布尔值都是False，除此之外是True：

- None
- False（布尔型）
- 0（整型0）
- 0L（长整型0）
- 0.0（浮点型0）
- 0.0+0.0j（复数0）
- ''（空字符串）
- [>]（空列表）
- ()（空元组）
- {}（空字典）
- 用户自定义的 类实例，该类定义了方法 nonzero() 或 len()，并且这些方法返回0或False

## 双精度浮点型

    print(0.0)
    print(-777.)
    print(-5.555567119)
    print(96e3 * 1.0)
    print(-1.609E-19)

## 复数

- 构成：实数+虚数
- 表示虚数的语法：real+imagj.
- 实数部分和虚数部分都是浮点型
- 虚数部分必须有后缀j或J
  
```python
print(complex(2,4))
print(1.23e-045+6.7e+089j)
```

## 十进制浮点型（decimal型）

```python
print("十进制浮点....")
dec=Decimal('.1')
print(dec)
print(Decimal(.1))
print(dec +Decimal(.1))
```

## 转换工厂

函数 int(), long(), float() 和 complex() 用来将其它数值类型转换为相应的数值类型。

```python
print("转换工厂....")
print(int(4.2222222))
print(float(4))
print(complex(4))
```

## 进制转换

python支持支持8进制、10进制和16进制整型，同时还提供了oct()和hex()内建函数来返回8进制和16进制字符串。

```python
#进制转换
print("进制转换....")
print(hex(255))
print(oct(255))
print(oct(0x111))
```

## ASII转换

chr函数和ord函数分别用来将数字转换为字符，和字符转换为数字。

```python
#ASII转换
print("进制转换....")
print(chr(76))
print(ord('L'))
```