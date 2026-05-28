# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # brute
        l = []

        curr1 = list1
        curr2 = list2
        
        while curr1 is not None:
            l.append(curr1.val)
            curr1=curr1.next
        while curr2 is not None:    
            l.append(curr2.val)
            curr2=curr2.next
        l.sort()

        dummy = ListNode(0)
        curr = dummy

        for val in l:
            nextnode = ListNode(val)
            curr.next = nextnode
            curr = curr.next
        
        return dummy.next
