from Nodo2 import Nodo2_2


class Lista2:

    def __init__(self):
        self.inicio = None

    def Agregar_2(self, x, y, numero):

        dato2 = Nodo2_2(x, y, numero)

        if self.inicio is None:
            self.inicio = dato2
        else:
            aux = self.inicio
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = dato2

    def MostrarD(self):
        aux = self.inicio
        while aux is not None:
            print(' x : ', str(aux.x), ' y :', str(
                aux.y), ' valor :', str(aux.numero))
            aux = aux.siguiente

    def Simular_Matriz(self, n, m):
        aux = self.inicio
        while aux is not None:
            if (aux.x == str(n)) and (aux.y == str(m)):
                return aux.numero
            aux = aux.siguiente
        return None

    def Simular_Matriz2(self, n, m):
        aux = self.inicio
        while aux is not None:
            if (aux.x == (n)) and (aux.y == (m)):
                return (aux.numero)
            if aux.siguiente == None:
                break
            else:
                aux =aux.siguiente
        return None

    def matriz_prueba(self, n, m):
        aux = self.inicio
        while aux is not None:
            if (aux.x == str(n) and (aux.y == str(m))):
                if aux.numero >= str(aux.Binario2):    #Binario2 = 1
                    return aux.Binario2                #Binario = 0
                if aux.numero < str(aux.Binario2):
                    return aux.Binario
            aux = aux.siguiente
        return None
