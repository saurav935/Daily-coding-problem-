

'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

* Also named as Serialize and Deserialize Binary Tree (297) at leetcode
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def preorder(root):
            if not root:
                return "#"
            else:
                mid = [str(root.val)]
                left = preorder(root.left)
                right = preorder(root.right)

                mid.extend(left)
                mid.extend(right)
                return mid

        print(" ".join(preorder(root)))
        return " ".join(preorder(root))

    def deserialize(self, data):
        vals = iter(data.split())
        print(data.split())

        def construct():
            val = next(vals)
            if val == "#":
                return None
            root = TreeNode(int(val))
            root.left = construct()
            root.right = construct()
            return root

        return construct()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
