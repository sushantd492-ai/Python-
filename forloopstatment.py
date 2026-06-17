for i in range (1,5):
 for j in range (4,1,-1):
     print(i,end=" ")
print()





for i in range (4,0,-1):
 for J in range (1,0,-1):
   print("*",end=" ")
 print()






for i in range(4, 0, -1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()  










num=65
for i in range (1,5):
    for j in range(i):
        print(chr(num),end=" ")
        num+=1
    print()    








ch='a'
for i in range (1,5):
    print(ch*i)
    ch=chr(ord(ch)+1)





n=5 
for i in range (1,n+1):
    for k in range (n-1):
        print(" ",end=" ")
    for j in range (i):
        print("*")
    print()



d={'name':'sushant','id':'sid1212121111211'}
print(d)
d['phoneno']="2222202020"
print(d)
del d['name']
print(d)
del d
print(d)



d1=dict(a='one',b='two')
print(d1)