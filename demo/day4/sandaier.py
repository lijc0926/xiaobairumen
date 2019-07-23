# #给a赋值
# def juge_3_2 (a):
#     print(a)
#     # 第一步：统一符号  对字符串的处理，用replace（）
#     a = (a.replace("''", '"'))
#     #print(a)
#     # 第二步：去掉中括号 字符串截取  [::]
#     a = a[2:-2]
#     #print(a)
#     # 第三步：变成list  字符串切片  .split（） 新建一个list变量
#     b = a.split('" , "')
#     #print(b)
#     # 第四步：取出后面的数字  循环遍历取出list里面的每个值，对这个值进行截取
#     c = {}
#     for i in b:
#         d = (i[1:])
#         #print(d)
#         # 第五步：统计相同的数字个数  用字典去统计
#         if (d in c):
#             c[d] += 1
#         else:
#             c[d] = 1
#     #print(c)
#     # 第六步：判断数据中有没有同时存在三个相同数字和两个相同数字  if判断
#     v1 = 0
#     v2 = 0
#     for i in c:
#         if (c[i] == 3):
#             v1 = 1
#         if (c[i] == 2):
#             v2 = 1
#     if (v1 == 1 and v2 == 1):
#         print("可以三带二")
#     else:
#         print("不可以三代二")
#
# #open 是 python提供的一个内置函数:作用就是打开一个文件.参数一:文件路径;参数二:文件的打开模式 r只读,W可写入,a可读可写
# #with open() as f 类似于 f = open ()他可以在with 的代码执行出问题的时候,做一些资源释放的工作
# with open("D:\\softwareDate\\python\\xiaobairumen\\demo\\day4\\card","r") as f:
# # 读文件.readlines()作用就是把文件中整个内容按行读取出来,存到一个list中;read()把整个文件的内容读取出来,存到一个字符串中
#     lines = f.readlines()
# #for循环遍历这个列表
#     for line in lines:
#         #去掉每一行末尾的换行符
#         line = line.replace("\n","")
#         print(line)
#         juge_3_2(line)
#int()把括号内的字符串转换成数字类型
#str()把括号内的数字转换成字符串类
# def jiafa(a,b):
#     q = a+b
#     print(a,"+",b,"=",q)
#     return q
# # def chengfa(num1,num2):
# #     c=num1
# #     d=num2
# #     w=c*d
# #     print(c,"x",d,"=",w)
# # def jianfa(num1,num2):
# #     e=num1
# #     f=num2
# #     r=e-f
# #     print(e,"-",f,"=",r)
# # def chufa(num1,num2):
# #     g=num1
# #     h=num2
# #     if(h == 0 ):
# #         print("除数不能为0")
# #     else:
# #         t=g/h
# #         print(g,"/",h,"=",t)
# # with open ("D:\\softwareDate\\python\\xiaobairumen\\demo\\day4\\shuzi.txt","r") as f:
# #     num = f.readlines()
# #     for nums in num:
# #         nums = nums.replace("\n","")
# #         nums = nums.split(",")
# #         jiafa(int(nums[0]),int(nums[1]))
# #         chengfa(int(nums[0]),int(nums[1]))
# #         jianfa(int(nums[0]), int(nums[1]))
# #         chufa(int(nums[0]), int(nums[1]))
# jiafa(10,454)
# jiafa(jiafa(10,454),100)
# # chengfa(54257,0)
# # jianfa(25454,45)
# # chufa(8,100)
#
def qianqian(hum1="小花",hum2="小明",money="滚出去",cc=",",ccc="小明打了小芳一巴掌"):
    return "{m1}让{m2}{my}{cc1}{ccc1}".format(m1=hum1,my=money,m2=hum2,ccc1=ccc,cc1=cc)
print(qianqian("小军","小刚","滚出去",".","小刚就出去了"))