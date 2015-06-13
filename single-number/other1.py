__author__ = 'sen'

nums = [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6,16,999]

def singleNumber(nums):
    nums.sort()
    numslen = len(nums)
    i = 0
    res = 0
    while(i<=numslen-1):
        res = res^nums[i]
        if res != 0:
            return res
        i = i+1
    return res

print singleNumber(nums)
