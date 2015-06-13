__author__ = 'sen'

nums = []
def removeDuplicates(nums):
    i = 0
    while(i+1<=len(nums)-1):
        if nums[i] == nums[i+1]:
            del nums[i+1]
        else:
            i = i+1
    return  len(nums)


print removeDuplicates(nums)
