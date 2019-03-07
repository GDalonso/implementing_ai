from state import State
from node import Node


class RecursiveDFS:
    # perform DFS search

    def search(self):
        # perform the search

        # get the initial State
        initialState = State()

        # crate root node
        rootNode = Node(initialState)

        # perform search from root node
        self.DFS(rootNode)

        rootNode.printTree()

    def DFS(self, node):
        # creates the search tree

        print(" -- proc -- ", node.state.path)

        # chack if we reached the goal State
        if node.state.checkGoalState():
            print("Reached goal state")
            return True

        else:
            # find the sucessor states from current states
            childStates = node, state.sucessorFunction()

            # add these states as children nodes of current node
            for childState in childStates:
                childNode = Node(State(childState))
                node.addChild(childNode)

                result = self.DFS(childNode)
                if result:
                    return True
            return False
