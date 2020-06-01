a="indiaismycountry"
dict={}
for i in a:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]=dict[i]+1
for i in dict:
    if dict[i]==1:
        print(i)
        break