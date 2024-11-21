import mysql.connector
import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="enzo123",
    database="agenda"
)
cursor = conexao.cursor()

def criar_contato(nome, telefone):
    sql = "INSERT INTO contatos (nome, telefone) VALUES (%s, %s)"
    valores = (nome, telefone)
    cursor.execute(sql, valores)
    conexao.commit()
    return True

def listar_contatos():
    cursor.execute("SELECT * FROM contatos")
    resultados = cursor.fetchall()
    return resultados 

def atualizar_contato(indice, novo_nome, novo_telefone):
    cursor.execute("SELECT * FROM contatos")
    resultados = cursor.fetchall()
    if indice >= 0 and indice < len(resultados):
        contato_id = resultados[indice][0]
        sql = "UPDATE contatos SET nome = %s, telefone = %s WHERE id = %s"
        valores = (novo_nome, novo_telefone, contato_id)
        cursor.execute(sql, valores)
        conexao.commit()
        return True
    else:
        return False

def excluir_contato(indice):
    cursor.execute("SELECT * FROM contatos")
    resultados = cursor.fetchall()
    if indice >= 0 and indice < len(resultados):
        contato_id = resultados[indice][0]
        sql = "DELETE FROM contatos WHERE id = %s"
        valores = (contato_id,)
        cursor.execute(sql, valores)
        conexao.commit()
        return True
    else:
        return False

if __name__ == "__main__":
    while True:
        print("\nOpções:")
        print("1. Criar novo contato")
        print("2. Listar contatos")
        print("3. Atualizar contato")
        print("4. Excluir contato")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")
        limpar_tela()
        if escolha == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            criar_contato(nome, telefone)
        elif escolha == "2":
            listar_contatos()
        elif escolha == "3":
            listar_contatos()
            indice = int(input("Digite o índice do contato que deseja atualizar: ")) - 1
            novo_nome = input("Digite o novo nome: ")
            novo_telefone = input("Digite o novo telefone: ")
            atualizar_contato(indice, novo_nome, novo_telefone)
        elif escolha == "4":
            listar_contatos()
            indice = int(input("Digite o índice do contato que deseja excluir: ")) - 1
            excluir_contato(indice)
        elif escolha == "5":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
