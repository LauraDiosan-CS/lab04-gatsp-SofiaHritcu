import random


def generateARandomPermutation(n):
    perm = [i for i in range(n)]
    pos1 = random.randint(0, n - 1)
    pos2 = random.randint(0, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm


# permutation-based representation
class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam  # problParam has to store the number of nodes/cities
        self.__repres = generateARandomPermutation(self.__problParam['noDim'])
        pos = len(self.__repres) + 1
        for i in range(len(self.__repres)):
            if self.__repres[i] == 0:
                pos = i
        self.__repres[0], self.__repres[pos] = self.__repres[pos], self.__repres[0]
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        # order XO
        pos1 = random.randint(-1, self.__problParam['noDim'] - 1)
        pos2 = random.randint(-1, self.__problParam['noDim'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        k = 0
        newrepres = self.__repres[pos1: pos2]
        for el in c.__repres[pos2:] + c.__repres[:pos2]:
            if el not in newrepres:
                if len(newrepres) < self.__problParam['noDim'] - pos1:
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1
        pos = len(newrepres) + 1
        for i in range(len(newrepres)):
            if newrepres[i] == 0:
                pos = i
        newrepres[0], newrepres[pos] = newrepres[pos], newrepres[0]
        offspring = Chromosome(self.__problParam)
        offspring.repres = newrepres
        return offspring

    def mutation(self):
        # insert mutation
        pos1 = random.randint(1, self.__problParam['noDim'] - 1)
        pos2 = random.randint(1, self.__problParam['noDim'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        el = self.__repres[pos2]
        del self.__repres[pos2]
        self.__repres.insert(pos1 + 1, el)
        pos = len(self.__repres) + 1
        for i in range(len(self.__repres)):
            if self.__repres[i] == 0:
                pos = i
        self.__repres[0], self.__repres[pos] = self.__repres[pos], self.__repres[0]

    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
