import mysql.connector
from agenda import criar_contato, listar_contatos, atualizar_contato, excluir_contato

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="enzo123",
        database="agenda"
    )

def testar_criar_contato():
    print("Testando a criação de novos contatos...")
    criar_contato("Enzo", "123456789")
    criar_contato("aaaaa", "987654321")
    contatos = listar_contatos()
    assert len(contatos) == 2, f"Esperado 2 contatos, mas encontrei {len(contatos)}"
    print("Criação de contatos testada com sucesso!")

def testar_listar_contatos():
    print("Testando a listagem de contatos...")
    contatos = listar_contatos()
    assert len(contatos) > 0, "Nenhum contato encontrado"
    for contato in contatos:
        print(f"ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}")
    print("Listagem de contatos testada com sucesso!")

def testar_atualizar_contato():
    print("Testando a atualização de contatos...")
    contatos = listar_contatos()
    if len(contatos) > 0:
        indice = 0  
        novo_nome = "aaaaa novo"
        novo_telefone = "1122334455"
        sucesso = atualizar_contato(indice, novo_nome, novo_telefone)
        assert sucesso, "Falha ao atualizar o contato"
        contatos_atualizados = listar_contatos()
        assert contatos_atualizados[indice][1] == novo_nome, f"Nome não atualizado para {novo_nome}"
        print("Atualização de contato testada com sucesso!")
    else:
        print("Nenhum contato encontrado para atualizar.")

def testar_excluir_contato():
    print("Testando a exclusão de contatos...")
    contatos = listar_contatos()
    if len(contatos) > 0:
        indice = 0  
        sucesso = excluir_contato(indice)
        assert sucesso, "Falha ao excluir o contato"
        contatos_restantes = listar_contatos()
        assert len(contatos_restantes) == len(contatos) - 1, "Contato não excluído corretamente"
        print("Exclusão de contato testada com sucesso!")
    else:
        print("Nenhum contato encontrado para excluir.")

if __name__ == "__main__":
    conectar_banco()

    testar_criar_contato()
    testar_listar_contatos()
    testar_atualizar_contato()
    testar_excluir_contato()

    print("\nTodos os testes foram executados com sucesso!")
