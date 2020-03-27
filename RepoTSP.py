class RepoTSP(object):
    def __init__(self, filename):
        self._filename = filename

    def readFile(self):
        f = open(self._filename, "r")
        graph = {}

        edges = []
        lines = f.readlines()
        n = int(lines[0])
        graph['noCities'] = n
        for i in range(1, n + 1):
            costs = []
            for j in lines[i].split(","):
                costs.append(int(j))
            edges.append(costs)
        graph['edges'] = edges
        return graph
