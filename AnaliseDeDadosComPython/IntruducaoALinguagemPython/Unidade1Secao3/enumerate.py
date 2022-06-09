# Sendo uma estrutura de repetição for() implementando a função enumerate(), o loop se iniciar com o for tendo como controladores c e i, o enumerate se encarrega de guardar dentro de i a posição de cada string e dentro de c o valor de cada uma.
nome = "Yuri Gabriel"

for i, c in enumerate(nome):
	print(f"Posição = {i}, valor = {c}")

input("Digite qualquer tecla para sair...")