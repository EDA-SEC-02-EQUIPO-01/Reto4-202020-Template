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
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------
def grafo_nuevo():
    citybike={"grafo":None}
    citybike["grafo"] = gr.newGraph(datastructure='ADJ_LIST',
                                  directed=True,
                                  size=1000,
                                  comparefunction=comparar_data)
    return citybike

def addStation(citibike, stationid):
    """
    Adiciona una estación como un vertice del grafo
    """
    if not gr.containsVertex(citibike["grafo"], stationid):
        gr.insertVertex(citibike["grafo"], stationid)
    return citibike

def addConnection(citibike, origin, destination, duration):
    """
    Adiciona un arco entre dos estaciones
    """
    edge = gr.getEdge(citibike["grafo"], origin, destination)
    if edge is None:
        gr.addEdge(citibike["grafo"], origin, destination, duration)
    return citibike

def numSCC(graph, sc):
    sc = scc.KosarajuSCC(graph['grafo'])
    return scc.connectedComponents(sc)

def sameCC(sc, station1, station2):
    return scc.stronglyConnected(sc, station1, station2)

def buscar_vertices(graph):
    return gr.numVertices(graph['grafo'])

def buscar_arcos(graph):
    return gr.numEdges(graph['grafo'])





def addTrip(citibike, trip):
    """
    """
    origin = trip['start station id']
    destination = trip['end station id']
    duration = int(trip['tripduration'])
    addStation(citibike, origin)
    addStation(citibike, destination)
    addConnection(citibike, origin, destination, duration)

    


# Funciones para agregar informacion al grafo

# ==============================
# Funciones de consulta
# ==============================

# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion
# ==============================
def comparar_data(route1,route2):
    r2=route2["key"]
    if (route1 == r2):
        return 0
    elif (route1 > r2):
        return 1
    else:
        return -1
