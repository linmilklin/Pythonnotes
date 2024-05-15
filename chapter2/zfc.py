#字符串

one = '缪\
缪'         # \用于字符串没输入完，接入上一行

two = "缪缪"
three = '''缪缪'''
four = """缪缪"""

print(one,two,sep='\n')     #要实现换行输出一般用\n换行

#字符串为不可变数据类型:字符串改变，id改变
print(id(one))
one = '缪尔赛思'
print(id(one))

#字符串的索引，从左往右0 ~ ，从右往左  ~ -1
zy = '劲发江潮落，气收秋毫平'
print(zy[3])
print(zy[-8])

#字符串的切片,
print(zy[:])
print(zy[:5])  #单纯按个数排序
print(zy[6:])  #从第几个后输出

#字符串切片步长
print(zy[::])   
print(zy[::4])  #类似输出后跳过几个后再输出

print(zy[::-1]) #倒过来
print(zy[4:1:-1])   #倒过来后，前面两个的顺序也要从大到小
