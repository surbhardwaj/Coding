"""
LC: 1004 Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        """
        Time complexity: O(N)
        Space complexity: O(1) 
        
        """
        
        N = len(nums)
        if N == 0 :
            return 0
        
        
        start, zero_cnt = 0, 0
        max_len = 0
        
        for end in range(N):
            if nums[end] == 0:
                zero_cnt+=1
            
            if zero_cnt<=k:
                max_len = max(max_len, end-start+1)
            
            while(zero_cnt>k and start<end):
                if nums[start] == 0:
                    zero_cnt-=1
                start+=1
        
      
        return max_len
                
                    
                
            
            
