# Most Frequent Word
text = "ai is great ai is powerful ai"
dict={}
text=text.split(" ")
for i in text:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)

c=0
fw=""
for i in dict:
    if dict[i]>c:
        c=dict[i]
        fw=i
print(fw)