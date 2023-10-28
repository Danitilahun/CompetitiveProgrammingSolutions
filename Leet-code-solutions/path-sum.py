# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        prefix_sum = 0

        def helper(root, ans):
            nonlocal prefix_sum
            if not root:
                return 

            if not root.left and not root.right:
                prefix_sum += root.val 
                ans.append(root.val)
                if prefix_sum - targetSum  == 0:
                    return True
                prefix_sum -= root.val
                ans.pop()
                return False

            prefix_sum += root.val 
            ans.append(root.val)
            
            left = helper(root.left , ans)
            if left : return left
            right = helper(root.right, ans)
            if right: return right
            prefix_sum -= root.val
            ans.pop()
            return False
        answer = helper(root ,[])
        return answer
            