from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        linked_list_sum = ListNode(val=0)
        curr_sum_node = linked_list_sum
        carryover = 0

        while l1 or l2 or carryover:
            curr_sum_node.next = ListNode(val=0)
            curr_sum_node = curr_sum_node.next

            node1_value = l1.val if l1 else 0
            l1 = l1.next if l1 else None

            node2_value = l2.val if l2 else 0
            l2 = l2.next if l2 else None

            curr_sum_node.val = (node1_value + node2_value + carryover) % 10

            carryover = 1 if (node1_value + node2_value + carryover) >= 10 else 0

        return linked_list_sum.next
