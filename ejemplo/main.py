from NodoLista import Lista
from NodoLista3 import Lista3

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
l = Lista3()

global tree
tree = None

global f
f = None

global D

D = None


root = None


class dat1:

    Fichero = " "
    root = ""
    tree = " "
    f = ""


def Cargar():
    global f
    global D
    global tree
    crg = dat1()
    crg.Fichero = filedialog.askopenfilename(initialdir="/",
                                             filetypes=(
                                                 ("Text File", "*.xml"), ("All Files", "*.*")),
                                             title="Choose a file.")

    tree = ET.parse(crg.Fichero)
    root = tree.getroot()

    for datos in root:
        f = Lista_para_los_dato.Agregar(
            datos.attrib['nombre'], datos.attrib['n'], datos.attrib['m'])
        for s in datos:
            f.intento_matriz.Agregar_2(s.attrib['x'], s.attrib['y'], s.text)


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
        opcion = int(input('Ingrese una opcion ... '))
        if opcion == 1:
            Cargar()
            print('Los Datos se han cargado con exito!!')
        elif opcion == 2:

            print("")
            Lista_para_los_dato.Modelo()
            print('')
            Lista_para_los_dato.ModeloBinario()
            Lista_para_los_dato.VerFormaMatrizBinaria()
            print("")
            print("Lo siento lo intente :)")
            print("")
        elif opcion == 3:
            print("Lo siento lo intente :)")
        elif opcion == 4:
            print("")
            print("")
            print('> Heli saul Vasquez Gomez')
            print('> 201700852')
            print('> Introduccion a la programacion y computacion 2 seccion "D"')
            print('> Ingenieria en Sistemas')
            print('> 5to semestre')
            print("")
            print("")
        elif opcion == 5:

            Lista_para_los_dato.e()
        elif opcion == 6:
            exit
        else:
            print('Seleccione una Opcion Porfavor!')


Menu()
