
print("Base de cálculo do IRPF de 2020 sobre o salário dos funcionários.")

print()

salario_funcionarios = 0
salario_funcionarios = float(input("Qual o valor do salário do funcionário? R$ "))

if salario_funcionarios <= 1903.98:
	print(f"O funcionário está isento de pagar imposto de renda e vai receber R${salario_funcionarios}.")
elif salario_funcionarios <= 2826.65:
	print(f"O funcionário vai receber R$ {salario_funcionarios - 142.08}")
elif salario_funcionarios <= 3751.05:
	print(f"O funcionário vai receber R$ {salario_funcionarios - 354.80}")
elif salario_funcionarios <= 4664.68:
	print(f"O funcionário vai receber R$ {salario_funcionarios - 636.13}")
else:
	print(f"O funcionário vai receber R$ {salario_funcionarios - 869.36}")

print()

input("Digite enter para sair...")