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
from DISClib.DataStructures import listiterator as it
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
    print("8- Requerimiento 6")
    print("9- Requerimiento 7")
    print("10- Requerimiento 8")
    print("0- Salir")
    

def imprimir_rutas_req4(cont,tiempo,estacion):
    rutas = controller.Rutaresistencia(cont,tiempo,estacion)
    ite= it.newIterator(rutas)
    while it.hasNext(ite):
        rut=it.next(ite)
        inicio=rut["Estacion_inicio"]
        final=rut["Estacion_final"]
        time= round((rut["tiempo"]/60),2)
        print(f"Puede tomar la estación {inicio} hasta la estación {final} con un tiempo estimado de {time} minutos")

while True:
    printMenu()
    entrada=input("Seleccione una opcion pra continuar\n")

    if int(entrada)==1:
        print("Inicializando...\n")
        time1= process_time()
        cont=controller.iniciar_grafo()
        ref=controller.iniciar_ref()
        time2=process_time()
        print(f"Tiempo de ejecucion: {time2-time1} segundos")
    elif int(entrada)==2:
        print("Inicializando...\n")
        time1= process_time()
        controller.loadFile(cont,ruta1,ref)
        #controller.loadFile(cont,ruta2)
        #controller.loadFile(cont,ruta3)
        #controller.loadFile(cont,ruta4)
        total=controller.retornar_arcos_y_vertices(cont)
        csc=controller.componentes_fuertemente_conectados(cont)
        time2=process_time()
        print(f"Tiempo de ejecucion: {time2-time1} segundos")
        print(f"Vertices: {total[0]}\nArcos: {total[1]}\nComponentes fuertemente conectados: {csc[0]}")
        componente1=input(f"Ingrese la primera estacion que desea saber si esta en el cluster:\n")
        componente2=input(f"Ingrese la segunda estacion que desea saber si esta en el cluster:\n")
        print(f"{controller.retornar_vertices_en_cluster(csc[1],componente1,componente2)}")
    elif int(entrada)==5:
        time1=process_time()
        top_llegada=controller.retornar_estaciones_top_ingreso(cont,ref)
        top_salida=controller.retornar_estaciones_top_llegada(cont,ref)
        peor_top=controller.retornar_estaciones_peor_top_llegada(cont,ref)
        time2=process_time()
        print(f"Top 3 estaciones con mas llegadas:\n{top_llegada}\nTop 3 estaciones con mas salidas\n{top_salida}\nTop 3 estaciones menos visitadas\n{peor_top}\nTiempo de ejecucion: {time2-time1} segundos")
    elif int(entrada)==6:
        time1= process_time()
        tiempo= int(input("Ingrese el tiempo maximo de resistencia (minutos): "))
        estacion= input("Ingrese la estación de ID de la estación de partida: ")
        imprimir_rutas_req4(cont,tiempo,estacion)
        time2=process_time()
    elif int(entrada)==8:
        coor1=float(input("Ingrese la latidud de su posicion actual\n"))
        coor2=float(input("Ingrese la longitud de su posicion actual\n"))
        coor3=float(input("Ingrese la latidud de su destino\n"))
        coor4=float(input("Ingrese la longitud de su destino\n"))
        datz=controller.retornar_ruta_de_interes(cont,ref,coor1,coor2,coor3,coor4)
        print(datz)
    elif int(entrada)==9:
            pass
    elif int(entrada)==10:
        bikeid=input("Ingrese el ID de bicicleta\n")
        fecha=input("Ingrese la fecha de la que desea averiguar los viajes:(utilice el formato YY-MM-DD)\n")
        lista=controller.retornar_identificador_de_bicicletas_mantenimiento(cont,ref,bikeid,fecha)
        print(f"Segundos totales de uso:{lista[0]}\nSegundos totales de receso:{lista[1]}\nLista de estaciones por las que el usuario {bikeid} ha pasado:\n")
        for g in lista[2]:
            print(g)
    elif int(entrada)==0:
        break

