class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    result = []
    
    def traverse(node):
        if node is None:
            return
        traverse(node.left)     # Left
        result.append(node.val) # Root
        traverse(node.right)    # Right
    
    traverse(root)
    return result