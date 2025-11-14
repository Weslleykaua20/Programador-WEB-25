

def saudacao(nome):  # para criar uma função, primeiro digitamops "def", depois o nome da função 
                     # e em seguida usamos () - que pode ter ou não variaveis.
                     # Outra nomeclatura para a váriavel é chamado de "parâmetro".
 
    print(f"Eae, {nome}!") # print é o comando que imprime algo no terminal.

saudacao("Weslley") # Aqui está o campo de como ativar/chamar uma função = colocamos o  nome dela
                    # fornecemos o que ela precisa.

def soma(a, b):
    resultado = a + b
    return resultado # Armazena e dá a póssibilidade de utilizar essa variavel fora da função "def".
total = soma(20, 25)
print(total)

# ________________________________________________________________________________________________________________________________

# Adição
def soma(a, b):
    resultado = a + b
    return resultado

# Subtração
def subtracao(a, b):
    resultado = a - b
    return resultado

# Multiplicação
def multiplicacao(a, b):
    resultado = a * b
    return resultado

# Divisão
def divisao(a, b):
    resultado = a / b
    return resultado

# Média
def media(a, b):
    resultado = (a + b) /2
    return resultado



print(soma(20,80))
print( subtracao(20, 80))
print( multiplicacao(20,80))
print( divisao(20,80))
print( media(20,80))

#____________________________________________________________________________________________#

def multiplicacao(a):
    resultado = a * 2
    return resultado
a = float(input("Digite o número que você que dobrar o valor:"))
total = multiplicacao(a)
print(total)

#_________________________________#

def converter(cm):
    resultado = cm / 100
    return resultado
cm = float(input("Digite:"))
total = converter(cm)
print(total)