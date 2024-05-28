class Cliente:
    def __init__(self, nombre, correo, direccion, telefono):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
        self.canasta = []
    
    def __str__(self):
        return f'''Cliente: {self.nombre} 
Dirección: {self.direccion}
Teléfono: {self.telefono}
                    '''
    
    def upDireccion(self, dirNueva):
        self.direccion = dirNueva
        print(f"La dirección de {self.nombre} ha sido actualizada a: {self.direccion}\n")
    
    def upTelefono(self,telNuevo):
        self.telefono = telNuevo
        print(f"El teléfono de {self.nombre} ha sido actualizado a: {self.telefono}\n")
    
    def añadirCanasta(self, articulo):
        self.canasta.append(articulo)
        
        print(f"{articulo} ha sido agregado al carrido de {self.nombre}")
    
    def verCanasta(self):
        print(f"\nCanasta de {self.nombre}")
        for articulo in self.canasta:
            print(f"- {articulo}")
        
        
    