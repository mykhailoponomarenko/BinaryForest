# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root, key):
        cur = root
        prev = None

        while cur is not None and cur.val != key:
            prev = cur
            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        if not cur:
            return root
        if not cur.left or not cur.right:
            if cur.left is not None:
                c = cur.left
            else:
                c = cur.right
            if not prev:
                return c
            if cur is prev.left:
                prev.left = c
            else:
                prev.right = c
        else:
            next = cur.right
            next_prev = cur
            while next.left:
                next_prev = next
                next = next.left
            cur.val = next.val
            if next is next_prev.left:
                next_prev.left = next.right
            else:
                next_prev.right = next.right
        return root
