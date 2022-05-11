chute = int
numero_secreto = int
tentativas = 0
numeros = [*range(1,101,1)]
chutes = []

print("#" * 32)
print("Bem vindo ao jogo da adivinhação!")
print("#" * 32)
print("Como funciona:")
print("O jogo irá sortear um número inteiro de 1 a 100")
print("Logo você tem que acertar o número")
# START
print("Começar - 1")
print("Sair - 0")
x = int(input("O que deseja? "))
if (x == 1):
    print("")
elif (x == 0):
    exit()
else:
    print("Não entendi a resposta!")
    print("Reinicie o programa e tente novamente")
    exit()

# SORTEIO DO NUMERO SECRETO
import random
import time
numero_secreto = random.randint(1, 100)
print("Sorteando...")
(time.sleep(1))
print("!!!!!Para correção da atividade o número sorteado é: ",numero_secreto,"!!!!!!")

# CHUTE
while chute != numero_secreto:
    print("_" *32)
    chute = int(input("Qual número deseja chutar? "))
    chutes.append(chute)
    if chute > numero_secreto:
        print("O número secreto é menor que ", chute)
        tentativas += 1
    if chute == numero_secreto:
        print("_" * 32)
        print("Parabéns você acertou!")
        tentativas += 1
        print("Seu número de tentativas foi: ", tentativas)
        break
    if chute < numero_secreto:
        print("O número secreto é maior que ", chute)
        tentativas += 1
    if chute not in numeros:
        print("\nQual é?! Você não leu as regras????")
        print("Tente novamente com um número entre 1 e 100!")
        tentativas += 1


    print("Os números que você já tentou são: ")
    print(chutes)

print("\nPara jogar novamente reinicie o jogo")