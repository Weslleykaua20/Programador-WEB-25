


#Descobrir a áreas de um circulo com o valor do raio
def circulo(raio):
    pi = 3.1415926
    area = pi * (raio**2)
    return area

x = int(input())
print("digite o valor do raio para calcularmos o valor da área do circulo" + circulo(x))
'''
'''
#aplicar um desconto
def aplicar_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    return preco_final

print(aplicar_desconto(80, 10))
'''

'''
#converter o valor de celsius para fahrenheit
def temperatura(celsius):
    fahrenheit = (celsius * 9 / 5) + 32 
    return fahrenheit

celsius = int(input("Digite a sua temperatura em graus celsius para convertermos a Fahenheit:"))
print(f"A temperatura em Fahenhait é de: {temperatura(celsius)} F°")
'''

'''
#converter o valor de fahrenheit para celsius
def temperatura(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit = float(input("Digite a sua temperatura em fahrenheit para convertermos a graus Celsius:"))
print(f"A temperatura em Celsius é de: {temperatura(fahrenheit)} C°")
'''