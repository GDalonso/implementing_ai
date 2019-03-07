import pydot
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class TreePlot:
    # create a plot for the search tree
    def __init__(self):
        # Constructor
        self.graph = pydot.Dot(graph_type="graph", dpi=300)
        self.index = 0

    def createGraph(self, node):
        """ creates pydot graph from search tree,
        similar to the printree() method of nodes
        """

        # create node
        parentGraphNode = pydot.Node(
            str(self.index) + " " + node.state.value, style="filled"
        )
        self.index += 1

        # add node
        self.graph.add_node(parentGraphNode)

        # call this method for child nodes
        for childNode in node.children:
            childGraphNode = self.createGraph(childNode)

            # create edge
            edge = pydot.Edge(parentGraphNode, childGraphNode)

            # add Edge
            self.graph.add_edge(edge)

        return parentGraphNode

    def generateDiagram(self, rootNode, currentNode):
        # generates diagram

        self.createGraph(rootNode, currentNode)

        # show the diagram
        self.graph.write_png("graph.png")
        img = mpimg.imread("graph.png")
        plt.imshow(img)
        plt.axis("off")
        mng = plt.get_current_fig_manager()
        mng.window.state("zoomed")
        plt.show()
