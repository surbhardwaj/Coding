"""
LC : 485. Max Consecutive Ones
Easy
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        Time complexity : O(N)
        Space Complexity : O(1)
        
        """
        
        
        N = len(nums)
        
        max_ones = 0
        cnt = 0
        for i in range(N):
            if nums[i] == 1:
                cnt+=1
            else:
                max_ones = max(max_ones, cnt)
                cnt = 0
                
    
        
        return max(max_ones, cnt)
    
                
