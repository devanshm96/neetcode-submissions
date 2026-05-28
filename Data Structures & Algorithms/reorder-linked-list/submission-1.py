# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if not head or not head.next:
        #     return
        # nodes = []
        # curr = head
        # while curr:
        #     nodes.append(curr)
        #     curr = curr.next
        
        # left, right = 0, len(nodes) - 1
        # while left < right:
        #     nodes[left].next = nodes[right]
        #     left += 1
        #     if left == right:
        #         break
        #     nodes[right].next = nodes[left]
        #     right -= 1
        
        # nodes[left].next = None


        if not head or not head.next:
            return

        # STEP 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 'slow' is now at the middle. 
        # We split the list into two halves by grabbing the second half...
        second = slow.next
        # ...and cutting off the first half's tail to prevent cycles.
        slow.next = None 

        # STEP 2: Reverse the second half of the list
        prev = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # 'prev' is now the head of the reversed second half
        second = prev 
        first = head

        # STEP 3: Merge the two halves (alternating)
        while second:
            # Save the next nodes for both halves
            tmp1, tmp2 = first.next, second.next
            
            # Re-wire the pointers to alternate
            first.next = second
            second.next = tmp1
            
            # Move our pointers forward
            first = tmp1
            second = tmp2