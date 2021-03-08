from NodoLista2 import Lista2
from NodoLista3 import Lista3
class Nodo_1:
    def __init__(self, nombre, n, m):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.matriz = "Matriz Binaria"
        self.intento_matriz = Lista2()
        self.FormaBinaria = Lista2()
        self.Patrones = Lista3()
        self.siguiente = None
        self.utimo = None
    def mostrar(self):
        self.intento_matriz.MostrarD()
