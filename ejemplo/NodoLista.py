from Nodo import Nodo_1
class Lista:

    def __init__(self):
        self.inicio = None
        self.final = None

    
    def Agregar(self,numero,x,y):
        dato = Nodo_1(numero,x,x)
        if self.inicio is None:
           self.inicio = dato
           return dato

        else:
            aux = self.inicio
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = dato
            dato.anterior = aux
            return dato
        return None

    
    def MostrarDatos(self):
        aux = self.inicio
        while aux is not None:
            print('[','Numero: ', aux.numero, 'X : ', aux.x ,'Y : ',aux.y,']')
           # print('Cursos:')
            #aux.cursos.MostrarCursos()
            print('---------------------------')
            aux = aux.siguiente