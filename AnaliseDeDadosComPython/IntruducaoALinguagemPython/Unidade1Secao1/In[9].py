# Utilizando a fórmula de equação do segundo grau, segue o seguinte exemplo proposto:
# Onde Y (resultado) depende do valor de X. X é a variável independente e Y a dependente.
# Considerando os valores a = 2, b = 0.5 e c = 1:
from time import time

a = 2
b = 0.5
c = 1

x = float(input("Digite o valor de x: ")) # A variável X converte o valor digitado para float, evitando erro de srt.

y = a * x ** 2 + b * x + c

print(f"O resultado de y para x = {x} é {y}.")

input("Digite qualquer tecla para fechar...")