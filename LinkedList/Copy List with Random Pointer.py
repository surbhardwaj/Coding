"""
138. Copy List with Random Pointer

O(N) Time and constant space


"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    
  
    def copyRandomList(self, head):
        if head == None:
            return head
        
        
        curr_node = head
     
        ## Setting the next node
        while(curr_node!=None):
            
            new_node = Node(x=curr_node.val)
            new_node.next = curr_node.next
            curr_node.next = new_node
            curr_node = curr_node.next.next
            
        
        ## Setting the random pointer
        
        curr_node = head
        while(curr_node!=None):
            random = curr_node.random
            if random:
                curr_node.next.random = random.next
            else:
                curr_node.next.random = None
                
            curr_node = curr_node.next.next
            
            
        ## Unweave the lists 
        
        curr_node = head
        start = head.next
        new_head = head.next
        while(curr_node!=None):
            curr_node.next = curr_node.next.next
            start.next = start.next.next if start.next else None
            curr_node = curr_node.next
            start = start.next
            
        return new_head
    
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        






        

