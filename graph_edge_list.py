# TODO: sanket shah, ss4228
# Please see instructions.pdf for the description of this problem.

# An implementation of a weighted, directed graph as an edge list. This means
# that it's represented as a list of tuples, with each tuple representing an
# edge in the graph.
class Graph:
    def __init__(self):
        # DO NOT EDIT THIS CONSTRUCTOR
        self.graph = []

    def add_edge(self, node1, node2, weight):
        """
    :param string node1: node labels
    :returns: None

    Adds a directed edge from `node1` to `node2` to the graph with weight
    defined by `weight`.
    """
        for tup in self.graph:
            i, j, k = tup[0], tup[1], tup[2]
            if i == node1 and j == node2:
                del(tup)
                q = True
                break

        self.graph.append((node1, node2, weight))

    def has_edge(self, node1, node2):
        """
    :param string node1, node2: key node labels from dict
    :returns: bool

    Returns whether the graph contains an edge from `node1` to `node2`.
    DO NOT EDIT THIS METHOD
    """
        return (node1, node2) in [(x, y) for (x, y, z) in self.graph]

    def get_neighbors(self, node):
        """
    :param string node: key label of dict
    :returns: list

    Returns the neighbors of `node` as a list of tuples [(x, y), ...] where
    `x` is the neighbor node, and `y` is the weight of the edge from `node`
    to `x`.
    """
        ls = []
        for (i, j, k) in self.graph:
            if i == node:
                ls.append((j, k))

        return ls

