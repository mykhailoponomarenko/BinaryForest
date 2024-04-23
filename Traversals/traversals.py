def pre_order(node):
    if not node:
        return []
    a = []
    a.extend([node.data])
    a.extend(pre_order(node.left))
    a.extend(pre_order(node.right))
    return a

def in_order(node):
    if not node:
        return []
    a = []
    a.extend(in_order(node.left))
    a.extend([node.data])
    a.extend(in_order(node.right))
    return a

def post_order(node):
    if not node:
        return []
    a = []
    a.extend(post_order(node.left))
    a.extend(post_order(node.right))
    a.extend([node.data])
    return a