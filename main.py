from funções import *

while True:
    escolha = menu()
    if escolha == 1:
        adicionar()
    if escolha == 2:
        exibir()
    if escolha == 3:
        nome = input('digite o nome do autor que deseja ver os livros: ')
        exibir_por_nome(nome)
    if escolha == 4:
        exibir()
        nome_livro = input('digite o titulo que deseja excluir: ')
        excluir(nome_livro)
    if escolha == 5:
        break
    if escolha < 1 or escolha > len(interface):
        print('opção invalida, digite novamente')
print('Volte sempre!')