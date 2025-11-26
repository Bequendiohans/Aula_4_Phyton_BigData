# # #Verificar maioridade
# # idade = int(input('Informe a sua idade: '))
# # if idade >=18:
# #     print('Você é maior de idade')
# # else:
# #     print('Você é menor de idade')

# #Testando mais possibilidades
# #Teste de pontos

# pontos = int(input('Quantos pontos? '))

# if pontos >= 100:
#     print('Nível máximo!')
# elif pontos >=50:
#     print('Na média.')
# else:
#     print('Pontuação baxas')

# VERIFICAÇÃO DE LOGIN

# usuario = input('Informe o usuário: ').lower()
# senha = input('informe a senha: ')

# if usuario == 'admin' and senha == '1234':
#     print('Você está logado!')
# else:
#     print('Ops, login ou senha incorreto!')

#CONDIÇÃO PARA BRINDE

# compra = float(input('Qual o valor da compra: R$ '))
# cliente_frequente = input('Cliente frequente? [S/N]').lower()

# if compra >= 1000 or cliente_frequente == 's':
#     print('Tem direito a brinde!')
# else:
#     print('Sem brinde.')

#CONDIÇÃO PARA APROVAÇÃO. NOTA E FREQUENCIA.

nota = float(input('Informe a nota: '))
frequencia = float(input('informe a frequencia: '))
if nota >= 7:
    if frequencia >= 75:
        print('APROVADO')
    else:
        print('Boa nota, mas reprovado por falta')
else:
    print('Reprovado por nota!')