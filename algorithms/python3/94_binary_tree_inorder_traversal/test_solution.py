from typing import List

from solution import TreeNode, Solution


class TestSolution:
    solution = Solution()

    @staticmethod
    def _create_binary_tree(values: List[int]):
        if not values:
            return None

        root = TreeNode(values[0])
        queue = [root]
        current_node_idx = 1

        while queue:
            parent_node = queue.pop(0)

            left_idx = current_node_idx
            right_idx = current_node_idx + 1
            current_node_idx += 2

            if left_idx < len(values) and (values[left_idx] is not None):
                parent_node.left = TreeNode(values[left_idx])
                queue.append(parent_node.left)

            if right_idx < len(values) and (values[right_idx] is not None):
                parent_node.right = TreeNode(values[right_idx])
                queue.append(parent_node.right)

        return root

    def test_case_1(self):

        nodes = [1, None, 2, 3]
        root = self._create_binary_tree(nodes)

        actual = self.solution.inorderTraversal(root)

        expected = [1, 3, 2]

        assert actual == expected

    def test_case_2(self):

        nodes = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
        root = self._create_binary_tree(nodes)

        actual = self.solution.inorderTraversal(root)

        expected = [4, 2, 6, 5, 7, 1, 3, 9, 8]

        assert actual == expected

    def test_case_3(self):

        nodes = []
        root = self._create_binary_tree(nodes)

        actual = self.solution.inorderTraversal(root)

        expected = []

        assert actual == expected

    def test_case_4(self):

        nodes = [1]
        root = self._create_binary_tree(nodes)

        actual = self.solution.inorderTraversal(root)

        expected = [1]

        assert actual == expected
