class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        values = []                                 #to stores the values that needed to be reverse
        nodes = []                                  #to keep track of the nodes
        counter = 0
        curr = head
        
        
        while curr:
            counter += 1
            if counter >= left and counter <= right:
                values.append(curr.val)             #adding the value and nodes in the list
                nodes.append(curr)                          
            curr = curr.next
            
            
        for node in nodes:
            node.val = values.pop(-1)               #for replacing the values of the nodes
        return head

    
    #RESULT: 36ms
    
