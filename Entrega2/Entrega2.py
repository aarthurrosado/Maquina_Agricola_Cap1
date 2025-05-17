import oracledb
from datetime import datetime
import os

# Código para inserção Manual e Manipulação CRUD dos dados
# Criando conexão
try:
    # Efetua a conexão com o Usuário no servidor
    conn = oracledb.connect(user='RM563145', password="260399", dsn='oracle.fiap.com.br:1521/ORCL')
    cursor = conn.cursor()

    # Cria as instruções para cada opção
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_alteracao = conn.cursor()
    inst_exclusao = conn.cursor()

except Exception as e:
    # Informa o erro
    print("Erro: ", e)
    conexao = False
else:
    # Flag para executar
    conexao = True

#--------------------------------------------------------------------------------------------------------------

# Funções de inserção

# PH
def inserir_sensor_ph(PH_registrado, status_sensor, loc_sensor):
    data_hora = datetime.now()
    cursor.execute("""
        INSERT INTO SENSOR_PH (
           PH_registrado, data_hora, status_sensor, loc_sensor
        )
        VALUES (:1, :2, :3, :4)
    """, (PH_registrado, data_hora, status_sensor, loc_sensor))
    conn.commit()

# Fósforo
def inserir_sensor_fosforo(Fosforo_registrado, status_sensor, loc_sensor):
    data_hora = datetime.now()
    cursor.execute("""
        INSERT INTO SENSOR_Fosforo (
           Fosforo_registrado, data_hora, status_sensor, loc_sensor
        )
        VALUES (:1, :2, :3, :4)
    """, (Fosforo_registrado, data_hora, status_sensor, loc_sensor))
    conn.commit() 

# Potássio
def inserir_sensor_potassio(Potassio_registrado, status_sensor, loc_sensor):
    data_hora = datetime.now()
    cursor.execute("""
        INSERT INTO SENSOR_Potassio (
           Potassio_registrado, data_hora, status_sensor, loc_sensor
        )
        VALUES (:1, :2, :3, :4)
    """, (Potassio_registrado, data_hora, status_sensor, loc_sensor))
    conn.commit() 


# Funções de consulta

def consultar_sensores_ph():
    cursor.execute("SELECT * FROM SENSOR_PH")
    for linha in cursor.fetchall():
        print(linha)

def consultar_sensores_fosforo():
    cursor.execute("SELECT * FROM SENSOR_Fosforo")
    for linha in cursor.fetchall():
        print(linha)

def consultar_sensores_fosforo():
    cursor.execute("SELECT * FROM SENSOR_Potassio")
    for linha in cursor.fetchall():
        print(linha)

# Funções de atualização

def atualizar_ph(id_senso_PH, novo_valor_PH):
    cursor.execute("""
        UPDATE SENSOR_PH
        SET PH_registrado = :1
        WHERE id_senso_PH = :2
    """, (novo_valor_PH, id_senso_PH))
    conn.commit()

def atualizar_fosforo( id_sensor_Fosforo, novo_valor_fosforo):
    cursor.execute("""
        UPDATE SENSOR_Fosforo
        Fosforo_registrado = :1
        WHERE id_sensor_Fosforo = :2
    """, (novo_valor_fosforo,   id_sensor_Fosforo))
    conn.commit()

def atualizar_potassio( id_sensor_Potassio, novo_valor_potassio):
    cursor.execute("""
        UPDATE SENSOR_Potassio
        Fosforo_registrado = :1
        WHERE id_sensor_Potassio = :2
    """, (novo_valor_potassio,   id_sensor_Potassio))
    conn.commit()

def remover_sensor_ph(id_senso_PH):
    cursor.execute("DELETE FROM SENSOR_PH WHERE id_senso_PH = :1", (id_senso_PH,))
    conn.commit()


# Funções de exclusão

def remover_sensor_ph(id_senso_PH):
    cursor.execute("DELETE FROM SENSOR_PH WHERE id_senso_PH = :1", (id_senso_PH,))
    conn.commit()

def remover_sensor_fosforo(id_sensor_Fosforo):
    cursor.execute("DELETE FROM SENSOR_Fosforo WHERE id_sensor_Fosforo = :1", (id_sensor_Fosforo,))
    conn.commit()

def remover_sensor_potassioo(id_sensor_Potassio):
    cursor.execute("DELETE FROM SENSOR_Potassio WHERE id_sensor_Potassio = :1", (id_sensor_Potassio,))
    conn.commit()


#------------------------------------------------------------------------------------------------------------

