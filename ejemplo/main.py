from NodoLista import Lista

import tkinter as tk
from tkinter import filedialog
from io import open
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as ET

root = tk.Tk()
root.withdraw()
Lista_para_los_dato = Lista()
Lista_para_los_dato2 = Lista()

global tree
tree = None

global f
f = None

global D

D  =None



class  dat1:
    
    Fichero = " "
    root = ""
    tree = " "
    f = ""
    
  




def Cargar():
    global f
    global D
    global tree
    crg = dat1()
    crg.Fichero = filedialog.askopenfilename(initialdir = "/",
                           filetypes = (("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file.")
    

    tree = ET.parse(crg.Fichero)
    D = tree.getroot()
    
    for datos in D:
        if datos.attrib['nombre'] == 'MatrizPrueba1':
            for subdatos in datos:
             f = Lista_para_los_dato.Agregar(subdatos.text,subdatos.attrib['x'],subdatos.attrib['y'])
        
        elif datos.attrib['nombre'] == 'MatrizPrueba2':
                for subdatos in datos:
                 f = Lista_para_los_dato2.Agregar(subdatos.text,subdatos.attrib['x'],subdatos.attrib['y'])
             
    



def Menu():
   
    c = dat1()
    global f
    global tree
    global D

    
    
    opcion = 0
    while opcion != 6:
        print('Menu Principal')
        print('    1.Cargar Archivo')
        print('    2.Procesar Archivo')
        print('    3.Escribir Archivo de Salida')
        print('    4.Mostrar Datos del Estudinate')
        print('    5.Generar Grafica')
        print('    6.Salir')

        opcion = int (input('Ingrese una opcion ... ')) 

        if opcion == 1:
         Cargar()
         print('Los Datos se han cargado con exito!!')
        elif opcion == 2:
         
           for datos in D:
            if datos.attrib['nombre'] == 'MatrizPrueba1':
             for subdatos in datos:
                 f.intento_matriz.Agregar_2(subdatos.text)
        
            elif datos.attrib['nombre'] == 'MatrizPrueba2':
                for subdatos in datos:
                    f.intento_matriz.Agregar_2(subdatos.text)
                   
           
           
          
        elif opcion == 3:
          f.intento_matriz.matriz_prueba()
        elif opcion == 4:
           print('hola 4')
        elif opcion == 5:
          print('hola 5')
        elif opcion == 6:
            exit
        else:
            print('Seleccione una Opcion Porfavor!')


Menu()