#基本数据类型有  4可变数据类型 和 不可变数据类型

a = 1
print(type(a)) #type查看数据类型

print(id(a)) #id查看数据存储地址

b = 1.6984
print(round(b)) #round取整
print(round(b,1)) #取一位小数

#数据类型转换  int()  float()  complex()

int(165.165)
int(float('984.762'))  #int转换字符串时，字符串内不能为浮点数