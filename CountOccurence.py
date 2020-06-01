a="indiaismycountry"
dict={}
for i in a:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]=dict[i]+1
for i in dict:
    print(i," ",dict[i])