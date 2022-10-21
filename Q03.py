lista =[]
cont = 0
while cont < 5:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua IDade: "))
    lista.append(nome)
    lista.append(idade)
    cont +=1
print(lista)
pergunta = input("Voce quer excluir alguem da lista : S/n").upper()
if pergunta == 'S':
    posiçao = int(input("Qual posiçao da lista voce quer excluir do Nome [0,2,4,6,8]: "))
    del lista[posiçao] 
    print(lista)
    posiçaoidade = int(input("Qual posiçao da idade voce quer excluir : "))
    
    del lista[posiçaoidade]
   
    print(lista)
else:
    print("ok")