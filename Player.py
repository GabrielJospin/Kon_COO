import Criatura
import Dado


def choicePlayer():
    print("Escolha seu estilo de jogo: ")
    print("1- Guerreiro: \"O Ataque é a melhor defesa\"")
    print("2- Ninja: \"O jeito ninja de ser\"")
    print("3- Escudeiro: \"Um homem sábio, sabe se defender\"")
    print("4- Bruxo: \"Eu sou o mestre dos magos\" (Indisponível nessa versão do jogo)")

    escolha = int(input())

    if escolha == 1:
        return Dado.Dado(20), 50, 60
    elif escolha == 2:
        return Dado.Dado(16), 80, 60
    elif escolha == 3:
        return Dado.Dado(10), 50, 90
    else:
        print("entrada inválida!!")
        return choicePlayer()


class Player(Criatura.Criatura):

    def __init__(self,):
        (ataque, esquiva, escudo) = choicePlayer()
        super(Player, self).__init__(20, ataque, esquiva, escudo)
        print("Escolha seu nome")
        self.nome = input()
        print("Sua Região de origem")
        self.regiao = input()
        print("Seu griro de vitoria")
        self.grito = input()
        print("Olá, %s da região de %s!!!" % (self.nome, self.regiao))

    def gritoDaVitoria(self):
        print(self.grito)

    def update(self):
        print("Você agora tem %d de vida" % self.vida)


    pass
