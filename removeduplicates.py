a=[12,56,34,89,23,45,12,89,34]
for i in a:
    print(i,end=" ")

print()
b=[]
for i in a:
    if i in b:
        continue
    else:
        b.append(i)

for i in b:
    print(i,end=" ")
print()