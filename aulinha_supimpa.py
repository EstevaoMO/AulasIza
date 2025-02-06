""" # Tipos de variável

var1 = 'olá' #string
var2 = 20 #int
var3 = 19.8 #float
var4 = True #boolean
var5 = False #boolean

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))

# Declaração de variáveis

# 1var = 3 (não funciona: número no começo)
# *var = 1 (não funciona: caractere especial, exceto _)

CONST = 123 # isso é uma constante, não se altera

# Operações

# Aritiméticas
adicao = 2+3
subtracao = 2-3
multiplicacao = 2*3
divisao = 2/2
potencia = 2**2
modulo = 2%2

# Recursão supimpa
adicao += 1
subtracao -= 1
multiplicacao *= 2
divisao /= 1
potencia **= 2
modulo %= 1

# Lógicos

# var4 = True
# var5 = False

# and
# or
# not

num_1 = 10
num_2 = 9

print(var4 and var5) #retorna False
print(num_1 == 10 and num_2 == 8) # retorna False
print(num_1 == 7 or num_2 == 8) # retorna True
print(not False) # retorna True
print(not True) # retorna False

# Comparação

# >
# <
# >=
# <=
# ==
# !=

print(8 > 9) # retorna False
print(8 < 9) # retorna True
print(10 >= 10) # retorna True
print(9 <= 10) # retorna True
print(7 == 6) # retorna False
print(7 != 9) # retorna True

print(8 < 9 and 7 != 9) # retorna True
 """

# If - Estrutura de Condição

numero = 7

if numero < 10:
    print("O número é menor do que 10")
else:
    print("o número não é menor do que 10")

texto_usuario = input('Insira aqui um texto: ')

print(texto_usuario)

# Exercício

"""
Faça um código em que o usuário insira um texto
Se o texto for 'oi', imprima 'olá, moço' no terminal
Caso contrário, imprima o texto que o usuário inseriu
"""

# Izabelly Fagundes - Resposta

texto_usuario = input("Insira aqui um texto")
if texto_usuario == "oi":
    print ("ola, moco")
else:
    print (texto_usuario)

"""
Faça um código em que o usuário
insira dois números (duas variáveis distintas)
Logo após, o resultado da soma será impresso no terminal
"""

var1_usuario = int(input ("Insira aqui um número: "))
var2_usuario = int(input ("Insira aqui outro número: "))
print (var1_usuario + var2_usuario)

"""
Faça um código em que o usuário vá inserir
Dois valores distintos e o código irá imprimir
Qual dos dois é o maior

Ex.:
primeiro número: 2
segundo número: 3

terminal: 2 é o maior número
"""

var1_usuario = int(input ("Insira aqui um número:"))
var2_usuario = int(input ("Insira aqui outro número:"))

if var1_usuario > var2_usuario:
    print (var1_usuario, "é o maior número")
else:
    print (var2_usuario, "é o maior número")

"""
Faça um código em que o usuário insira um valor
Se o valor for positivo, imprima 'é positivo'
Se o valor for negativo, imprima 'é negativo'
Se o valor for igual a zero, imprima 'é zero'
"""

input_usuario = int(input("Insira um valor: "))

if input_usuario > 0:
    print('é positivo')
if input_usuario < 0:
    print('é negativo')
if input_usuario == 0:
    print('é zero')

"""
Para casa:

Faça um código em que o usuário diga o valor
do raio de um círculo e seja impresso o valor da área

Arredonde pi para 3

Ex.:

valor: 2
terminal: a área é 12
"""

raio = float(input("Digite o valor do raio aí, meu parça:"))

pi = 3

area = pi* (raio**2)

print (f"A area do círculo é: {area:.2f}")

x = 5

# Elif - Estrutura de Condição

if x > 2:
    print('qualquer coisa')
elif x >  3:
    print('outra coisa')
elif x > 4:
    print('ultima coisa')

"""
Faça um código em que o usuário
Diga a nota (inteira) que ele tirou numa prova
Se a nota for maior ou igual a 7, ele passou
Se a nota for maior ou igual a 5, ele está de recuperação
Caso nenhuma dessas opções seja o caso, ele reprovou
"""

nota = int(input("Digite a nota que você tirou na prova: "))

if nota >= 7:
    print ("Parabéns! Você passou.")
elif nota >= 5:
    print ("Que pena. Ainda dá pra se salvar, você está de recuperação.")
else:
    print ("Infelizmente, a casa caiu! Você está reprovado.")

# While - Estrutura de Repetição
x = 2

while x <= 4:
    print(f"O valor de x é {x}")
    x += 1

print(f"O último valor de x é {x}")

"""
Faça um código em que o usuário diga seu nome,
Enquanto o nome digitado não for "Iza", o usuário
Terá que digitar outro nome
"""

""" Sem else: o último print não está relacionado à condição do else """

nome = (input("Diga seu nome:"))
while nome != "Iza":
    print ("errou!")
    nome = input ("nome incorreto, tente de novo:")
print ("Correto! Bem-vinda, Iza!")

""" Com else: o último print não está relacionado à condição do else """

nome = (input("Diga seu nome:"))
while nome != "Iza":
    print ("errou!")
    nome = input ("nome incorreto, tente de novo:")
else:
    print ("Correto! Bem-vinda, Iza!")


""" Exemplo joguinho simples para o break """

vida_jogador = 100
vida_monstro = 50

while True:
    print(f"Você: {vida_jogador}HP")
    print(f"Monstro: {vida_monstro}HP")

    ataque = int(input('Diga que você quer atacar teclando 1, caso não 2: '))

    if ataque == 1:
        vida_monstro -= 10
    elif ataque == 2:
        vida_jogador -= 10

    if vida_jogador <= 0:
        print("Você morreu! Tadinho, todo xoxo...")
        break
    if vida_monstro <= 0:
        print("Você venceu, garanhão! Parabéns!")
        break

"""
Faça um código em que o usuário diga uma senha
Caso essa senha não seja "1234", dizer que a
Senha está errada e pedir para o usuário tentar de novo
No entanto, caso a senha seja "5678", deixá-lo entrar como moderador
"""

while True:
    senha = input("Digite a senha:")

    if senha == "1234":
        print ("Acesso permitido.")
        break
    elif senha == "5678":
        print ("Acesso permitido como moderador.")
        break
    else:
        print ("Senha incorreta. Tente novamente.")