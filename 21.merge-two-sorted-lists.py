#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        temp = ListNode(0,None)
        dummy = temp

        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                dummy.next = ListNode(p1.val)
                p1 = p1.next
                dummy = dummy.next
            else :
                dummy.next = ListNode(p2.val)
                p2 = p2.next
                dummy = dummy.next
        while  p1 is not None:
            dummy.next = ListNode(p1.val)
            p1=p1.next
            dummy = dummy.next
        while p2 is not None:
            dummy.next = ListNode(p2.val)
            p2 = p2.next
            dummy = dummy.next
        return temp.next
            
                
        
# @lc code=end

