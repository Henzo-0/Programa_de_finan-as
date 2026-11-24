import defs
import datetime, time

while True:
    defs.titulo("APP DE FINANÇAS")
    # Ler o saldo atual
    try:
        with open('saldo.txt', 'r') as saldo_conta:
            texto = saldo_conta.read().strip()
            valor = defs.conversorFloat(texto) if texto else 0.00
    except FileNotFoundError:
        with open('saldo.txt', 'w') as saldo_conta:
            saldo_conta.write('0')
        valor = 0.00
    print(f"Saldo atual: {valor:.2f}")
    #Opcões do menu
    print('1 - adicionar dinheiro\n2 - remover dinheiro\n3 - historico\n4 - sair')
    resposta = int(input('Digite a opção desejada: '))
    #Adicionar dinheiro
    if resposta == 1:
        print('Adicionar dinheiro')
        print('Digite o valor que deseja adicionar: ')
        dinheiro_adicionado = defs.conversorFloat(input("R$: "))
        descricao_ad = input("Digite a descrição da transação: ")
        with open('historico.txt', 'a', encoding='utf-8') as historico:
            historico.write(f"\033[32mAdicionado [{datetime.datetime.now().strftime('%d/%m/%Y')}][R$: {dinheiro_adicionado:.2f}] - Descrição: {descricao_ad}\033[0m\n")

        with open('saldo.txt', 'w') as saldo_conta:
            valor += dinheiro_adicionado
            saldo_conta.write(f"{valor:.2f}")
    #Remover dinheiro
    elif resposta == 2:
        print("Remover dinheiro")
        print('Digite o valor que deseja remover: ')
        dinheiro_removido = defs.conversorFloat(input("R$: "))
        descricao_re = input("Digite a descrição da transação: ")
        with open('historico.txt', 'a', encoding= 'utf-8') as historico:
            historico.write(f'\033[31mRemovido [{datetime.datetime.now().strftime("%d/%m/%Y")}][R$: {dinheiro_removido:.2f}] - Descrição: {descricao_re}\033[0m\n')

        with open('saldo.txt', 'w') as saldo_conta:
            valor -= dinheiro_removido
            saldo_conta.write(f"{valor:.2f}")
    #Mostrar histórico
    elif resposta == 3:
        print("Historico")
        try:
            with open('historico.txt', 'r', encoding='utf-8') as historico:
                historico_texto = historico.read()
                print(historico_texto)
        except:
            print("Não há histórico de transações.")
        finally:
            time.sleep(2)
    elif resposta == 4:
        print("Sair")
        break