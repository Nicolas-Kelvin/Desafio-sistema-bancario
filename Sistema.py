deposito = 0
saque = 0
saldo = 0
#exibir msg q nao sera possivel sacar por falta de saldo.
op = 0
limite = 500
limite_saque = 3
#Limite de saque diário.
t_sacado = 0

while op != 4:
    print('~' * 26)
    print('     Sistema Bancário')
    print('~' * 26)
    print('''
    [ 1 ] Depositar
    [ 2 ] Sacar
    [ 3 ] Extrato
    [ 4 ] Sair
    ''')
    op = int(input('Digite a operação desejada: '))
    
    if op == 1:
        
        deposito = float(input('Depositar: R$'))
        print('{:.2f}R$ Depositado com sucesso!'.format(deposito))
        deposito = deposito + saldo
    elif op == 2:
        saldo = saldo + deposito
        saque = float(input('Sacar: R$'))
        t_sacado += saque 
        limite_saque -= 1
        if saldo > 0:
            if limite_saque < 0:
                print ('Seu limete de saque diario é 3!')
                t_sacado -= saque 
                limite_saque += 1
            elif saque > limite:
                print('Seu limite de saque é de {}R$'.format(limite))
                t_sacado -= saque  
                limite_saque += 1
                
            elif saque <= limite:
                print('Saque de {:.2f}R$ efetuado com sucesso!'.format(saque))

        else:        
           print('Não sera possivel sacar por falta de saldo!')
    elif op == 3:
        saldo = deposito - t_sacado
        extrato = print('Valor deposito: {:.2f}R$\nValor sacado: {:.2f}R$\nSaldo conta:{:.2f}R$'.format(deposito, t_sacado, saldo))
        #todos os saques devem ser armazenados em na variavel extrato.
    
    elif op == 4:
        print('Finalizando o sistema....')
        
    else: 
       print('Operação inválida, por favor selecione a operação desejada.')
    

