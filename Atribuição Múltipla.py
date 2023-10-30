#Atribuição múltipla
a, b = 1, 2
print('Antes da troca')
print("O valor das variáveis: a={}, b={}".format(a, b))
#Primeira troca
temp = a
a = b
b = temp
print('Primeira troca')
print("O valor das variáveis: a={}, b={}".format(a, b))
#Segunda troca
a, b, = b, a
print('Segunda troca')
print("O valor das variáveis: a={}, b={}".format(a, b))