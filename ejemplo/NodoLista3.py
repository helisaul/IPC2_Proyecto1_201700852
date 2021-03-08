from Nodo3 import Nodo3_3
class Lista3:
    def __init__(self):
        self.inicio = None
        
    
    def tamanio(self):
        aux = self.inicio
        if aux is not None:
            return aux.tam

    

    def Agregar(self,contador,dato):
        datos = Nodo3_3(contador,dato)
        if self.inicio is not None:
            self.inicio = datos
        else:
            aux = self.inicio
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = datos
    
    def Mostra_Datos(self):
        aux = self.inicio
        while aux is not None:
            print(aux.dato,aux.contador)
            aux = aux.siguiente
