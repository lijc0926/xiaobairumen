#创建字典
a = {}

##字典中key是唯一的不可改变的
#列表不能当key，元组中有列表时不能当key，字符串，数字，可以为key
#新增数据
a['姓名']='李井琛'
a['性别']='男'
print(a)
#修改数据
a['姓名']='狗蛋'
print(a)
#删除某一对值，pop
# a.pop('姓名')
# print(a)
#查key的value
print(a['姓名'])
for key in a:
    print(a[key])
#把一个字典合并到另外一个字典
# b={'姓名':'小花'}
# c={'性别':'男人'}
# b.update(c)
# print(b)
# #两个字点合并成一个新的字典
# print(dict(b,**c))
# print(c)
# #成员判断，只支持key
# if '姓名' in b:
#     print('存在字典之中')
# #获取字典长度
# print(len(b))