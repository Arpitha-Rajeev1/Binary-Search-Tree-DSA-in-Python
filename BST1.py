#search for the element x in BST
def search(root, x):
    if root == None:
        return False
    if root.data == x:
        return True
    elif root.data > x:
        return search(root.left, x)
    else:
        return search(root.right, x)

#construct the BST using sorted array
def constructBST(lst):

    length = len(lst)
    if length == 0:
        return None
    if length == 1:
        return BinaryTreeNode(lst[0])
    new = length - 1
    half = new // 2
    mid = lst[half]
    root = BinaryTreeNode(mid)
    root.left = constructBST(lst[:half])
    root.right = constructBST(lst[half + 1:])

    return root

#print the nodes between k1 and k2 in BST
def printing(root, k1, k2):
    if root == None:
        return
    if root.data > k2:
        printing(root.left, k1, k2)
    elif root.data < k1:
        printing(root.right, k1, k2)
    else:
        print(root.data)
        printing(root.left, k1, k2)
        printing(root.right, k1, k2)

#check if it is BST
def minTree(root):
    if root == None:
        return 100000
    leftMin = minTree(root.left)
    rightMin = minTree(root.right)
    return min(leftMin, rightMin, root.data)

def maxTree(root):
    if root == None:
        return -100000
    leftMax = maxTree(root.left)
    rightMax = maxTree(root.right)
    return max(leftMax, rightMax, root.data)

def isBST(root):
    if root == None:
        return True

    leftMax = maxTree(root.left)
    rightMin = minTree(root.right)

    if root.data > rightMin or root.data <= leftMax:
        return False

    isLeftBST = isBST(root.left)
    isRightBST = isBST(root.right)
    return isLeftBST and isRightBST
#the above method is O(n^2)

#improved solution for check BST
def isBST2(root):
    if root == None:
        return 100000, -100000, True
    leftMin, leftMax, isLeftBST = isBST2(root.left)
    rightMin, rightMax, isRightBST = isBST2(root.right)

    minimum = min(leftMin, rightMin, root.data)
    maximum = max(leftMax, rightMax, root.data)
    isTreeBST = True
    if root.data <= leftMax or root.data > rightMin:
        isTreeBST = False
        
    if not(isLeftBST) or not(isRightBST):
        isTreeBST = False

    return minimum, maximum, isTreeBST

#another solution for check BST
def isBST3(root, min_range, max_range):
    if root == None:
        return True

    if root.data < min_range or root.data > max_range:
        return False

    isLeftWithinConstraints = isBST3(root.left, min_range, root.data - 1)
    isRightWithinConstraints = isBST3(root.right, root.data, max_range)

    return isLeftWithinConstraints and isRightWithinConstraints
    

