lista = [
        {'titulo': 'Dom Quixote', 'autor': 'Miguel de Cervantes', 'ano': 1605},
        {'titulo': 'Guerra e Paz', 'autor':' Liev Tolstói','ano':1869},
        {'titulo': 'A Montanha Mágica', 'autor':'Thomas Mann','ano':1924},
        {'titulo': 'Cem Anos de Solidão', 'autor':'Gabriel García','ano':1967},
        {'titulo': 'Ulisses ', 'autor':'James Joyce','ano':1922},
        {'titulo': 'Em Busca do Tempo Perdido', 'autor': 'Marcel Proust', 'ano': 1913}
]

interface = ['Adicionar Livro', 'Listar Livros', 'Buscar Livro por Autor', 'Excluir Livro', 'Sair']
livro = {}
def linha():
    print('-'*60)

def menu():
    c = 1
    linha()
    print('Seja bem vindo a sua biblioteca de livros!')
    linha()
    for i in interface:
        print(f'{c} - ', end='')
        print(i)
        c+=1
    escolha = ler_inteiro('digite a opção desejada: ')
    linha()
    return escolha

def ler_inteiro(num):
    while True:
        try:
            entrada = int(input(num))
        except:
            print('Erro, digite um número')
        else:
            return entrada

def exibir():
    print('Listando livros da sua biblioteca')
    linha()
    c = 1
    for i in lista:
        print(f'{c} - Titulo: {i["titulo"]}', end=' ')
        print(f'/ Autor: {i["autor"]}', end=' ')
        print(f'/ Ano: {i["ano"]}')
        c+=1
def adicionar():
    livro['titulo'] = input('digite o nome do livro: ')
    livro['autor'] = input('digite o nome do autor: ')
    livro['ano'] = ler_inteiro('digite o ano de publicação do livro: ')
    lista.append(livro.copy())
def exibir_por_nome(autor):
    c = 1
    autor_achado = 'não achado'
    for i in lista:
        if autor == i['autor']:
            print(f'{c} - Titulo: {i["titulo"]}', end=' ')
            print(f'/ Autor: {i["autor"]}', end=' ')
            print(f'/ Ano: {i["ano"]}')
            c += 1
            autor_achado = 'achado'
    if autor_achado == 'não achado':
        print('autor não encontrado')

def excluir(nome_livro):
    indice_para_remover = None
    for i, livro in enumerate(lista):
        if livro['titulo'] == nome_livro:
            indice_para_remover = i
            break
    if indice_para_remover is not None:
        del lista[indice_para_remover]
        print('Filme excluído com sucessso!')
    else:
        print('titulo não encontrado')
