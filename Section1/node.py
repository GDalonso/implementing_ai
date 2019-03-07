class Node:
    # represents a node in the search tree
    def __init__(self, state):
        # Constructor
        self.state = state
        self.depth = 0
        self.children = []
        self.parent = None

    def addChild(self, childNone):
        # add a node under another Node
        self.children.append(childNode)
        childNode.parent = self
        childNode.depth = self.depth + 1

    def printTree(self):
        # print the tree
        print(self.depth, " - ", self.state.value)
        for child in self.children:
            child.printTree()
