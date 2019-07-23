# a= "dlflsdhflhdslfhs"
# print(a[3:])
# print(a[:3:-1])
# print(a[2:6])


a="[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']"
a=a.replace("''",'"')
a=a[2:-2]
b=a.split('" , "')
print(b)
c=[]
for i in b:
    i=int(i[1:])
    c.append(i)
print(c)