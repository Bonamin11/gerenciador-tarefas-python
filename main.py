import os
from tarefas import (
    carregar_tarefas,
    adicionar_tarefa,
    listar_tarefas,
    remover_tarefa,
    concluir_tarefa,
    mostrar_vencidas,
    mostrar_estatisticas,
    editar_tarefa
)

carregar_tarefas()

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Marcar tarefa como concluída")
    print("5 - Sair")
    print("6 - Mostrar tarefas vencidas")
    print("7 - Mostrar estatísticas")
    print("8 - Editar tarefa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        remover_tarefa()

    elif opcao == "4":
        concluir_tarefa()

    elif opcao == "5":
        print("Saindo...")
        break

    elif opcao == "6":
        mostrar_vencidas()

    elif opcao == "7":
        mostrar_estatisticas()
        
    elif opcao == "8":
        editar_tarefa()

    else:
        print("Opção inválida!")
        input("Pressione Enter...")