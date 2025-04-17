def adicionar_contatos (contatos, nome_novo_contato, telefone_novo_contato, email_novo_contato):
    dicionario_contatos = {'nome': nome_novo_contato, 'telefone': telefone_novo_contato, 'email': email_novo_contato, 'favorito': False}
    contatos.append(dicionario_contatos)
    print('Você adicionou um novo contato com sucesso!')
    return

def ver_contatos(tarefas):
    print('\nLista de Contatos:')
    for indice, contato in enumerate(contatos, start=1):
        status = "★" if contato["favorito"] == True else "não"
        print(f'{indice}.')
        print(f'CONTATO: {contato["nome"]}')
        print(f'TELEFONE: {contato["telefone"]}') 
        print(f'EMAIL: {contato['email']}')
        print(f'FAVORITADO: {status}\n')
    
def editar_contatos(contatos, indice_contato, nome_novo_contato, telefone_novo_contato, email_novo_contato):     
    indice_corrigido = int(indice_contato) - 1
    if indice_corrigido >= 0 and indice_corrigido < len(contatos):
        contatos[indice_corrigido]['nome'] = nome_novo_contato
        contatos[indice_corrigido]['telefone'] = telefone_novo_contato
        contatos[indice_corrigido]['email'] = email_novo_contato
        print('\nO CONTATO FOI ATUALIZADO')
    else:
        print('\nEscolha outra alternativa!')

def favoritar_contatos(contatos, indice_contato):
    indice_corrigido = int(indice_contato) - 1
    if indice_corrigido >= 0 and indice_corrigido < len(contatos):
        contatos[indice_corrigido]['favorito'] = True

def desfavoritar_contatos(contatos, indice_contato):
    indice_corrigido = int(indice_contato) - 1
    if indice_corrigido >= 0 and indice_corrigido < len(contatos):
        if contatos[indice_corrigido]['favorito'] == True:
            contatos[indice_corrigido]['favorito'] = False
        else: 
            print ('Esse contato não estava favoritado')
    else:
        print('Tente outra alternativa!')

def lista_favoritos(contatos):
    print('\nContatos Favoritados:')
    favoritos = [contato for contato in contatos if contato.get("favorito") == True]
    
    if not favoritos:
        print('Nenhum contato favoritado.\n')
    else:
        for indice, contato in enumerate(favoritos, start=1):
            print(f'{indice}.')
            print(f'CONTATO: {contato["nome"]}')
            print(f'TELEFONE: {contato["telefone"]}') 
            print(f'EMAIL: {contato["email"]}')
            print(f'FAVORITADO: ★\n')
def lista_delete(contatos, indice_contato):
    indice_corrigido = int(indice_contato) - 1
    if 0 <= indice_corrigido < len(contatos):
        contato_removido = contatos.pop(indice_corrigido)
        print(f'O contato "{contato_removido["nome"]}" foi deletado com sucesso!')
    else:
        print('Índice inválido. Tente novamente.')

    



        


    
    


contatos = []

while True:
    print('\nMenu da Lista de Contatos: ')
    print('1. Adicionar Contato')
    print('2. Ver Contatos')
    print('3. Editar Contatos')
    print('4. Favoritar Contatos')
    print('5. Desfavoritar Contatos')
    print('6. Lista de favoritos')
    print('7. Deletar Contato')
    print('8. Sair')


    escolha = input('Digite a sua escolha:')

    if escolha == '1':
        nome_novo_contato = input("Digite o nome do contato: ")
        telefone_novo_contato = input("Digite o telefone do contato: ")
        email_novo_contato = input("Digite o email do contato: ")
        adicionar_contatos(contatos, nome_novo_contato, telefone_novo_contato, email_novo_contato)
    elif escolha == '2':
        ver_contatos(contatos)
    elif escolha == '3':
        ver_contatos(contatos)
        indice_contato = input('Digite o número do contato que deseja alterar: ')
        nome_novo_contato = input("Digite o nome do contato: ")
        telefone_novo_contato = input("Digite o telefone do contato: ")
        email_novo_contato = input("Digite o email do contato: ")
        editar_contatos(contatos, indice_contato, nome_novo_contato, telefone_novo_contato, email_novo_contato)
        ver_contatos(contatos)
    elif escolha == '4':
        ver_contatos(contatos)
        indice_contato = input('Escolha indice de um contato que deseje favoritar: ')
        favoritar_contatos(contatos, indice_contato)
    elif escolha == '5':
        ver_contatos(contatos)
        indice_contato = input('Escolha a opção que deseja desfavoritar: ')
        desfavoritar_contatos(contatos, indice_contato)
    elif escolha == '6':
        lista_favoritos(contatos)
    elif escolha == '7':
        ver_contatos(contatos)
        indice_contato = input('Escolha o contato que deseja deletar: ')
        lista_delete(contatos, indice_contato)
    elif escolha == '8':
        break