"""
766. Toeplitz Matrix
Easy

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.


"""

"""
Time complexity: O(M*N)
Space complexity: O(1)

"""


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        """
        
        Input : matrix of size m*n
        output : T/F
        
        
      
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        
        for i in range(m-1):
            for j in range(n-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
                
                
        return True
    
    
    
    
            
