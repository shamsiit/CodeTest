class Node:  
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None


def lca_driver(root, n1, n2): 

    if root is None: 
        return None

    if not isinstance(root, Node) or not isinstance(root, Node) or not isinstance(root, Node):
        raise ValueError("Not proper data")    

    if root.key == n1 or root.key == n2: 
        return root  
  
    left_lca = lca_driver(root.left, n1, n2)  
    right_lca = lca_driver(root.right, n1, n2) 
  
    if left_lca and right_lca: 
        return root  

    return left_lca if left_lca is not None else right_lca 

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7)

def lca(node1, node2):
    node = lca_driver(root, node1, node2)
    return node

print( "lca(6,7) = ", lca(6, 7).key) 
print( "lca(3,7) = ", lca(3, 7).key)  

'''
Time complexity of the above solution is O(n) as the method does a simple tree traversal in bottom up fashion.

'''