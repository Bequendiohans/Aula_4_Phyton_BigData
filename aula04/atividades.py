# VERIFICADOR DE DESCONTOS
# Sistema de descontos para compras acima de R$250,00
# *Se atentar para usar o "f" no "print" para chamar variáveis atribuidas anteriormente.*

# compra = float(input('Qual o valor da sua compra? '))

# if compra > 250:
#     promocao = compra * 0.16
#     total = compra - promocao
#     print(f'O valor final da sua compra: R${total:.2f}')
# else:
#     print(f'O valor final da sua compra é: R${compra:.2f}')

# ATIVIDADE 2:
# VERIFICAÇÃO AUTOMÁTICA DE LIBERAÇÃO DE UM PEDIDO

# estoque = int(input('Informe a quantidade no estoque: '))
# requisitado = int(input('Informe a quantidade necessária: '))
# peso = int(input('Qual o peso do pedido? '))

# if peso <= 50 and requisitado > estoque:
#     print('O produto não pode ser enviado')

#ATIVIDADE 3:

# filiacao = int(input('Informe seu tempo de serviço: '))
# valor_mov = float(input("Informe o valor movmentdo nos últimos 06 meses: "))

# if filiacao > 3 or valor_mov > 5000:
#     print('Você tem direito ao benefício.')
# else:
#     print('Você não tem direito ao benefício.')


# #ATIVIDADE 4:
# #VALIDAÇÃO DE QUALIDADE DE DADOS:

# valor = int(input('Informe um valor: '))

# if valor < 0:
#     print('Valor INVÁLIDO')
# elif 0 < valor <= 50:
#     print('Valor BAIXO')
# elif valor <= 200:
#     print('Valor ACETÁVEL')    
# else:
#     print('Valor ALTO, verifique os dados.')


#ATIVIDADE 5:
#SISTEMA DE FRETE COM MAIS CATEGORIAS

compra = float(input('Informe o valor total da sua compra em R$: '))

if compra > 500:
    print('Você ganhou frete grátis!')
elif compra >= 300:
    print('')