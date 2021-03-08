from Nodo import Nodo_1
from graphviz import Digraph


class Lista:

    def __init__(self):
        self.inicio = None
        self.final = None

    def Agregar(self, nombre, n, m):
        dato = Nodo_1(nombre, n, m)
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
            print('[', 'Numero: ', str(aux.nombre),
                  'n : ', aux.n, 'm : ', aux.m, ']')
            # print('Cursos:')
            aux.intento_matriz.MostrarD()
            print('---------------------------')
            aux = aux.siguiente

    def Modelo(self):
        aux = self.inicio
        a = int(aux.n)
        b = int(aux.m)
        if aux is not None:
            print('--------', aux.nombre, '---------')
            print('---------------------------')

            for i in range(0, a):
                p = ''
                for j in range(0, b):

                    p = p + \
                        str(aux.intento_matriz.Simular_Matriz((i+1), (j+1))) + "\t"
                print(p)
            print('---------------------------')

    def ModeloBinario(self):
        aux = self.inicio
        a = int(aux.n)
        b = int(aux.m)
        if aux is not None:
            for i in range(0, a):
                for j in range(0, b):
                    identidad = 1
                    f = (aux.intento_matriz.Simular_Matriz((i+1), (j+1)))
                    if int(f) >= identidad:
                        str(aux.FormaBinaria.Agregar_2(i+1, j+1, identidad))
                    identidad2 = 0
                    if int(f) < identidad:
                        str(aux.FormaBinaria.Agregar_2(i+1, j+1, identidad2))
            # aux.FormaBinaria.MostrarD()

    def VerFormaMatrizBinaria(self):
        aux = self.inicio
        a = int(aux.n)
        b = int(aux.m)
        if aux is not None:
            print("-------Matriz Binaria-------")
            for i in range(0, a):
                B = ""
                for j in range(0, b):
                    B = B + \
                        str(aux.FormaBinaria.Simular_Matriz2((i+1), (j+1)))+"\t"
                print(B)
            print("----------------------------")

    def Buscar_Patrones(self):
        aux = self.inicio
        a = int(aux.n)
        b = int(aux.m)
        contG = 1
        if aux is not None:
         for fila  in range(0,a-1):
             comparacion = True
             if int(aux.Patrones.tamanio()) > 0:
                 for rtx in aux.Patrones.tamanio(): 
                   if rtx[1] == fila+1:
                    comparacion = False

             if comparacion:
                aux.Patrones.Agregar(contG,fila+1)
                for filC in range(fila+1, a): #1
                    #print("fila compara")
                    esIgual = True
                    for col in range (0,b):
                        #print("col compara")
                        if not (aux.FormaBinaria.Simular_Matriz(fila+1, col+1) == aux.FormaBinaria.Simular_Matriz(filC+1, col+1)):
                            esIgual = False
                    if esIgual:
                        aux.Patrones.Agregar(contG,filC+1)
                contG += 1
         if int(aux.Patrones.tamanio()) > 0:
            seAlmacena = True
            for gr in aux.Patrones.getSize(): #[[1,1],[1,2]]
            #print("ultima fila")
                if gr[1] == a:
                 seAlmacena = False
            if seAlmacena:
             aux.Patrones.Agregar(contG,a)
         print(aux.Patrones.Mostra_Datos())
   
    
    
    
    
    '''
    def gra(self):
         aux = self.inicio

         if aux is not None:
             w = Digraph()filC+1
             w.edges((aux.nombre, str(i)) for i in range(1, 10))
             w.view()
    '''
    

    def e(self):
        aux = self.inicio
        a = int(aux.n)
        b = int(aux.m)
        if aux is not None:
            dot = Digraph(comment='The Round Table')
            dot.node('A', aux.nombre)
            dot.node('B', aux.n)
            dot.node('L', aux.m)
            dot.edges(['AB', 'AL'])
            for i in range(0, a):
                p = ""
                for j in range(0, b):
                    p = p + \
                        str(aux.intento_matriz.Simular_Matriz(i+1, j+1)) + "\t"
                dot.node(p)

            #dot.edge('B', 'L', constraint='false')
            dot.render('test-output/round-table.gv', view=True)
