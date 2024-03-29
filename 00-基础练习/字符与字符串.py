##########################字符类型#######################
"""
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
print (counter)
print (miles)
"""
##########################字符串##########################
'''
Python中的字符串用单引号(')或双引号(")括起来，同时使用反斜杠(\)转义特殊字符。
字符串的截取的语法格式如下：
变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。
加号 (+) 是字符串的连接符， 星号 (*) 表示复制当前字符串，紧跟的数字为复制的次数。
'''
'''
str = 'Hello World!'
print (str)           # 输出完整字符串
print (str[0])        # 输出字符串中的第一个字符
print (str[2:5])      # 输出字符串中第三个至第五个之间的字符串
print (str[2:])       # 输出从第三个字符开始的字符串
print (str * 2)       # 输出字符串两次
print (str + "TEST")  # 输出连接的字符串
'''
###########################反斜杠(\)转义##########################
# Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
'''
print('Ru\noob')
print(r'Ru\noob')
'''

'''
注意：
1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。
'''
