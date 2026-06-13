# Problem: Count Frequency of Elements

nums = [1, 2, 2, 3, 1, 2, 4]
dict={}

for i in nums:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

print(dict)


# Find the element with the highest frequency.
max=0
maxEle=None
for key,value in dict.items():
    if value > max:
        maxEle=key
        max=value

print(f"Element is {maxEle} with fequency {max}")
