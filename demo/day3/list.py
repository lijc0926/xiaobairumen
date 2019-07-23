a = []
#添加单个元素
a.append(0)
b = [2,2,1,3,3,1,3]
# #合并列表1
# print(a+b)
# #合并列表2
# a.extend(b)
# print(a)
# #合并列表3
a +=b
print(a)
# #删除元素1
# del a[0]
# print(a)
#删除元素2
# a.pop(0)
# print(a)
#清空列表1
# a.clear(a)
# print(a)
#清空列表2
# a = []
# print(a)
#更改数据
# a[0]=0
# print(a)



#遍历
for i in a:
    print(i)
#截取某个数据
print(a[0])
#截取部分数据
print(a[1:4])
#倒序
print(a[::-1])
#隔一个取一个
print(a[::2])
#求列表长度
print(len(a))
#成员判断
if( 3 in a):
    print('存在列表中')
else:
    print('不存在列表中')