# TODO: Sanket Shah, ss4228

def shortest_path(graph, source, target):
    """
    :param Graph graph: Graph class object
    :param string source: string label
    :param string target: string label


    """
    # `graph` is an object that provides a get_neighbors(node) method that returns
    # a list of (node, weight) edges. both of your graph implementations should be
    # valid inputs. you may assume that the input graph is connected, and that all
    # edges in the graph have positive edge weights.
    #
    # `source` and `target` are both nodes in the input graph. you may assume that
    # at least one path exists from the source node to the target node.
    #
    # this method should return a tuple that looks like
    # ([`source`, ..., `target`], `length`), where the first element is a list of
    # nodes representing the shortest path from the source to the target (in
    # order) and the second element is the length of that path
    #
    # NOTE: Please see instructions.pdf for additional information about the
    # return value of this method.
    node = (source, 0)
    t = Tracker(node)
    while t.queue:
        node = t.dequeue()
        if node[0] == source:
            t.discover(node, node)
        for neighbor in graph.get_neighbors(node[0]):
            t.discover(node, neighbor)
            if target in t.discovered.keys():
                if t.discovered[node[0]]['distance'] > t.discovered[target]['distance']:
                    continue
            if node[0] != target:
                t.enqueue(neighbor)
    if target not in t.discovered.keys():
        return "target not found"
    return t.best_path_to(target)


class Tracker(object):
    """
    tracking object with methods
    """

    def __init__(self, source):
        assert type(source) == tuple
        self.source = source
        self.queue = [source]
        self.discovered = {}
        self.count = len(self.discovered.keys())

    def enqueue(self, node):
        assert type(node) == tuple, "type error"
        if node not in self.queue:
            if node[0] in self.discovered.keys():
                if not self.discovered[node[0]]['traversed']:
                    self.queue.append(node)
            else:
                print('node not in discovered...enqueueing')
                self.queue.append(node)

    def dequeue(self):
        node = self.queue.pop(0)
        self.traverse(node)
        return node

    def traverse(self, node):
        assert type(node) == tuple, "type error"
        node = node[0]
        if node not in self.discovered.keys():
            self.discovered[node] = {
                'traversed': True,
                'parent': node,
                'distance': 0 if node == self.source[0] else float('inf')
            }
        else:
            self.discovered[node]['traversed'] = True

    def discover(self, node, neighbor):
        assert type(neighbor) == tuple, "type error"
        assert type(node) == tuple, "type error"
        node = (node[0], self.discovered[node[0]]['distance']) if self.count else node
        if neighbor[0] not in self.discovered.keys():
            self.discovered[neighbor[0]] = {
                'traversed': False,
                'parent': node[0],
                'distance': 0 if neighbor == self.source else float('inf')
            }

        if (
                neighbor[1]
                + self.discovered[node[0]]['distance']
                < self.discovered[neighbor[0]]['distance']):

            self.discovered[neighbor[0]]['distance'] = (
                    neighbor[1] + self.discovered[node[0]]['distance']
            )
            self.discovered[neighbor[0]]['parent'] = node[0]

    def best_path_to(self, node):
        """
        :param string node: current node for path to
        produces path to node and total distance from the discovered table
        """
        assert type(node) == str, "type error"
        ls = [node]
        if self.discovered[node]['parent'] == node:
            return ls

        def construct_path(node):
            if self.discovered[node]['parent'] == node:
                ls.reverse()
                return
            else:
                ls.append(self.discovered[node]['parent'])
                construct_path(self.discovered[node]['parent'])

        construct_path(node)

        return (ls, self.discovered[node]['distance'])

