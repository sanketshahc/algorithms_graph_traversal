# Sanket Shah ss4228
# This is a helper module to generate test graphs
import random

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

