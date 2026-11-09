import random


def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binarySearchInSortedArray(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        elif arr[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1


# Node class
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class RBNode:
    def __init__(self, value, color='red'):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


def insertBST(root, val):
    if not root:
        return BSTNode(val)
    if val < root.val:
        root.left = insertBST(root.left, val)
    elif val > root.val:
        root.right = insertBST(root.right, val)
    return root


def buildRB(sortedArr):
    redLevel = (len(sortedArr) + 1).bit_length() - 1

    def build(left, right, level, parent):
        if left > right:
            return None
        mid = (left + right) // 2
        node = RBNode(sortedArr[mid], 'red' if level == redLevel else 'black')
        node.parent = parent
        node.left = build(left, mid - 1, level + 1, node)
        node.right = build(mid + 1, right, level + 1, node)
        return node

    return build(0, len(sortedArr) - 1, 0, None)


def BSTSearch(root, target):
    curr = root
    if not curr:
        return -1
    if curr.val == target:
        return curr
    elif target < curr.val:
        return BSTSearch(curr.left, target)
    else:
        return BSTSearch(curr.right, target)


def RBTSearch(root, target):
    curr = root
    if not curr:
        return -1
    if curr.value == target:
        return curr
    elif target < curr.value:
        return RBTSearch(curr.left, target)
    else:
        return RBTSearch(curr.right, target)


def genInput(n):
    return random.sample(range(n * 10), n)


if __name__ == '__main__':
    arr = genInput(10)
    sortedArr = sorted(arr)
    bRoot = None
    for i in arr:
        bRoot = insertBST(bRoot, i)
    rRoot = buildRB(sortedArr)
    target = arr[5]
    print('Linear Search:', linearSearch(arr, target))
    print('Binary Search :', binarySearchInSortedArray(sortedArr, target))
    print('Binary Search Tree :', BSTSearch(bRoot, target).val)
    print('Red Black Tree:', RBTSearch(rRoot, target).value)
