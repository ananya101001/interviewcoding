f = open("../Random.txt")

l = []
swp = False
for i in f:
    l.append(int(i))

for i in range(0,len(l)-1):
    swp = False
    for j in range(0,len(l) - i - 1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            swp = True
    if not swp:
        break

print(l)
