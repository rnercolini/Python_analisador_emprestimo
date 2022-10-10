# Analisa se um empréstimo será aprovado com base na renda do solicitante.
print('\033[2;31mDigite as informações solicitadas\033[m')
print('\033[32m-=-\033[m' * 20)
valor = float(input('Digite o valor do imóvel: R$ '))
renda = float(input('Digite o valor da renda familiar: R$ '))
tempo = int(input('Digite a quantidade de anos para pagar: '))
mensal = valor / (tempo * 12)
print('\033[32m-=-\033[m' * 20)
print('Valor da prestação: R$ {:.2f}'.format(mensal))
print('Percentual da renda familiar: {:.2f}%'.format((mensal / renda)*100))
if renda * (30/100) > mensal:
    print('\033[35mParabéns, o seu financiamento foi aprovado!\033[m')
else:
    print('\033[37mInfelizmente o seu financiamento não foi aprovado.\033[m')
