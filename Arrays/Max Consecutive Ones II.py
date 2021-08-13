"""
LC: 487 (Medium)
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Time complexity : O(N)
        Space : O(1)
        
        """
        
        start, set_index = 0, None
        
        N = len(nums)
        max_ones = 0
        
        for end in range(N):
            if nums[end]==0:
                if set_index == None:
                    set_index = end
                else:
                    max_ones = max(max_ones, end-1-start+1)
                    start = set_index+1
                    set_index = end
                    
        return max(max_ones, end-start+1)
                    
                
