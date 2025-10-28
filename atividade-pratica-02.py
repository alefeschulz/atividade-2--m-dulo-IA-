def conversor_moeda():
    valor_reais = 100.00
    taxa_dolar = 5.60
    taxa_euro = 6.60

    valor_dolar = valor_reais / taxa_dolar
    valor_euro = valor_reais / taxa_euro

    print("\n=== Conversor de Moeda ===")
    print(f"Valor em Reais: R$ {valor_reais:.2f}")
    print(f"Valor em Dólares: US$ {valor_dolar:.2f}")
    print(f"Valor em Euros: € {valor_euro:.2f}\n")


def calculadora_desconto():
    produto = "Camiseta"
    preco_original = 50.00
    desconto_percentual = 20

    valor_desconto = preco_original * (desconto_percentual / 100)
    preco_final = preco_original - valor_desconto

    print("\n=== Calculadora de Desconto ===")
    print(f"Produto: {produto}")
    print(f"Preço original: R$ {preco_original:.2f}")
    print(f"Desconto: {desconto_percentual}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Preço final: R$ {preco_final:.2f}\n")


def calculadora_media():
    nota1 = 7.5
    nota2 = 8.0
    nota3 = 6.5
    media = (nota1 + nota2 + nota3) / 3

    print("\n=== Calculadora de Média Escolar ===")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média final: {media:.2f}\n")


def calculadora_consumo():
    distancia = 300
    combustivel = 25
    consumo_medio = distancia / combustivel

    print("\n=== Calculadora de Consumo de Combustível ===")
    print(f"Distância percorrida: {distancia} km")
    print(f"Combustível gasto: {combustivel} litros")
    print(f"Consumo médio: {consumo_medio:.2f} km/l\n")


def calculadora_soma():
    print("\n=== Calculadora de Soma ===")
    while True:
        try:
            A = int(input("Digite o valor de A (inteiro): "))
            B = int(input("Digite o valor de B (inteiro): "))
            break
        except ValueError:
            print("⚠️ Entrada inválida! Digite apenas números inteiros.")
    X = A + B
    print(f"X = {X}\n")


def calculadora_salario():
    print("\n=== Calculadora de Salário ===")
    while True:
        try:
            numero_funcionario = int(input("Digite o número do funcionário: "))
            horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
            valor_por_hora = float(input("Digite o valor recebido por hora: "))
            break
        except ValueError:
            print("⚠️ Entrada inválida! Digite valores numéricos válidos.")
    
    salario = horas_trabalhadas * valor_por_hora
    print(f"NÚMERO = {numero_funcionario}")
    print(f"SALÁRIO = R$ {salario:.2f}\n")


# ======= MENU PRINCIPAL =======
while True:
    print("===== MENU DE OPÇÕES =====")
    print("1 - Conversor de Moeda")
    print("2 - Calculadora de Desconto")
    print("3 - Calculadora de Média Escolar")
    print("4 - Calculadora de Consumo de Combustível")
    print("5 - Calculadora de Soma com Entrada do Usuário")
    print("6 - Calculadora de Salário por Horas Trabalhadas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        conversor_moeda()
    elif opcao == "2":
        calculadora_desconto()
    elif opcao == "3":
        calculadora_media()
    elif opcao == "4":
        calculadora_consumo()
    elif opcao == "5":
        calculadora_soma()
    elif opcao == "6":
        calculadora_salario()
    elif opcao == "0":
        print("\nSaindo do programa... Até mais! 👋")
        break
    else:
        print("\n⚠️ Opção inválida! Escolha um número entre 0 e 6.\n")
