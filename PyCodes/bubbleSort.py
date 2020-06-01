file = open("../random.txt")
list = []
for line in file:
    list.append(int(line))

for i in range(0,len(list)-1):
    for j in range(0,len(list)-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(list)
