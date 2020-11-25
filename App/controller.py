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

import config as cf
from App import model as m
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def iniciar_grafo():
    el_grafo=m.grafo_nuevo()
    return el_grafo
def iniciar_ref():
    la_ref=m.tabla_de_referencia()
    return la_ref
# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def loadTrips(analyzer):
    for filename in os.listdir(cf.data_dir):
        if filename.endswith('.csv'):
            print('Cargando archivo: ' + filename)
            loadFile(analyzer, filename)
    return analyzer

def loadFile(citibike, tripfile,reference):
    """
    """
    tripfile = cf.data_dir + tripfile
    input_file = csv.DictReader(open(tripfile, encoding="utf-8"),
                                delimiter=",")
    for trip in input_file:
        m.addTrip(reference["referencia"],reference["referencia_llegada"],citibike, trip)
    return citibike

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
def componentes_fuertemente_conectados(citybike):
    variable=m.numSCC(citybike,{})
    return variable

def retornar_arcos_y_vertices(citybike):
    vert=m.buscar_vertices(citybike)
    arc=m.buscar_arcos(citybike)
    return (vert,arc)

def retornar_vertices_en_cluster(sc,comp1,comp2):
    return m.sameCC(sc,comp1,comp2)

def retornar_estaciones_top_ingreso(graph,reference_table):
    return m.buscar_estaciones_top_ingreso(graph["grafo"],reference_table["referencia_llegada"])
def retornar_estaciones_top_llegada(graph,reference_table):
    return m.buscar_estaciones_top_llegada(graph["grafo"],reference_table["referencia"])
def retornar_estaciones_peor_top_llegada(graph,reference_table):
    return m.buscar_estaciones_top_llegada(graph["grafo"],reference_table["referencia_llegada"])

def Rutaresistencia(grafo,tiempo, estacion_inicio):
    r= m.resistencia(grafo,tiempo, estacion_inicio)
    return r

