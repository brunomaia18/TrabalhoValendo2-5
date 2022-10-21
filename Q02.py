def main():
    global n1, n2
    n1=float(input("Digitie um numero: "))
    n2=float(input("Digitie um numero: "))
    print(''' QUAL OPERAÇÃO VOCÊ DESEJA FAZER:
          [1] SOMAR
          [2] SUBTRAIR
          [3] MULTIPLICAR
          [4] DIVIDIR''')
    escolha = int(input("Escolha uma operação: "))
    if escolha == 1 :
        soma()
    elif escolha == 2:
        subtracao()
    elif escolha == 3:
        multiplicacao()
    elif escolha == 4:
        divisao()
    else:
        print('valor invalido')
        main()
    
def soma():
    resultado = n1 + n2
    print(f'{n1} + {n2} = {resultado}')
def subtracao():
    resultado = n1 - n2
    print(f'{n1} - {n2} = {resultado}')
def multiplicacao():
    resultado = n1 * n2
    print(f'{n1} * {n2} = {resultado}')
def divisao():
    resultado = n1 / n2
    print(f'{n1} / {n2} = {resultado}')
    
main()    