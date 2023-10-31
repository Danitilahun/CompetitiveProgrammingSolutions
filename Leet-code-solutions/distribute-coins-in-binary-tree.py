# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        res = 0
        
        def postOrder(root: Optional[TreeNode]) -> int:
            nonlocal res
            if root is None:
                return 0
            ans = postOrder(root.left) + postOrder(root.right) + root.val - 1
            res += abs(ans)
            return ans
        
        postOrder(root)
        return res













