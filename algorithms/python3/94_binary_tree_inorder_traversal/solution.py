from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        values = []
        visited = {None}
        stack = deque([root])

        while len(stack) > 0:
            current_node = stack.pop()

            if (current_node.left is None) or (id(current_node.left) in visited):
                values.append(current_node.val)
                visited.add(id(current_node))

                if current_node.right:
                    stack.append(current_node.right)

            else:
                stack.append(current_node)
                stack.append(current_node.left)

        return values
