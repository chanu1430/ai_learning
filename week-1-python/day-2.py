#largest,smallest number in a list
nums = [5, 2, 9, 1, 7]
# nums = [-10, -3, -25, -1]
max=nums[0]
min=nums[0]
for i in range(1,len(nums)):
    if(nums[i]>max):
        max=nums[i]
    if(nums[i]<min):
        min=nums[i]

print(max)
print(min)
    