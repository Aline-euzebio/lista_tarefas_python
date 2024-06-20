from time import sleep

def adicionar(lista_tarefa:list):
    dicionario = {}
    dicionario['tarefa'] = str(input("Digite a tarefa: "))
    dicionario['prioridade'] = str(input("Digite sua prioridade[alta/media/baixa]: "))
    dicionario['categoria'] = str(input("Digite sua categoria[domestica, empresarial, lazer]: "))
    lista_tarefa.append(dicionario)

def listar(lista_tarefa:list):
   opcao = int (input('''
Voce deseja filtar sua busca por qual tarefa por:
1-categoria
2-prioridade
3-nenhum
'''))
   if opcao == 1:
        cat = str(input("Digite qual a categoria que deseja domestica/empresarial/lazer: "))

        for i in lista_tarefa:   
            for chave, valor in i.items():
                if i["categoria"] == cat:
                    print (f"{chave}, {valor}")
   if opcao == 2:
        prior = str(input("Digite qual a prioridade que desesja baixa/alta/baixa: "))

        for i in lista_tarefa:
            for chave, valor in i.items():
                if i ["prioridade"] == prior:
                    print(f"{chave}, {valor}")
   
   if opcao == 3:
    for i in lista_tarefa:
        for chave, valor in i.items():
            print (f"{chave}, {valor}")
        print("=30*")

def concluir(lista_tarefa):
    tarefa = str(input("Defina a tarefa que deseja concluir: "))
    prioridade = str(input("Digite a prioridade da tarefa: "))
    categoria = str(input("Defina a categoria: "))
    lista_tarefa.remove({'tarefa':tarefa,'prioridade':prioridade,'categoria':categoria})
    print("\33[32mTarefa concluida\033[m")
    sleep(2)