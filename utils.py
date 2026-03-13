from datetime import datetime


def validar_data(data_str):
    try:
        data_obj = datetime.strptime(data_str, "%d/%m/%Y")

        if data_obj.date() < datetime.now().date():
            return None

        return data_obj

    except ValueError:
        return None


def prioridade_num(p):

    if p == "alta":
        return 1

    elif p == "média":
        return 2

    elif p == "baixa":
        return 3


def tarefa_vencida(data_tarefa):

    hoje = datetime.now().date()

    return data_tarefa.date() < hoje