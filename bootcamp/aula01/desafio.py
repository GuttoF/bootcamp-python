# 1. Solicita ao usuário que digite o seu nome
nome = input("Qual é o seu nome? ")

# 2. Solicita o valor do salário e converte para float
salario = float(input("Qual é o seu salário? "))

# 3. Solicita o valor do bônus recebido e converte para float
bonus = float(input("Qual é o valor do bônus recebido? "))

# 4. Calcula o valor do KPI
valor = float(1000 + salario * bonus)

# 5. Imprime o valor total do kpi
print(f"O valor total do KPI de {nome} é de R$ {round(valor, 2)}")
