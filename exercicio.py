"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# n = input('Digite um numero')
# try :
#     n = int(n)
#     if n % 2==0 :
#         print(f'{n} par')
#     else :
#         print(f'{n} e impar')
# except :
#     print(f'{n} nao e um numero')

    

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
h = input('Que horas sao?') #h = hora

try :
    h = int(h)
    if h <= 11:
         print('bom dia')
    elif h >= 12 and h <= 17 :
         print('Boa tarde!')
    elif h >= 18 and h <= 23 :
         print('Boa noite!')
    else :
         print('A hora que vc digitou nao existe')
except :
     print('A hora que vc digitou nao existe')
    
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# n = input('Digite seu primeiro nome :') #n = nome do usuario
# tn = len(n)

# if tn >=1 :
#     if tn <= 4 :
#         print('seu nome e curto')
#     elif tn >=5 and tn <= 6 :
#         print('seu nome e normal')
#     elif tn > 6 :
#         print('seu nome e mt grand')
# else :
#     print('Digite algo')
    



    


