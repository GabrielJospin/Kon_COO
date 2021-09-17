import Criatura
import Dado


class Pato(Criatura.Criatura):

    def __init__(self, nome, quantidade):
        self.quantidade = quantidade
        ataque = Dado.Dado(10, 1)
        super(Pato, self).__init__(quantidade/3, ataque, 0, 0)
        self.nome = nome

    def falar(self):
        print("%s says: QUACK QUACK QUACK QUACK QUACK" % self.nome)
        # Que foi? Pato não fala meu kssksksk
        print("Algo como 'eu vou te matar seu degraça' ")

    def descreve(self):
        print("O EXERCITO DE %d PATOS DO REI %s ESTA VINDO NA SUA DIREÇÃO" % (self.quantidade, self.nome))
        print("Como todo exercito de patos ele tem vontade e força para vencer um humano em uma luta HONESTA")

    pass
