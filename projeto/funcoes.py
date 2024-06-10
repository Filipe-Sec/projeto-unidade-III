#DICIONÁRIOS E LISTAS USADOS PARA ARMAZENAMENTO DE DADOS
administradores = {}
clientes = {}
filmes = {}
ingressos_vendidos = []

#VALIDA SE O USUÁRIO SEJA ADMINISTRADOR OU O CLIENTE INSERIRAM
def validar_email(email):
    return "@" in email and ".com" in email


#CADASTRO DE USUÁRIO(ADMINISTRADOR E CLIENTE)
def cadastrar_usuario():
    nomeDeUsuario = input("Digite como gostaria de ser chamado: ")
    email = input("Digite o email do usuário: ")
    
    if not validar_email(email):
        print('Email inválido. Tente novamente inserindo um email válido!')
        return
    
    senha = input("Digite a senha do usuário: ")
    tipo = input("Digite o tipo de usuário (ADM ou CLIENTE): ").upper()
    
    usuario = {
        "email": email,
        "senha": senha,
        "nomeDeUsuario": nomeDeUsuario
    }
    
    if tipo == 'ADM':#responsável por verificar se o usuário cadastrado é do tipo ADM, caso seja armazena os dados no respecito dicionário
        administradores[email] = usuario
        print(f"Administrador cadastrado com sucesso!")
    elif tipo == 'CLIENTE':#responsável por verificar se o usuário cadastrado é do tipo CLIENTE, caso seja armazena os dados no respecito dicionário
        clientes[email] = usuario
        print(f"Cliente cadastrado com sucesso")
    else:
        print("Tipo de usuário inválido. Insira 'ADM' ou 'Cliente'.")

#VALIDA O LOGIN USANDO EMAIL E SENHA
def fazer_login(tipoDeUsuario):
    email = input("Digite o email: ")
    
    if not validar_email(email):
        print("Email inválido. O email deve conter '@' e '.com'.")
        return False
    
    senha = input("Digite a senha: ")
    
    if tipoDeUsuario == 'ADM':
        if email in administradores and administradores[email]['senha'] == senha:
            print(f"Login bem-sucedido como Administrador: {administradores[email]['nomeDeUsuario']}")
            return administradores[email]
        else:
            print("Email ou senha inválidos para Administrador.")
            return False
    elif tipoDeUsuario == 'CLIENTE':
        if email in clientes and clientes[email]['senha'] == senha:
            print(f"Login bem-sucedido como Cliente: {clientes[email]['nomeDeUsuario']}")
            return clientes[email]
        else:
            print("Email ou senha inválidos para Cliente.")
            return False

#VERIFICA O TIPO DE USUÁRIO E RETORNA UM BOOLEANO
def verificarTipoDeUsuario(tipoDeUsuario):
    if tipoDeUsuario == 'ADM':
        return bool(administradores)
    elif tipoDeUsuario == 'CLIENTE':
        return bool(clientes)

#CADASTRAMENTO DE NOVOS FILMES(ADMINISTRADOR)
def cadastrar_filme():
        nomeDoFilme = input("Digite o nome do filme: ")
        sala = input("Digite a sala do filme: ")
        horario = input("Digite o horário do filme: ")
        capacidade = int(input("Digite a capacidade da sala: "))
        valor = float(input("Digite o valor do ingresso: "))

        filme = {
                "sala": sala,
                "horario": horario,
                "capacidade": capacidade,
                "valor": valor,
                "ingressos_vendidos": 0
            }
                
        filmes[nomeDoFilme] = filme
        print(f"Filme '{nomeDoFilme}' cadastrado com sucesso.")


#LISTAR FILMES
def listar_filmes():
    if not filmes:
        print("Nenhum filme cadastrado.")
        return
    
    print("\n==========[ LISTA DE FILMES ]==========")
    for filme in filmes:
        print(f"Filme: {filme['nomeDoFilme']}", 
              f"| Sala: {filme['sala']}", 
              f"| Ingressos disponíveis: {filme['ingressos_disponiveis']}", 
              f"| Horário: {filme['horario']}", 
              f"| Preço: R${filme['preco']}", end=' | \n')


#BUSCA O FILME DE ACORDO COM O NOME
def buscar_filme():
    nomeDoFilme = input("Digite o nome do filme a ser buscado: ")
    if nomeDoFilme in filmes:
        print(f"Dados do filme '{nomeDoFilme}': {filmes[nomeDoFilme]}")
    else:
        print("Filme não encontrado.")

