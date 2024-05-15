#字符串格式化
# 1.f-string
one = '约儿'
two = '洛伊德'

aaa = f'{one}和{two}'
print(aaa)

# 格式说明  ：
shu = 3.1416926
print(f'{shu:.3f}')     #保留后三位小数

aaa = f'{one:7}和{two}'
print(aaa)
                                #规定字符串长度，不足的用空格填充(字符串在右侧填充，数字在左侧填充)
bbb = f'{age1:6}和{age2}'
print(bbb)

#特殊填充
    #金额
jin = 100000000000
print(f'{jin:,}')
