# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if (root is None):
            return []

        dq = deque([root])
        result = []

        while (dq):
            levelSize = len(dq)

            curLevel = []

            for _ in range(levelSize):
                node = dq.popleft()

                curLevel.append(node.val)

                if (node.left):
                    dq.append(node.left)
                if (node.right):
                    dq.append(node.right)

            result.append(curLevel)

        return result