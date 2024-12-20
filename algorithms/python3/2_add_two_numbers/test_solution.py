from typing import List

from solution import ListNode, Solution


class TestSolution:
    solution = Solution()

    @staticmethod
    def _generate_linked_list(digits: List[int]):
        if not digits:
            return None

        head = ListNode(digits[0])
        current = head

        for num in digits[1:]:
            current.next = ListNode(num)
            current = current.next

        return head

    @staticmethod
    def _validate_solution(actual: ListNode, expected: ListNode):
        actual_node = actual
        expected_node = expected

        while actual_node:
            assert actual_node.val == expected_node.val
            actual_node = actual_node.next
            expected_node = expected_node.next

        assert actual_node is None
        assert expected_node is None

    def test_case_1(self):

        l1 = self._generate_linked_list([2, 4, 3])
        l2 = self._generate_linked_list([5, 6, 4])

        actual = self.solution.addTwoNumbers(l1, l2)

        expected = self._generate_linked_list([7, 0, 8])

        self._validate_solution(actual, expected)

    def test_case_2(self):

        l1 = self._generate_linked_list([0])
        l2 = self._generate_linked_list([0])

        actual = self.solution.addTwoNumbers(l1, l2)

        expected = self._generate_linked_list([0])

        self._validate_solution(actual, expected)

    def test_case_3(self):

        l1 = self._generate_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = self._generate_linked_list([9, 9, 9, 9])

        actual = self.solution.addTwoNumbers(l1, l2)

        expected = self._generate_linked_list([8, 9, 9, 9, 0, 0, 0, 1])

        self._validate_solution(actual, expected)
