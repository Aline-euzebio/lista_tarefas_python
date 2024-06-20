
from funcoes import*

tarefa = []
while True:
    #looping que vai sempre perguntar ao usuario o que ele deseja fazer (adicionar, remover, listar)
    print('='*30)
    print(f'{"MENU INTERATIVO".center(30)}')
    print('='*30)
    menu = str(input('''
1-para adicionar
2-para concluir
3-para listar
'''))
    if menu == "1":
        adicionar(tarefa)
    elif menu == "2":
        concluir(tarefa)
    elif menu == "3":
        listar(tarefa)
    perg = str(input("Você deseja continuar ?[S/N]")).upper().strip()[0]
    if perg == "N":
        break