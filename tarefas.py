import json
from datetime import datetime
from utils import validar_data, prioridade_num, tarefa_vencida

tarefas = []


def salvar_tarefas():

    with open("tarefas.json", "w", encoding="utf-8") as arquivo:

        tarefas_salvar = []

        for t in tarefas:

            tarefas_salvar.append({
                "descricao": t["descricao"],
                "data": t["data"].strftime("%d/%m/%Y"),
                "prioridade": t["prioridade"],
                "concluida": t["concluida"]
            })

        json.dump(tarefas_salvar, arquivo, indent=4, ensure_ascii=False)


def carregar_tarefas():

    try:

        with open("tarefas.json", "r", encoding="utf-8") as arquivo:

            dados = json.load(arquivo)

            for t in dados:

                tarefas.append({
                    "descricao": t["descricao"],
                    "data": datetime.strptime(t["data"], "%d/%m/%Y"),
                    "prioridade": t["prioridade"],
                    "concluida": t.get("concluida", False)
                })

    except FileNotFoundError:
        pass


def adicionar_tarefa():

    descricao = input("Digite a tarefa: ")

    while True:

        data_str = input("Digite a data (dd/mm/aaaa): ")

        data_obj = validar_data(data_str)

        if data_obj:
            break
        else:
            print("Data inválida!")

    while True:

        prioridade = input("Prioridade (alta/média/baixa): ").lower()

        if prioridade in ["alta", "média", "media", "baixa"]:

            if prioridade == "media":
                prioridade = "média"

            break

        else:
            print("Prioridade inválida!")

    tarefas.append({
        "descricao": descricao,
        "data": data_obj,
        "prioridade": prioridade,
        "concluida": False
    })

    salvar_tarefas()

    print("Tarefa adicionada!")
    input("Pressione Enter...")


def listar_tarefas():

    print("\n--- SUAS TAREFAS ---")

    if tarefas:

        tarefas_ordenadas = sorted(
            tarefas,
            key=lambda t: (t["data"], prioridade_num(t["prioridade"]))
        )

        for i, t in enumerate(tarefas_ordenadas, start=1):

            if t["concluida"]:
                status = "✅ Concluída"

            elif tarefa_vencida(t["data"]):
                status = "⚠️ VENCIDA"

            else:
                status = "⏳ Pendente"

            print(
                f"{i} - {t['descricao']} | {status} | "
                f"{t['data'].strftime('%d/%m/%Y')} | {t['prioridade']}"
            )

    else:
        print("Nenhuma tarefa cadastrada.")

    input("\nPressione Enter...")


def remover_tarefa():

    if tarefas:

        tarefas_ordenadas = sorted(
            tarefas,
            key=lambda t: (t["data"], prioridade_num(t["prioridade"]))
        )

        print("\n--- REMOVER TAREFA ---")

        for i, t in enumerate(tarefas_ordenadas, start=1):
            print(f"{i} - {t['descricao']}")

        numero = input("Número da tarefa: ")

        if numero.isdigit():

            numero = int(numero)

            if 1 <= numero <= len(tarefas_ordenadas):

                tarefa_real = tarefas_ordenadas[numero - 1]

                tarefas.remove(tarefa_real)

                salvar_tarefas()

                print("Tarefa removida!")

            else:
                print("Número inválido!")

        else:
            print("Digite apenas números!")

    else:
        print("Nenhuma tarefa cadastrada.")

    input("Pressione Enter...")


def concluir_tarefa():

    if tarefas:

        tarefas_ordenadas = sorted(
            tarefas,
            key=lambda t: (t["data"], prioridade_num(t["prioridade"]))
        )

        print("\n--- CONCLUIR TAREFA ---")

        for i, t in enumerate(tarefas_ordenadas, start=1):

            status = "✅" if t["concluida"] else "⏳"

            print(f"{i} - {t['descricao']} {status}")

        numero = input("Digite o número: ")

        if numero.isdigit():

            numero = int(numero)

            if 1 <= numero <= len(tarefas_ordenadas):

                tarefa_real = tarefas_ordenadas[numero - 1]

                tarefa_real["concluida"] = True

                salvar_tarefas()

                print("Tarefa concluída!")

            else:
                print("Número inválido!")

        else:
            print("Digite apenas números!")

    else:
        print("Nenhuma tarefa cadastrada.")

    input("Pressione Enter...")


def mostrar_vencidas():

    print("\n--- TAREFAS VENCIDAS ---")

    encontrou = False

    for t in tarefas:

        if tarefa_vencida(t["data"]) and not t["concluida"]:

            print(
                f"{t['descricao']} | "
                f"{t['data'].strftime('%d/%m/%Y')} | "
                f"{t['prioridade']}"
            )

            encontrou = True

    if not encontrou:
        print("Nenhuma tarefa vencida.")

    input("\nPressione Enter...")


def mostrar_estatisticas():

    total = len(tarefas)

    concluidas = sum(1 for t in tarefas if t["concluida"])

    pendentes = sum(1 for t in tarefas if not t["concluida"])

    vencidas = sum(
        1 for t in tarefas
        if tarefa_vencida(t["data"]) and not t["concluida"]
    )

    print("\n📊 ESTATÍSTICAS\n")

    print(f"Total de tarefas: {total}")
    print(f"Concluídas: {concluidas}")
    print(f"Pendentes: {pendentes}")
    print(f"Vencidas: {vencidas}")

    input("\nPressione Enter...")
    
def editar_tarefa():

    if tarefas:

        tarefas_ordenadas = sorted(
            tarefas,
            key=lambda t: (t["data"], prioridade_num(t["prioridade"]))
        )

        print("\n--- EDITAR TAREFA ---")

        for i, t in enumerate(tarefas_ordenadas, start=1):
            print(f"{i} - {t['descricao']}")

        numero = input("Digite o número da tarefa: ")

        if numero.isdigit():

            numero = int(numero)

            if 1 <= numero <= len(tarefas_ordenadas):

                tarefa = tarefas_ordenadas[numero - 1]

                print("\nDeixe vazio para manter o valor atual")

                nova_desc = input(f"Nova descrição ({tarefa['descricao']}): ")

                if nova_desc:
                    tarefa["descricao"] = nova_desc

                while True:

                    nova_data = input(
                        f"Nova data ({tarefa['data'].strftime('%d/%m/%Y')}): "
                    )

                    if not nova_data:
                        break

                    data_obj = validar_data(nova_data)

                    if data_obj:
                        tarefa["data"] = data_obj
                        break
                    else:
                        print("Data inválida!")

                while True:

                    nova_prioridade = input(
                        f"Nova prioridade ({tarefa['prioridade']}): "
                    ).lower()

                    if not nova_prioridade:
                        break

                    if nova_prioridade in ["alta", "média", "media", "baixa"]:

                        if nova_prioridade == "media":
                            nova_prioridade = "média"

                        tarefa["prioridade"] = nova_prioridade
                        break

                    else:
                        print("Prioridade inválida!")

                salvar_tarefas()

                print("Tarefa atualizada!")

            else:
                print("Número inválido!")

        else:
            print("Digite apenas números!")

    else:
        print("Nenhuma tarefa cadastrada.")

    input("Pressione Enter...")