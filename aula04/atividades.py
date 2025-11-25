#Verificador de descontos
#Sistema de descontos para compras acima de R$250,00
# Se atentar para usar o "f" no "print" para chamar variáveis atribuidas anteriormente.

compra = float(input('Qual o valor da sua compra? '))

if compra > 250:
    promocao = compra * 0.16
    total = compra - promocao
    print(f'O valor final da sua compra: R${total:.2f}')
else:
    print(f'O valor final da sua compra é: R${compra:.2f}')

