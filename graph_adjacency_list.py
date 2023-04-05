# TODO: Sanket SHah, ss4228

# Please see instructions.pdf for the description of this problem.

# An implementation of a weighted, directed graph as an adjacency list. This
# means that it's represented as a map from each node to a list of it's
# respective adjacent nodes.

# import random


class Graph:
    def __init__(self):
        # DO NOT EDIT THIS CONSTRUCTOR
        self.graph = {}

    def add_edge(self, node1, node2, weight):
        """
    :param string node1: key from dict, node label
    :param float weight: edge weight...
    :returns: none

    Adds a directed edge from `node1` to `node2` to the graph with weight defined by `weight`.
    """
        if node1 in self.graph.keys():
          q = False
          for (i,j) in self.graph[node1]:
            if i == node2:
              j = weight
              q = True
              break

          if not q:
            self.graph[node1].append((node2, weight))

        else:
          self.graph[node1] = [(node2, weight)]


    def has_edge(self, node1, node2):
        """
    :param string node1, node2: key node labels from dict
    :returns: bool

    Returns whether the graph contains an edge from `node1` to `node2`.
    DO NOT EDIT THIS METHOD
    """

        if node1 not in self.graph:
            return False
        return node2 in [x for (x, i) in self.graph[node1]]

    def get_neighbors(self, node) -> list:
        """
    :param string node: key label of dict
    :returns: list

    Returns the neighbors of `node` as a list of tuples [(x, y), ...] where
    `x` is the neighbor node, and `y` is the weight of the edge from `node`
    to `x`.
    """
        ls = None
        if node in self.graph.keys():
            ls = self.graph[node]
            for _ in ls:
                for n in range(len(ls) - 1):
                    if ls[n][1] > ls[n + 1][1]:
                        ls[n], ls[n + 1] = ls[n + 1], ls[n]

        return ls or []


# Must uncomment module import above
def rand_graph():
    """
    :returns: dict, ls

    construct psuedo random directed graphs of 26 nodes. returns nodes dict and edges list
    """

    edges = 8
    weights = 20

    e = int(random.normalvariate(edges, 2))
    r = random.randint
    possible_neighbors = [
        [chr(i) for i in range(ord('a'), ord('h') + 1)],
        [chr(i) for i in range(ord('e'), ord('m') + 1)],
        [chr(i) for i in range(ord('k'), ord('s') + 1)],
        [chr(i) for i in range(ord('p'), ord('z') + 1)],
    ]
    dict = {}
    ls = []
    for i in possible_neighbors:
        for j in i:
            p = i.copy()
            for k in range(0, r(3, min(len(i) - 3, e))):
                del (p[r(0, len(p) - 1)])
                p.remove(j) if j in p else None
                n = [(q, r(1, weights)) for q in p]
            dict[f'{j}'] = n
    for i, j in dict.items():
        ls.extend([(i, n, w) for n, w in j])

    return dict, ls




