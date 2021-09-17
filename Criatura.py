import Dado


class Criatura:

    def __init__(self, vida, ataque, esquiva, escudo):
        self.vida = vida
        self.ataque = ataque
        self.esquiva = esquiva
        self.escudo = escudo

    def isDead(self):
        return self.vida == 0

    def isFriendly(self):
        return self.ataque == 0

    def attack(self, alvo):
        alvo.vida -= self.ataque.rolar()

    def Damage(self, dano):
        self.vida -= dano

    def esquivar(self, dano):

        result = Dado.Dado().rolar()
        if result >= self.esquiva:
            print("hmm a esquiva falhou hihi")
            self.Damage(dano/2)
        else:
            print("Boa fujão, não levou dano")

    def defender(self, dano):
        result = Dado.Dado().rolar()
        if result >= self.escudo:
            print("Seu escudo falhou, agora você terá que lidar com isso")
            self.Damage(dano)
        else:
            print("A defesa funcionou, mas por quanto tempo?")
    pass
