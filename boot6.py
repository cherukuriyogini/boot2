#Binary tree preorder traversal(144)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # value of the node
        self.left = left      # left child
        self.right = right    # right child
class Solution: 
 
    def preordderTraversal(self,root):
        result=[]

        def preorder(node):
            if not node:
                return 
            result.append(node.val)

            preorder(node.left)

            preorder(node.right)

        preorder(root)


        return result
