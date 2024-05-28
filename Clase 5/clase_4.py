#String

#Método Upper
# cadena1 = 'soY la pRimer cadena'
# print(cadena1)
# cadena1_en_mayusculas = cadena1.upper()
# #cadena1 = cadena1.upper()
# print(cadena1)
# print(cadena1_en_mayusculas)

# cadena1_en_minusculas = cadena1.lower()
# print(cadena1_en_minusculas)

# cadena1_en_modo_titulo = cadena1.title()
# print(cadena1_en_modo_titulo)

# cadena1_en_modo_parraf = cadena1.capitalize()
# print(cadena1_en_modo_parraf)


#######################################
#######################################
#######################################

# cadena1 = 'soY la pRimer cadena'
# print(cadena1.count('a'))
# print(cadena1.count(' '))
# print(cadena1.count('z'))

# print(cadena1.find('a'))
# print(cadena1.find(' '))
# print(cadena1.find(''))
# print(cadena1.find('z'))

# print(cadena1.rfind('a'))
# print(cadena1.rfind(' '))
# print(cadena1.rfind(''))
# print(cadena1.rfind('z'))

# cadena2 = 'segunda cadena al rescate'
# lista = cadena2.split()
# print(lista)
# lista2 = cadena2.split('a')
# print(lista2)
# lista3 = cadena2.split('a ')
# print(lista3)
# lista4 = cadena2.split('asd el pepe loco')
# print(lista4)

# lista = ['segunda', 'cadena', 'al', 'rescate']
# #cadena = ' '.join(lista)
# # cadena = '<>pepito<>solito'.join(lista)
# # print(cadena)
# cadena = ' -=-=- '.join(lista)
# print(cadena)

# password = input('Ingrese su password: ')
# # print(password.strip())
# # print(password)

# print(password.strip('asd'))
# print(password)

# palabra_repetida = 'cadena cadena cadena cadena'
# # palabra_repetida_modificada = palabra_repetida.replace('cadena', 'otra')
# palabra_repetida_modificada = palabra_repetida.replace('cadena', 'otra',3)
# print(palabra_repetida)
# print(palabra_repetida_modificada)

#Lista
#lista = ['segunda', 'cadena', 'al', 'rescate']
# print(lista)
# lista.clear()
# print(lista)

#lista2 = lista + [1,2,3]
# lista += [1,2,3]
# print(lista)
# lista.extend([1,2,3])
# print(lista)


# lista = ['segunda', 'cadena', 'al', 'rescate']
# lista.insert(1,0)
# print(lista)

# lista = ['segunda', 'cadena', 'al', 'rescate']
# lista.reverse()
# print(lista)

# lista_numeros = [5,4,2,1,8]
# #lista_numeros.sort()
# lista_numeros.sort(reverse=False)
# print(lista_numeros)

# lista_numeros1 = ['5','1','2','13']
# lista_numeros1.sort()
# print(lista_numeros1)


#Sets
#Métodos
# conjunto1 = {1,'valor1',(1,True)}
# iterable1 = (1,'valor1',(1,True))
# print(conjunto1.isdisjoint(iterable1))
# iterable2 = (2,'valor2',(2,True))
# print(conjunto1.isdisjoint(iterable2))

# conjunto1 = {1,'valor1',(1,True)}
# iterable1 = (1,'valor1',(1,True),45)

# print(conjunto1.issubset(iterable1))
# print(conjunto1.issuperset(iterable1))

# conjunto1 = {1,'valor1',(1,True)}
# iterable1 = (1,'valor1',(2,True),45)
# conjunto3 = conjunto1.union(iterable1)
# print(conjunto1)
# print(conjunto3)

# conjunto1 = {1,'valor1',(1,True)}
# iterable1 = (1,'valor1',(2,True),45)
# #conjunto3 = conjunto1.union(iterable1)
# print(conjunto1.difference(iterable1))
# print(conjunto1)

# conjunto1 = {1,'valor1',(1,True)}
# iterable1 = (1,'valor2',(1,True),45)
# #conjunto3 = conjunto1.union(iterable1)
# print(conjunto1.intersection(iterable1))
# print(conjunto1)

# conjunto1 = {1,'valor1',(1,True)}
# iterable1 = (1,'valor2',(1,True),45)
# conjunto1.difference_update(iterable1)
# print(conjunto1)

# conjunto1 = {1,'valor1',(1,True)}
# iterable1 = (1,'valor2',(1,True),45)
# conjunto1.intersection_update(iterable1)
# print(conjunto1)

#Dicts
# auto = {
#     'motor' : 'v8',
#     'color' : 'Negro',
#     'vidrios' : (6,'blindados'),
#     'pasajeros': 4
# }

# valor1 = auto['motor']
# print(valor1)


# print(auto.keys())
# print(auto.values())
# print(auto.items())


# numero1 = 1
# numero2 = numero1
# numero1 += 2
# print(numero1)
# print(numero2)

# conjunto1 = {1,'conjunto 1', (1,True)}
# #conjunt3 = conjunto1
# conjunto3 = conjunto1.copy()
# print(conjunto3)
# conjunto1.add(465)
# print(conjunto1)
