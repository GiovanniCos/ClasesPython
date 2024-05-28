bd_usrs = {}

def registrar(registros):
    usr = input("Ingrese el nombre del usuario a registrar: ")
    pswd = input("Ingrese su contraseña: ")
    if usr in registros:
        print("El nombre de usuario ya ha sido registrado, vuelva a intentarlo con un nombre de usuario distinto. \n")
    else:
        registros[usr] = pswd
        print("El registro del usuario "+ usr + " ha sido correcto")
        print("\n")

def mostrarInfo(registros):
    print("¡Para mostrar toda la información debes tener derechos de administrador!")
    admn = input("Ingrese la clave del administrador: ")
    if admn == "admin":
        for usuario in registros:
            print("Usuario: " f'{usuario}: "Contraseña: " {registros[usuario]}')
        print("\n")

def acceso(registros):
    usr = input("Ingrese su nombre de usuario: ")
    if usr not in registros:
        print("El usuario " + usr + " no se encuentra registrado. Vuelva a intentarlo o en su defecto, registrarse.\n")
    else:
        pswd = input("Ingrese su contraseña: ")
        if pswd == registros[usr]:
            print("El inicio de sesión ha sido correcto!!\n")
        else:
            print("La contraseña es incorrecta, vuelva a intentarlo.\n")
            
salir = True
while salir:
    print("Seleccione una opción:")
    print("1.- Registrar usuario")
    print("2.- Iniciar Sesión")
    print("3.- Mostrar información")
    print("4.- Salir")
    opc = input("Ingrese la opción: ")
    
    if opc == '1':
        registrar(bd_usrs)
    elif opc == '2':
        acceso(bd_usrs)
    elif opc == '3':
        mostrarInfo(bd_usrs)
    elif opc == '4':
        salir = False
        print("Ha salido")
    else:
        print("Valor no reconocido, vuelva a intentarlo.\n")
    