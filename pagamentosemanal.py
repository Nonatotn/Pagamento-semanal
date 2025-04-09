def calcular_pagamento(salario_hora, horas_regulares, horas_extras):
    """
    Calcula o pagamento semanal total com base no salário por hora,
    horas regulares e horas extras.

    :param salario_hora: Salário por hora (float)
    :param horas_regulares: Total de horas regulares (float)
    :param horas_extras: Total de horas extras (float)
    :return: Pagamento total (float)
    """
    pagamento_regular = salario_hora * horas_regulares
    pagamento_extras = horas_extras * salario_hora * 1.5
    pagamento_total = pagamento_regular + pagamento_extras
    return pagamento_total

if __name__ == "__main__":
    try:
        salario_hora = float(input("Digite o salário por hora (valor positivo): "))
        horas_regulares = float(input("Digite o total de horas regulares (valor positivo): "))
        horas_extras = float(input("Digite o total de horas extras (valor positivo): "))

        if salario_hora < 0 or horas_regulares < 0 or horas_extras < 0:
            print("Erro: Todos os valores devem ser positivos.")
        else:
            pagamento = calcular_pagamento(salario_hora, horas_regulares, horas_extras)
            print(f"O pagamento semanal total é: R$ {pagamento:.2f}")
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")