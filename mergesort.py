def mergesort(b):
    n=len(b)
    m=n//2
    if n>1:
        lst=b[:m]
        rst=b[m:]
        mergesort(lst)
        mergesort(rst)
        i=0
        k=0
        j=0
        while i<len(lst) and j<len(rst):
            if lst[i]<rst[j]:
                b[k]=lst[i]
                i=i+1
            else:
                b[k]=rst[j]
                j=j+1
            k=k+1
        while(i<len(lst)):
            b[k]=lst[i]
            k=k+1
            i=i+1
        while(j<len(rst)):
            b[k] =rst[j]
            k = k + 1
            j=j+1


def printarray(b):
    for i in range(0,len(b)):
        print(b[i],end=" ")
    print()



c=[]
a=open('mbox-short.txt','r')
for line in a:
    c.append(int(line))
printarray(c)
mergesort(c)
printarray(c)
