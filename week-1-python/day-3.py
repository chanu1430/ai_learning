s = "hello"
vowels=['a','e','i','o','u']
count=0
for i in s:
    if i.lower() in vowels:
        # count=count+1
        count+=1
print(count)