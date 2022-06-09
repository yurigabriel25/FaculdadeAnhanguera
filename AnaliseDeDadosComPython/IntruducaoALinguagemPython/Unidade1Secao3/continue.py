# já na função continue o código prossegue, mas nesse caso todas as letras a da frase são puladas pela função continue.

from dis import dis


disciplina = "Linguagem de programação"

for c in disciplina:
	if c == 'a':
		continue
	else:
		print(c)

input("Digite qualquer tecla para sair...")