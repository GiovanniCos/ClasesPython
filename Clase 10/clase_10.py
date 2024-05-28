#def dividir(a,b):
#    try:
#        return a/b
#    except:
 #       print('No se puede dividir porque el divisor no es correcto')
  #  return 'hola'    
#try:
 #   print(dividir(5,'a'))
#except:
 #   print('Mensaje del except de afuera')
 
# bandera = True
# while bandera:
#     print('''
# Selecciona una opción:
# 1. Retirar efectivo
# 2.Cambiar contraseña
# 3.Salir
# ''')
#     try:
#         opcion = input('Ingrese la opción: ')
#         if opcion == '1':
#             print('Retirar efectivo')
#         elif opcion == '2':
#             print('Cambiar contraseña')
#         elif opcion == '3':
#             bandera = False
#         else:
#             raise Exception()
#     except:
#         print('Ingresaste algo incorrecto. Vuelve a seleccionar una opción.')
#     else:
#         print('Pase por el else')
#     finally:
#         print('Pase por el finally')


def dividir(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'No puedes dividir por 0'
    except Exception:
        return 'Pase por el except'

    
print(dividir(5,'a'))
print(dividir(5,0))