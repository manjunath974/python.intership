class Node:
    def __init__(self,key):
        self.left=None
        self.rigth=None
        self.value=key

class BinaryTree:
    def __init__(self,root_value):
        self.root=Node(root_value)

    def insert(self,current_node,value):
        if value<current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self.insert(current_node.left,value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            self.insert(current_node.right,value)

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.value,end=" ")
            
            self.preorder(node.right)
    def preorder(self,node):
        if node:
            print(node.value,end=" ")
            self.preorder(node.left)
            self.preorder(node.rigth)
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.rigth)
            print(node.value,end=" ")

tree = BinaryTree(5)
tree.insert(tree.root,8)
tree.insert(tree.root,4)
tree.insert(tree.root,9)
tree.insert(tree.root,6)
print("In-order traversal:")
tree.inorder(tree.root)
print("\nPre-order traversal:")
tree.preorder(tree.root)
print("\nPost-order traversal:")
tree.postorder(tree.root)








            
