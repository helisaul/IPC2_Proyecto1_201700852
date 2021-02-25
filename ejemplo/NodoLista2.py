from Nodo2 import Nodo2_2
class Lista2:

    def __init__(self):
        self.inicio = None
    

    def Agregar_2(self,numero):

        dato2 =Nodo2_2(numero)

        if self.inicio is None:
            self.inicio = dato2
        else:
            aux = self.inicio
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = dato2

    def MostrarCursos(self):
        aux = self.inicio
        while aux is not None:
            print(' Numero : ', aux.numero)
            aux = aux.siguiente

    
    def matriz_prueba(self):
        aux = self.inicio
        while aux is not None:
            for c in aux.numero:
                if int (c) > 1:
                    aux.numero = 1
                print(aux.numero)
                aux = aux.siguiente

    

