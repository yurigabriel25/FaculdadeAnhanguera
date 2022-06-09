# Exemplo de aplicação da estrutura AND:

qtde_faltas = int(input("Digite a quantidade de faltas do aluno(a): "))
media_final = float(input("Digite a média final do aluno(a): "))

if qtde_faltas <= 5 and media_final >= 7:
        print("O aluno está aprovado.")
else:
        print("O aluno está reprovador.")

input("Digite qualquer tecla para sair...")
