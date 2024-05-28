from paqueteCliente.moduloCliente import Cliente

cliente1 = Cliente('Giovanni Francisco','giovannifrancisco.98.gf@gmail.com','Calle Siempre viva 742', '5523452310')

print(cliente1)

cliente1.upTelefono("5529382192")
cliente1.upDireccion("Calle Siempre Viva 749")

cliente1.añadirCanasta("Computadora")
cliente1.añadirCanasta("Mouse Gamer Inalámbrico")
cliente1.añadirCanasta("Silla Gamer")
cliente1.añadirCanasta("Monitor Curvo Gamer")

cliente1.verCanasta()