#TimeComplexity:O(n)
#SpaceComplexity:O(1)
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this :No
# Implemented iterator using Stack


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.stack = []
        
        self.dfs(root)
        

    def next(self) -> int:
        node = self.stack.pop()
        
        self.dfs(node.right)
        
        return node.val

    def hasNext(self) -> bool:
        if bool(self.stack):
            return True
        else:
            return False
        
    def dfs(self,root):
        
        while(root != None):
            
            self.stack.append(root)
            root = root.left
    
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()