# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #while both are not equal to null
        # 1 4 5
        # 2 3 6

        #merge list 2 into list 1
        # if curr1.val < curr2.val
        dummy = ListNode()
        tail = dummy
        l1 = list1
        l2 = list2


        while l1 and l2:
            tmpL1 = l1.next
            tmpL2 = l2.next

            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2



        return dummy.next
        