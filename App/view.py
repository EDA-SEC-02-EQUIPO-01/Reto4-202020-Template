"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config
from time import process_time

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________

ruta1="201801-1-citibike-tripdata.csv"
ruta2="201801-2-citibike-tripdata.csv"
ruta3="201801-3-citibike-tripdata.csv"
ruta4="201801-4-citibike-tripdata.csv"
# ___________________________________________________
#  Menu principal
# ___________________________________________________

"""
Menu principal
"""
def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Crear analizador")
    print("2- Cargar informacion")
    print("3- Requerimiento 1")
    print("4- Requerimiento 2")
    print("5- Requerimiento 3")
    print("6- Requerimiento 4")
    print("7- Requerimiento 5")
    print("0- Salir")
    

while True:
    printMenu()
    entrada=input("Seleccione una opcion pra continuar\n")

    if int(entrada[0])==1:
        print("Inicializando...\n")
        time1= process_time()
        cont=controller.iniciar_grafo()
        time2=process_time()
        print(f"Tiempo de ejecucion: {time2-time1} segundos")
    elif int(entrada[0])==2:
        print("Inicializando...\n")
        time1= process_time()
        controller.loadFile(cont,ruta1)
        controller.loadFile(cont,ruta2)
        controller.loadFile(cont,ruta3)
        controller.loadFile(cont,ruta4)
        total=controller.retornar_arcos_y_vertices(cont)
        csc=controller.componentes_fuertemente_conectados(cont)
        time2=process_time()
        print(f"Tiempo de ejecucion: {time2-time1} segundos")
        print(f"Vertices: {total[0]}\nArcos: {total[1]}\nComponentes fuertemente conectados: {csc}")
