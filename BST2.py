#find the root of the node which is equal to s
def nodeToRootPath(root, s):
    if root == None:
        return None
    if root.data == s:
        l = list()
        l.append(root.data)
        return l

    leftOutput = nodeToRootPath(root.left, s)
    if leftOutput != None:
        leftOutput.append(root.data)
        return leftOutput

    rightOutput = nodeToRootPath(root.right, s)
    if rightOutput != None:
        rightOutput.append(root.data)
        return rightOutput
    else:
        return None

#BST class with all methods
class BST:
    def __int__(self):
        self.root = None
        self.numNodes = 0

    def printTreeHelper(self, root):
        if root is None:
            return
        print(root.data, end=':')
        if root.left is not None:
            print('L', end=':')
            print(root.left.data, end=',')

        if root.right is not None:
            print('R', end=':')
            print(root.right.data, end='')
        print()
        self.printLevelWise(root.left)
        self.printLevelWise(root.right)
    
    def printTree(self):
        self.printTreeHelper(self.root)

    def searchHelper(self, root, data):
        if root == None:
            return False

        if root.data == data:
            return True

        if root.data > data:
            return self.searchHelper(root.left, data)
        else:
            return self.searchHelper(root.right, data)
            
    def search(self, data):
        return self.searchHelper(self.root, data)

    def insertHelper(self, root, data):
        if root == None:
            node = BinaryTreeNode(data)
            return node

        if root.data >= data:
            root.left = self.insertHelper(root.left, data)
            return root
        else:
            root.right = self.insertHelper(root.right, data)
            return root
            
    def insert(self, data):
        self.numNodes += 1
        self.root = self.insertHelper(self.root, data)

    def minu(self, root):
        if root == None:
            return 10000

        if root.left == None:
            return root.data

        return self.min(root.left)
        
    def deleteHelper(self, root, data):
        if root == None:
            return False, None
        if root.data < data:
            deleted, newRightNode = self.deleteHelper(root.right, data)
            root.right = newRightNode
            return deleted, root

        if root.data > data:
            deleted, newLeftNode = self.deleteHelper(root.left, data)
            root.left = newLeftNode
            return deleted, root

        if root.left == None and root.right == None:
            return True, None

        if root.left == None:
            return True, root.right

        if root.right == None:
            return True, root.left

        replacement = self.minu(root.right)
        root.data = replacement
        deleted, newRightNode = seld.deleteHelper(root.right, replacement)
        root.right = newRightNode
        return True, root

    def delete(self, data):
        deleted, newRoot = self.deleteHelper(self.root, data)
        if deleted:
            self.numNodes -= 1
        self.root = newRoot
        return deleted

    def count(self):
        return self.numNodes
