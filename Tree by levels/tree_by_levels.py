def tree_by_levels(node):
    if not node:
        return []
    visited = []
    queue = [node]
    result = []
    while queue:
        v = queue.pop(0)
        if v not in visited:
            visited.append(v)
            result.append(v.value)
            if v.left:
                queue.append(v.left)
            if v.right:
                queue.append(v.right)
    return result