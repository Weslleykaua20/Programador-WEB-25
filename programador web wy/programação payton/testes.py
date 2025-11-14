'''
ef multiplicacao(a):
    resultado = a * 2
    return resultado
a = float(input("Digite o número que você que dobrar o valor:"))
total = multiplicacao(a)
print(total)

#_________________________________#

def converter(cm):
    resultado = cm / 100
    return resultado
cm = input("Digite:")
total = converter(cm)
print(total)

'''
# faça uma função que peça o ano de nascimento, o ano atual, e calcule a idade atual do usuário.

def idade(anoat, ano):
    resultado = ano - anoat
    return resultado

anoat = int (input("Digite o ano atual:"))
ano = int (input("Digite o seu ano de nascimento:"))

print(f"Em {anoat}, a sua idade é de {idade()} anos!")