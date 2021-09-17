import Pato as pt
import Player


def choice():
    print("Escolha oq fará agora? ")
    print("1- ATACAAAAAARRRR")
    print("2- Ta doido, eu vou é fugir")
    print("3- Vou usar meu escudo de defesa")
    return int(input())
    pass


def action(jogador, exerc):
    escolha = choice()
    if escolha == 1:
        print("Você decide atacar, será que tens o que é preciso?")
        jogador.attack(exerc)
        print("Boa, agora o exercito tem %d de vida" % exerc.vida)
        print("Agora é a vez do exercito de patos")
        exerc.falar()
        exerc.attack(jogador)
        print("Você parece ter sofrido um dano, é um exercito e tanto não?")
        jogador.update()
        print("Agora é sua vez!!!")
    elif escolha == 2:
        print("Você decide esquivar, Fugir parece ser uma escolha fácil não é mesmo?")
        jogador.esquivar(exerc.ataque.rolar())
        jogador.update()
        print("Mas eles não desistem e vão atrás de você novamente")
        exerc.falar()
    elif escolha == 3:
        print("Você decide se defender, realmente jamais venceria um exercito de patos")
        jogador.defender(exerc.ataque.rolar())
        jogador.update()
        print("Mas eles não desistem e vão atrás de você novamente")
        exerc.falar()
    else:
        print("Inserção inválida")
        choice()
    pass


print("Eleito melhor jogo pelo festival de Quack")
print("Vencedor do premio com laranja")
print("\"A Jogabilidade e Imersão é incrível\" - New York Time (Sobre The Last Of Us 2)")
print(" \"Foi o jogo mais legal que eu já joguei\" - Minha irmã mais nova")
print(" \"Quando você vai sair do computador e procurar algo útil pra fazer?\" - Minha mãe")
print(" Com vocês .....")
print()
print()
print("DUCK WARRR")
print("O MELHOR JOGO DO MUNDO DOS PATOS")
exercito = pt.Pato("DUCKING", 99)
player = Player.Player()

exercito.descreve()
print("Mas você não é um humano qualquer")
print("Você é %s, a pessoa que irá derrotar o exercito do %s" % (player.nome, exercito.nome))
exercito.falar()

while player.vida > 0 and exercito.vida > 0:
    action(player, exercito)

if player.vida > 0:
    print("Ou não, talvez você só ouvisse o eco dos patos")
    print("PARABENS %s ACABOU DE DERROTAR UM EXERCÍTO" % player.nome)
    print("Você grita: ")
    player.gritoDaVitoria()
    print()
    print("Sempre acreditei em você, obvio")
    print("E o que é isso.. esse brilho")
    print("Dos céus um grande sapo desce a terre, esta é a figura mais aproximada de um Deus")
    print("Deus Frog te nomeia, um Deus entre humanos e você recebe toda a sua glória")
    print("Meus parabéns")
else:
    print("Ninguém disse que seria fácil")
    print("Um exercito de patos!! pra um simples humano!!!")
    print("Até que para um ser claramente inferior você lutou bravamente")
    print("Mas infelizmente isso pouco vale, como uma alma andando por ai")