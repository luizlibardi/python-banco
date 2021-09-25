from typing import List, Dict
from time import sleep

from utils.helper import formata_float_str_moeda
from models.conta import Conta

contas: List[Dict[Conta, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('===========================================')
    print('==============Bem-vindo(a)=================')
    print('===============Belly-Bank==================')
    print('===========================================')

    print('Selecione uma das opções abaixo: ')
    print('1 - Criar uma conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    # elif opcao == 3:
    #     efetuar_deposito()
    # elif opcao == 4:
    #     efetuar_transferencia()
    # elif opcao == 5:
    #     listar_contas()
    # elif opcao == 6:
    #     print('Volte sempre!')
    #     sleep(2)
    #     exit(0)
    else:
        print('Opção Inválida')
        sleep(1)
        menu()

def criar_conta() -> None:
    print('Criar uma Conta')
    print('===============')

    nome: str = input('Nome: ')
    saldo: float = float(input('Saldo: '))
    limite: int = int(input('Limite: '))

    conta: Conta = Conta(nome, saldo, limite)
    contas.append(conta)

    print(f'A conta de {conta.nome} foi criada com sucesso')
    print(f'Código da conta: {conta.codigo} \nSaldo: {conta.saldo} \nLimite: {conta.limite}')
    sleep(2)
    menu()

def efetuar_saque() -> None:
    if len(contas) > 0:
        print('Efetuar Saque')
        print('===============')
        codigo: int = int(input('Qual é o Código da conta? '))
        valor: float = float(input('Qual o valor a sacar?'))

        conta: Conta = pega_conta_por_codigo(codigo)

        conta.set_saldo = (conta.saldo - valor)
        print(conta.saldo)

    #     if conta.codigo == codigo:
    #         for item in contas:
    #             Conta.set_saldo = (conta.saldo - valor)
    #             print(conta.saldo)
    #             # print('Saque efetuado com sucesso!')
    #             # print(f'Saldo atual: {item.saldo}')
    #             # print(f'Saldo atual: {conta.saldo}')

    #             sleep(2)
    #             menu()
    #     else:
    #         print('Codigo da conta não encontrado')
    #         sleep(2)
    #     menu()
    # else:
    #     print('Ainda não existem contas registradas.')
    #     sleep(2)
    #     menu()

# def efetuar_transferencia() -> None:
#     if len(contas) > 1:
#         print('Efetuar Saque')
#         print('===============')
#         codigo1: int = int(input('Insira o ID da conta que irá transferir: '))
#         codigo2: int = int(input('Insira o ID da conta que irá receber a transferência: '))
#         valor: float = float(input('Insira o valor da transferência: '))
        
#         conta1: Conta = pega_conta_por_codigo(codigo1)
#         conta2: Conta = pega_conta_por_codigo(codigo2)
#         print(valor)
#         print(conta1)
#         print(conta2)



#         return f'Transferência completa: \nSaldo de {conta1.nome}: {conta1.saldo} \nSaldo de {conta2.nome}: {conta2.saldo}'
            
#     else:
#         print('É necessário no mínimo duas Contas para utilizar a função de transferência')
#         sleep(2)
#         menu()


def pega_conta_por_codigo(codigo: int) -> Conta:
    c: Conta = None

    for conta in contas:
        if conta.codigo == codigo:
            c = conta
        return c

if __name__ == '__main__':
    main()