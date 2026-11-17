class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def pre_order(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.val)
        pre_order(root.left, result)
        pre_order(root.right, result)
    return result

def in_order(root, result=None):
    if result is None:
        result = []
    if root:
        in_order(root.left, result)
        result.append(root.val)
        in_order(root.right, result)
    return result

def post_order(root, result=None):
    if result is None:
        result = []
    if root:
        post_order(root.left, result)
        post_order(root.right, result)
        result.append(root.val)
    return result

def level_order(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        current = queue.pop(0)
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

if __name__ == "__main__":
    # Constructing a sample binary tree based on your project structure:
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("--- Binary Tree Traversals ---")
    print("Pre-order traversal:", pre_order(root))
    print("In-order traversal:", in_order(root))
    print("Post-order traversal:", post_order(root))
    print("Level-order traversal:", level_order(root)) 