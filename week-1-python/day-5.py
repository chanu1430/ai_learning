import math


#  Problem: Reverse a String
s = "hello"
res=""

for i in s:
    # print(i)
    res=i+res

print(res)

# Check if a string is a palindrome.

s="madsam"
l=0
r=len(s)-1

# print()

while l<r:
    if(s[l]==s[r]):
        l+=1
        r-=1
    else:
        break

print(l,r)
if(l==r or l>r):
    print("it is a palindrome")
else:
    print("not a palindrome")
