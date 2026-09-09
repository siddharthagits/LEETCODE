# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        q=[(root,targetSum,[])]
        res=[]
        while q:
            node,remSum,path=q.pop(0)
            remSum=remSum-node.val
            path.append(node.val)
            if not node.left and not node.right and remSum==0:
                res.append(path)
            if node.left:
                q.append((node.left,remSum,path[:]))
            if node.right:
                q.append((node.right,remSum,path[:]))
        return res