while conexao:
    os.system('cls')

    # Menu
    print("------- Dados Sensores -------")
    print("""
    1 - Inserir Dados
    2 - Consultar Dados
    3 - Alterar Dados
    4 - Excluir Dados
    6 - SAIR
    """)

    # Pegar input
    escolha = input("Selecione -> ")

    # Verificar valor digitado
    if escolha.isdigit():
        escolha = int(escolha)
    else:
        escolha = 6
        print("Digite um número.\nReinicie a Aplicação!")

    os.system('cls')  # Limpa a tela

    # Lógica de escolha
    match escolha:

        # Inserir valor
        case 1:
            try:
                print("----- Escolha o Sensor -----\n")
                print("----- 1 para PH -----\n")
                print("----- 2 para Fósforo -----\n")
                print("----- 3 para Potássio -----\n")
                escolha_sensor = input("Selecione -> ")
                if escolha_sensor == 1:
                    inserir_sensor_ph(
                    Ph =input("Digite o valor do PH"),
                    status = input("Digite o status do sensor"),
                    loc = input("Digite a localização do sensor "))           
                if escolha_sensor == 2:
                    inserir_sensor_fosforo(
                    Ph =input("Digite o valor do Fósforo"),
                    status = input("Digite o status do sensor"),
                    loc = input("Digite a localização do sensor "))
                if escolha_sensor == 3:
                    inserir_sensor_potassio(
                    Ph =input("Digite o valor do Potássio"),
                    status = input("Digite o status do sensor"),
                    loc = input("Digite a localização do sensor "))
            except ValueError:
                print("Digite um número")
            else:
                    # Caso haja sucesso na gravação
                    print("\n##### Dados Gravados #####")

        # LISTAR TODOS OS PETS
        case 2:
             try:
                print("----- Escolha o Sensor -----\n")
                print("----- 1 para PH -----\n")
                print("----- 2 para Fósforo -----\n")
                print("----- 3 para Potássio -----\n")
                escolha_sensor = input("Selecione -> ")
                if escolha_sensor == 1:
                    consultar_sensores_ph
                    lista_dados = []           
                if escolha_sensor == 2:
                    inserir_sensor_fosforo(
                    Ph =input("Digite o valor do Fósforo"),
                    status = input("Digite o status do sensor"),
                    loc = input("Digite a localização do sensor "))
                if escolha_sensor == 3:
                    inserir_sensor_potassio(
                    Ph =input("Digite o valor do Potássio"),
                    status = input("Digite o status do sensor"),
                    loc = input("Digite a localização do sensor "))
             except ValueError:
                print("Digite um número")
             else:
                    # Caso haja sucesso na gravação
                    print("\n##### Dados Gravados #####")

        # ALTERAR OS DADOS DE UM REGISTRO
        case 3:
            try:
                # ALTERANDO UM REGISTRO
                print("----- ALTERAR DADOS DO PET -----\n")

                lista_dados = []  # Lista para captura de dados da tabela

                pet_id = int(input(margem + "Escolha um Id: "))  # Permite o usuário escolher um Pet pelo id

                # Constrói a instrução de consulta para verificar a existência ou não do id
                consulta = f""" SELECT * FROM petshop WHERE id = {pet_id}"""
                inst_consulta.execute(consulta)
                data = inst_consulta.fetchall()

                # Preenche a lista com o registro encontrado (ou não)
                for dt in data:
                    lista_dados.append(dt)

                # analisa se foi encontrado algo
                if len(lista_dados) == 0: # se não há o id
                    print(f"Não há um pet cadastrado com o ID = {pet_id}")
                    input("\nPressione ENTER")
                else:
                    # Captura os novos dados
                    novo_tipo = input(margem + "Digite um novo tipo: ")
                    novo_nome = input(margem + "Digite um novo nome: ")
                    nova_idade = input(margem + "Digite uma nova idade: ")

                    # Constrói a instrução de edição do registro com os novos dados
                    alteracao = f"""
                    UPDATE petshop SET tipo_pet='{novo_tipo}', nome_pet='{novo_nome}', idade='{nova_idade}' WHERE id={pet_id}
                    """
                    inst_alteracao.execute(alteracao)
                    conn.commit()
            except ValueError:
                    print("Digite um número na idade!")
            except:
                print(margem + "Erro na transação do BD")
            else:
                print("\n##### Dados ATUALIZADOS! #####")

        # EXCLUIR UM REGISTRO
        case 4:
            print("----- EXCLUIR PET -----\n")
            lista_dados = []  # Lista para captura de dados da tabela
            pet_id = input(margem + "Escolha um Id: ")  # Permite o usuário escolher um Pet pelo ID
            if pet_id.isdigit():
                pet_id = int(pet_id)
                consulta = f""" SELECT * FROM petshop WHERE id = {pet_id}"""
                inst_consulta.execute(consulta)
                data = inst_consulta.fetchall()

                # Insere os valores da tabela na lista
                for dt in data:
                    lista_dados.append(dt)

                # Verifica se o registro está cadastrado
                if len(lista_dados) == 0:
                    print(f"Não há um pet cadastrado com o ID = {pet_id}")
                else:
                    # Cria a instrução SQL de exclusão pelo ID
                    exclusao = f"DELETE FROM petshop WHERE id={pet_id}"
                    # Executa a instrução e atualiza a tabela
                    inst_exclusao.execute(exclusao)
                    conn.commit()
                    print("\n##### Pet APAGADO! #####")  # Exibe mensagem caso haja sucesso
            else:
                print("O Id não é numérico!")

        # EXCLUIR TODOS OS REGISTROS
        case 5:
            print("\n!!!!! EXCLUI TODOS OS DADOS TABELA !!!!!\n")
            confirma = input(margem + "CONFIRMA A EXCLUSÃO DE TODOS OS PETS? [S]im ou [N]ÃO?")
            if confirma.upper() == "S":
                # Apaga todos os registros
                exclusao = "DELETE FROM petshop"
                inst_exclusao.execute(exclusao)
                conn.commit()

                # Depois de excluir todos os registros ele zera o ID
                data_reset_ids = """ ALTER TABLE petshop MODIFY(ID GENERATED AS IDENTITY (START WITH 1)) """
                inst_exclusao.execute(data_reset_ids)
                conn.commit()

                print("##### Todos os registros foram excluídos! #####")
            else:
                print(margem + "Operação cancelada pelo usuário!")

        # SAI DA APLICAÇÃO
        case 6:
            # Modificando o flag da conexão
            conexao = False

        # CASO O NUMERO DIGITADO NÃO SEJA UM DO MENU
        case _:
            input(margem + "Digite um número entre 1 e 6.")

    # Pausa o fluxo da aplicação para a leitura das informações
    input(margem + "Pressione ENTER")
else:
    print("Obrigado por utilizar a nossa aplicação! :)")