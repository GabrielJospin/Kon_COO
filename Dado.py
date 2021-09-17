from random import Random as rand


class Dado:

    def __init__(self, lados=100, roladas=1):
        self.lados = lados
        self.roladas = roladas

    def rolar(self):
        total = 0
        random = rand()
        for i in range(self.roladas):
            total += random.randint(1, self.lados)

        return total

    pass
