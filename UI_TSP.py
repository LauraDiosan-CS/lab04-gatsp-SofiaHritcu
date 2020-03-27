class UI(object):
    def __init__(self, solver):
        self._solver = solver

    def run(self):
        file_name = input("Enter file name: ").strip()
        dimensiune = input("Dimensiunea pop: ").strip()
        dimensiune = int(dimensiune)
        # dimensiune = 200
        numarGeneratii = input("Nr generatii: ").strip()
        numarGeneratii = int(numarGeneratii)
        # numarGeneratii = 100
        self._solver.setSolverParam(file_name, dimensiune, numarGeneratii)
        self._solver.solveGA()
