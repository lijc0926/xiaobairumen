# for i in range(2,100):
#    n = 2
#    for j in range(2,i+1):
#        if (i%n == 0):
#            break
#        n = n+1
#    if(n==i):
#        print(i)



a = 'http://qa.yansl.com/#/login'
xieyi = a.split('://')[0]
a = a.split('://')[1]
yuming = a[:a.find('/')]
uri = a[a.find('/'):]
print(xieyi,yuming,uri)
# print(yuming)
# print(uri)
d={}
d['协议']=xieyi
d['ip']=yuming
d['uri']=uri
print(d)