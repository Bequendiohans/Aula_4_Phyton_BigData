#VERIFICADOR DE DESCONTOS
#Sistema de descontos para compras acima de R$250,00
#*Se atentar para usar o "f" no "print" para chamar variáveis atribuidas anteriormente.*

# compra = float(input('Qual o valor da sua compra? '))

# if compra > 250:
#     promocao = compra * 0.16
#     total = compra - promocao
#     print(f'O valor final da sua compra: R${total:.2f}')
# else:
#     print(f'O valor final da sua compra é: R${compra:.2f}')

# ATIVIDADE 2:
# VERIFICAÇÃO AUTOMÁTICA DE LIBERAÇÃO DE UM PEDIDO

estoque = int(input('Informe a quantidade no estoque: '))
requisitado = int(input('Informe a quantidade necessária: '))
peso = int(input('Qual o peso do pedido? '))

if peso <= 50 and requisitado > estoque:
    print('O produto não pode ser enviado')