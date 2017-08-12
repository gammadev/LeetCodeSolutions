# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        answer = l3 = ListNode(0)
        while l1 != None or l2 != None:
            if l3.next:
                carry = 1
        
            if not l1:
                l3.next = ListNode(l2.val + carry)
                l2 = l2.next
            elif not l2:
                l3.next = ListNode(l1.val + carry)
                l1 = l1.next
            else:
                l3.next = ListNode(l1.val + l2.val + carry)
                l1 = l1.next
                l2 = l2.next
            
            carry = 0
            
            if l3.next.val >= 10:
                l3.next.val = l3.next.val % 10
                l3.next.next = ListNode(1)
            
            l3 = l3.next
            
        return answer.next
        
        
                
        
