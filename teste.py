"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
#Nome
n = input('Digite seu nome: ')
#Idade
i = input('Digite sua idade: ')
if n and i :
    print(f'Seu nome eh {n}')
    print(f'Seu nome invertido eh: {n[::-1]}')
    if ' ' in n:
        print('Seu nome contem espaco')
    else:
        print('Seu nome nao contem espaco')
    print(f'Seu nome tem {len(n)} letras')
    print(f'A primeira letra do seu nome eh: {n[0]}')
    print(f'A ultima letra do seu nome eh: {n[-1]}')
    
else :
    print('Desculpe, voce deixou campos vazios')
    
