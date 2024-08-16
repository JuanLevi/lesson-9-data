class TreeNode:
    def __init__(self,v):
       self.value=v
       self.right=None
       self.left=None 
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,root,v):
        if root is None:
            return TreeNode(v)
        if v > root.value:
            root.right=self.insert(root.right,v)
        else:
            root.left=self.insert(root.left,v)
        return root
    
    def search(self,v,root=None):
        if root is None:
            root = self.root
        
        if v == root.value or root is None:
            return root
        elif v > root.value:
            return self.search(v,root.right)
        else:
            return self.search(v,root.left)
        


    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            print(root.value)
            self.inOrder(root.right)
    
    def preOrder(self,root):
        if root:
            print(root.value)
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def postOrder(self,root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.value)




tree=BinarySearchTree()

tree.root=TreeNode(10)

tree.insert(tree.root,5)
tree.insert(tree.root,1)
tree.insert(tree.root,8)
tree.insert(tree.root,17)
tree.insert(tree.root,12)

tree.insert(tree.root,21)


tree.inOrder(tree.root)

i=tree.search(11)

if i:
    print('Key is found')
else:
    print('Key is not found')