#SISTEMA DE OCUPAÇÃO DE SALAS
def sala_ocupada(sala, horario):
    for filme in filmes.values():
        if filme["sala"] == sala and filme["horario"] == horario:
            return True
    return False

#ATUALIZAR DADOS DO FILME
def atualizar_filme():
    nomeDoFilme = input("Digite o nome do filme a ser atualizado: ")
    if nomeDoFilme in filmes:
        print("Dados atuais do filme:")
        print(filmes[nomeDoFilme])
        
        sala = input("Digite a nova sala do filme: ")
        horario = input("Digite o novo horário do filme: ")
        capacidade = input("Digite a nova capacidade da sala: ")
        duracao = input("DIgite a nova duraçãp")
        valor = input("Digite o novo valor do ingresso: ")
        autor = input("")
        
        if sala and horario and sala_ocupada(sala, horario):
            print(f"A sala {sala} já está ocupada no horário {horario}.")
            return
        
        if duracao:
            filmes[nomeDoFilme]["duracao"] = duracao
        if sala:
            filmes[nomeDoFilme]["sala"] = sala
        if horario:
            filmes[nomeDoFilme]["horario"] = horario
        if capacidade:
            filmes[nomeDoFilme]["capacidade"] = int(capacidade)
        if valor:
            filmes[nomeDoFilme]["valor"] = float(valor)
        if autor:
            filmes[nomeDoFilme]["autor"] = autor
        
        print(f"Dados do filme '{nomeDoFilme}' atualizados com sucesso.")
    else:
        print("Filme não encontrado.")

#REMOVER FILME
def remover_filme():
    nomeDoFilme = input("Digite o nome do filme a ser removido: ")
    if nomeDoFilme in filmes:
        del filmes[nomeDoFilme]
        print(f"Filme '{nomeDoFilme}' removido com sucesso.")
    else:
        print("Filme não encontrado.")
        
#LISTA INGRESSOS VENDIDOS
def listar_ingressos_vendidos():
    if ingressos_vendidos:
        for ingresso in ingressos_vendidos:
            print(ingresso)
    else:
        print("Nenhum ingresso vendido.")

#LISTA INGRESSOS VENDIDOS DE UM FILME ESPECÍFICO
def listar_ingressos_vendidos_filme():
    nomeDoFilme = input("Digite o nome do filme: ")
    ingressos_filme = [ingresso for ingresso in ingressos_vendidos if ingresso["nomeDoFilme"] == nomeDoFilme]
    
    if ingressos_filme:
        for ingresso in ingressos_filme:
            print(ingresso)
    else:
        print(f"Nenhum ingresso vendido para o filme '{nomeDoFilme}'.")
        
#COMPRA DE INGRESSOS(CLIENTE)
def comprar_ingresso():
    nomeDoFilme = input("Digite o nome do filme que deseja assistir: ")
    for filme in filmes:
        if filme['nome'] == nomeDoFilme:
            if filme['ingressos_disponiveis'] > 0:
                filme['ingressos_disponiveis'] -= 1
                ingresso = {
                    'cliente': clientes['nome_usuario'],
                    'filme': filme['nome'],
                    'horario': filme['horario'],
                    'preco': filme['preco']
                }
                ingressos_vendidos.append(ingresso)
                print("Ingresso comprado com sucesso!")
                return
            else:
                print("Ingressos esgotados para esse filme.")
                return
    print("Filme não encontrado.")
     
#LISTAGEM DE INGRESSOS DO CLIENTE   
def listar_ingressos_cliente():
    ingressos_cliente = [ingresso for ingresso in ingressos_vendidos if ingresso["cliente"] == ["nomeDeUsuario"]]
    
    if ingressos_cliente:
        for ingresso in ingressos_cliente:
            print(ingresso)
    else:
        print(f"Nenhum ingresso comprado pelo cliente '{['nomeDeUsuario']}'.")
        
#GERAR ARQUIVO .txt COM AS INFORMAÇÕES DOS INGRESSOS
def gerar_arquivo_ingressos():
    ingressos_cliente = [ingresso for ingresso in ingressos_vendidos if ingresso["cliente"] == ["nomeDeUsuario"]]
    
    if ingressos_cliente:
        with open(f'ingressos_{["nomeDeUsuario"]}.txt', 'w') as file:
            for ingresso in ingressos_cliente:
                file.write(f'{ingresso}\n')
        print(f"Arquivo 'ingressos_{['nomeDeUsuario']}.txt' gerado com sucesso.")
    else:
        print(f"Nenhum ingresso comprado pelo cliente '{['nomeDeUsuario']}' para gerar arquivo.")