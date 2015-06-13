__author__ = 'sen'

nums=[3,2,1,5,6,4]
k = 2

def findKthLargest(nums, k):
    nums.sort()
    return nums[-k]


print findKthLargest(nums,k)
