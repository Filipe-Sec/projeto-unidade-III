from funcoes import *

#VERIFICA O TIPO DE USUÁRIO E RETORNA UM BOOLEANO
def verificar_usuarios(tipoDeUsuario):
    if tipoDeUsuario == 'ADM':
        return bool(administradores)
    elif tipoDeUsuario == 'CLIENTE':
        return bool(clientes)

def menu_administrador():
    while True:
        print('='*10 + "[ MENU DO ADMINISTRADOR ]" + '='*10)
        print("(1) Cadastrar filme \n(2) Buscar filme \n(3) Atualizar dados do filme \n(4) Remover filme \n(5) Listar todos os ingressos vendidos \n(6) Listar ingressos vendidos para um filme \n(7) Voltar ao menu principal")
        opcaoMenuAdministrador = input("Escolha uma opção: ")

        if opcaoMenuAdministrador == '1':
            cadastrar_filme()
        elif opcaoMenuAdministrador == '2':
            buscar_filme()
        elif opcaoMenuAdministrador == '3':
            atualizar_filme()
        elif opcaoMenuAdministrador == '4':
            remover_filme()
        elif opcaoMenuAdministrador == '5':
            listar_ingressos_vendidos()
        elif opcaoMenuAdministrador == '6':
            listar_ingressos_vendidos_filme()
        elif opcaoMenuAdministrador == '7':
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def menu_cliente():
    while True:
        print("\n==========[ MENU CLIENTE ]==========")
        print("(1) Comprar ingresso")
        print("(2) Listar meus ingressos")
        print("(3) Gerar arquivo de ingressos")
        print("(4) Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            comprar_ingresso()
        elif opcao == '2':
            listar_ingressos_cliente()
        elif opcao == '3':
            gerar_arquivo_ingressos()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_principal():
    while True:
        print('='*10 + "[ MENU PRINCIPAL ]" + '='*10)
        print("(1) Gerenciar filmes (ADM) \n(2) Comprar ingressos (Cliente) \n(3) Cadastrar usuário (ADM ou Cliente) \n(4) Sair")
        opcaoMenuInicial = input("Escolha uma opção: ")
        
        if opcaoMenuInicial == '1':
            if verificar_usuarios('ADM'):
                adm = fazer_login('ADM')
                if adm:
                    menu_administrador()
            else:
                print("Nenhum administrador cadastrado. Por favor, cadastre um administrador primeiro.")
                cadastrar_usuario()
            
        elif opcaoMenuInicial == '2':
            if verificar_usuarios('CLIENTE'):
                cliente = fazer_login('CLIENTE')
                if cliente:
                    menu_cliente()
            else:
                print("Nenhum cliente cadastrado. Por favor, cadastre um cliente primeiro.")
                cadastrar_usuario()
        elif opcaoMenuInicial == '3':
            cadastrar_usuario()
        elif opcaoMenuInicial == '4':
            print("[SISTEMA ENCERRADO]")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()