'''
Created on Mar 21, 2019

@author: J
'''

'''
Created on Mar 21, 2019

@author: J
'''

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    @staticmethod
    def findMin(nums):
        
        # empty nums
        if len(nums) == 0:
            return -1
        
        # special loop almost flat
        mid = 0 + (len(nums) - 1)//2
        if nums[0] == nums[-1] == nums[mid]:
            smallest_ele =  nums[0]
            for i in range(len(nums)):
                if smallest_ele > nums[i]:
                    smallest_ele = nums[i]
            return smallest_ele
        
        # special loop start is the smalles
        if nums[0] < nums[-1]:
            return nums[0]
        
        
        # binary search
        # write your code here
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start)//2
            
            if nums[mid] >= nums[start]:
                start = mid
            else:
                end = mid
        
        return nums[end] 

nums = [2,1]
print("The answer is 1. The calculation result is " + str(Solution.findMin(nums)))

nums = [4,4,5,6,7,0,1,2]
print("The answer is 0. The calculation result is " + str(Solution.findMin(nums)))
