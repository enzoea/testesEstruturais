from gerenciador_contatos import criar_contato, listar_contatos, atualizar_contato, excluir_contato

def testar_criar_contato():
    print("Testando a criação de novos contatos...")
    criar_contato("Enzo", "123456789")
    criar_contato("Maria", "987654321")
    assert len(contatos) == 2, f"Esperado 2 contatos, mas encontrei {len(contatos)}"
    print("Criação de contatos testada com sucesso!")

def testar_listar_contatos():
    print("Testando a listagem de contatos...")
    listar_contatos()
    assert len(contatos) > 0, "Nenhum contato encontrado"
    print("Listagem de contatos testada com sucesso!")

def testar_atualizar_contato():
    print("Testando a atualização de contatos...")
    if len(contatos) > 0:
        indice = 0  
        novo_nome = "Enzo Atualizado"
        novo_telefone = "1122334455"
        atualizar_contato(indice, novo_nome, novo_telefone)
        assert contatos[indice]["nome"] == novo_nome, "Nome não atualizado corretamente"
        assert contatos[indice]["telefone"] == novo_telefone, "Telefone não atualizado corretamente"
        print("Atualização de contato testada com sucesso!")
    else:
        print("Nenhum contato encontrado para atualizar.")

def testar_excluir_contato():
    print("Testando a exclusão de contatos...")
    if len(contatos) > 0:
        indice = 0  
        excluir_contato(indice)
        assert len(contatos) == 1, "Contato não excluído corretamente"
        print("Exclusão de contato testada com sucesso!")
    else:
        print("Nenhum contato encontrado para excluir.")

if __name__ == "__main__":
    testar_criar_contato()
    testar_listar_contatos()
    testar_atualizar_contato()
    testar_excluir_contato()
    print("\nTodos os testes foram executados com sucesso!")
