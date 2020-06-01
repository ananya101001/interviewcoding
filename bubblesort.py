b=[]
# n=int(input('enter how many numbers u need to enter'))
# for i in range(0,n):
#     a.append(int(input()))
a=open('mbox-short.txt','r')
for line in a:
    b.append(int(line))
print(b)
temp=0
for i in range(0,len(b)):
    for j in range(i+1,len(b)):
        if b[i]>b[j]:
            temp=b[i]
            b[i]=b[j]
            b[j]=temp


print(b)