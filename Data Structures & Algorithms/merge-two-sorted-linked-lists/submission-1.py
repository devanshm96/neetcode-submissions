# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # brute
        # l = []

        # curr1 = list1
        # curr2 = list2
        
        # while curr1 is not None:
        #     l.append(curr1.val)
        #     curr1=curr1.next
        # while curr2 is not None:    
        #     l.append(curr2.val)
        #     curr2=curr2.next
        # l.sort()

        # dummy = ListNode(0)
        # curr = dummy

        # for val in l:
        #     nextnode = ListNode(val)
        #     curr.next = nextnode
        #     curr = curr.next
        
        # return dummy.next
        

        dummy = ListNode(0)
        curr = dummy

        while list1 is not None and list2 is not None:
            if list1.val<list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr=curr.next

        # if any leftover nodes
        if list1 is not None:
            curr.next = list1
        elif list2 is not None:
            curr.next = list2

        return dummy.next


