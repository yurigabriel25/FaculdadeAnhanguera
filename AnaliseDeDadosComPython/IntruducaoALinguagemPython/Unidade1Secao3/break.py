# Utilizando a função break o código para de ser executado na utlização dessa função, nesse caso, dentro o if solicita que a contagem pare ao chegar na letra a.
from dis import dis


disciplina = "Linguagem de programação"

for c in disciplina:
	if c == 'a':
		break
	else:
		print(c)

input("Digite qualquer tecla para sair...")