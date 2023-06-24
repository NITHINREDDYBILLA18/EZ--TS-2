class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

def insert(root, key):
    if root is None:
        return Node(key)
    elif key < root.val:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


r = None

r = insert(r, 100)
r = insert(r, 70)
r = insert(r, 50)
r = insert(r, 60)
r = insert(r, 9)
r = insert(r, -3)
#r = insert(r, 80)

# Print the tree using inorder traversal
print("Inorder traversal:")
inorder(r)
print()


