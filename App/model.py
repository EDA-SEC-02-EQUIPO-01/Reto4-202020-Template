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
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.DataStructures import adjlist as adj
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Utils import error as error
assert config
import datetime

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
def tabla_de_referencia():
    ref={"referencia":None,
         "referencia_llegada":None,
         "rango_edad":None}
    ref["referencia"]=m.newMap(comparefunction=comparar_data)
    ref["referencia_llegada"]=m.newMap(comparefunction=comparar_data)
    ref["rango_edad"]=m.newMap(comparefunction=comparar_data)
    return ref


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

def addreference(referenfe_table,id,vertex):
    """agrega a una tabla de hash la informacion de un vertice
    tomando el id de la estacion como llave y crea una lista
    donde se guardara la informacion de los distintos viajes"""
    verificador=m.get(referenfe_table,id)
    if not verificador:
        lista=lt.newList()
        m.put(referenfe_table,id,lista)
    verificador=m.get(referenfe_table,id)
    dta_interna=me.getValue(verificador)
    lt.addLast(dta_interna,vertex)
    m.put(referenfe_table,id,dta_interna)  
    return referenfe_table   

def numSCC(graph, sc):
    sc = scc.KosarajuSCC(graph['grafo'])
    return (scc.connectedComponents(sc),sc)

def sameCC(sc, station1, station2):
    return scc.stronglyConnected(sc, station1, station2)

def buscar_vertices(graph):
    return gr.numVertices(graph['grafo'])

def buscar_arcos(graph):
    return gr.numEdges(graph['grafo'])





def addTrip(reference_tab,reference_tab_llegada,citibike, trip):
    """
    """
    origin = trip['start station id']
    destination = trip['end station id']
    duration = int(trip['tripduration'])
    addStation(citibike, origin)
    addStation(citibike, destination)
    addConnection(citibike, origin, destination, duration)
    addreference(reference_tab,origin,trip)
    addreference(reference_tab_llegada,destination,trip)

    


# Funciones para agregar informacion al grafo

# ==============================
# Funciones de consulta
# ==============================
def buscar_estaciones_top_ingreso(graph,reference_table):
    """"Funcion para hallar los viajes que llegan a una estacion!"""
    estaciones=lt.newList()
    vertices=gr.vertices(graph)
    it_vertice=it.newIterator(vertices)
    while it.hasNext(it_vertice):
        vert=it.next(it_vertice)
        estacion=gr.indegree(graph,vert)
        nombre=conversor_id_nombre(vert,reference_table)
        lt.addLast(estaciones,(estacion,nombre))
    merge.mergesort(estaciones,lessFunction)
    final_top=[]
    for i in range(3):
        top=lt.lastElement(estaciones)
        final_top.append(top)
        lt.removeLast(estaciones)
    return final_top


def buscar_estaciones_top_llegada(graph,reference_table):
    """"Funcion para hallar los viajes que llegan a una estacion!"""
    estaciones=lt.newList()
    vertices=gr.vertices(graph)
    it_vertice=it.newIterator(vertices)
    while it.hasNext(it_vertice):
        vert=it.next(it_vertice)
        estacion=gr.outdegree(graph,vert)
        
        lt.addLast(estaciones,(estacion,vert))
    merge.mergesort(estaciones,lessFunction)
    final_top=[]
    for i in range(3):
        top=lt.lastElement(estaciones)
        nombre=conversor_id_nombre(top[1],reference_table,"start station name")
        final_top.append((top[0],nombre))
        lt.removeLast(estaciones)

    return final_top

def buscar_estaciones_peor_top(graph,reference_table):
    """"Funcion para hallar los viajes que llegan a una estacion!"""
    estaciones=lt.newList()
    vertices=gr.vertices(graph)
    it_vertice=it.newIterator(vertices)
    while it.hasNext(it_vertice):
        vert=it.next(it_vertice)
        estacion=gr.indegree(graph,vert)
        estacion+=gr.outdegree(graph,vert)
        lt.addLast(estaciones,(estacion,vert))
    merge.mergesort(estaciones,lessFunction)
    final_top=[]
    for i in range(3):
        top=lt.firstElement(estaciones)
        nombre=conversor_id_nombre(top[1],reference_table,"end station name")
        final_top.append((top[0],nombre))
        lt.removeFirst(estaciones)
    return final_top



    
def conversor_id_nombre(id,reference_table,value="end station name"):
    reference=m.get(reference_table,id)
    data=me.getValue(reference)
    item=lt.firstElement(data)
    return item[value]


def resistencia(graph,tiempo, estacion_inicio):
    rutas= lt.newList(comparar_data)
    borrar= lt.newList(comparar_data)
    estaciones = adj.adjacents(graph['grafo'],estacion_inicio)
    ite = it.newIterator(estaciones)
    no_repetir= m.newMap(numelements=17, prime=109345121, 
                                maptype='CHAINING', loadfactor=0.5, 
                                comparefunction=comparar_data)
    m.put(no_repetir,estacion_inicio,1)
    while (it.hasNext(ite)):
        est = it.next(ite)
        edg = adj.getEdge(graph['grafo'],estacion_inicio,est)
        duracion= edg["weight"]
        if duracion < (tiempo*60) and m.contains(no_repetir,est)==False:
            ruta={}
            ruta["Estacion_final"]=est
            ruta["Estacion_inicio"]= estacion_inicio
            ruta["tiempo"]= duracion
            lt.addLast(rutas,ruta)
            lt.addLast(borrar,ruta)
            m.put(no_repetir,est,1)
    ite2=it.newIterator(borrar)
    while (it.hasNext(ite2)):
        est2 = it.next(ite2)
        estaciones2 = adj.adjacents(graph['grafo'],est2["Estacion_final"])
        ite3=it.newIterator(estaciones2)
        while (it.hasNext(ite3)):
            est3 = it.next(ite3)
            edg2 = adj.getEdge(graph['grafo'],est2["Estacion_final"],est3)
            if m.contains(no_repetir,est3)==False:
                if "Tiempo_acumulado" not in est2.keys():
                    tiempo_acumulado= edg2["weight"]+est2["tiempo"]
                    if tiempo_acumulado < (tiempo*60):
                        ruta={}
                        ruta["Estacion_final"]= est3
                        ruta["Estacion_inicio"]= est2["Estacion_final"]
                        ruta["tiempo"]= edg2["weight"]
                        ruta["tiempo_acumulado"]= tiempo_acumulado
                        lt.addLast(rutas,ruta)
                        lt.addLast(borrar,ruta)
                        m.put(no_repetir,est3,1)
                else:
                    tiempo_acumulado= edg2["weight"]+est2["tiempo_acumulado"]
                    if tiempo_acumulado < (tiempo*60):
                        ruta={}
                        ruta["Estacion_final"]= est3
                        ruta["Estacion_inicio"]= est2["Estacion_final"]
                        ruta["tiempo"]= edg2["weight"]
                        ruta["tiempo_acumulado"]= tiempo_acumulado
                        lt.addLast(rutas,ruta)
                        lt.addLast(borrar,ruta)
                        m.put(no_repetir,est3,1)
            lt.removeFirst(borrar)         
    return rutas

def Camino_corto (graph,est1,est2):
    disk=djk.Dijkstra(graph,est1)
    alter=djk.initSearch(graph,est1)
    cam=djk.pathTo(alter,est2)
    
    return cam

def ruta_de_interes(graph,ref_table_llegada,coor1,coor2,coor_destino_1,coor_destino_2):
    vertex_list=gr.vertices(graph)
    it_vertice=it.newIterator(vertex_list)
    valor_referencia=10
    valor_referencia2=10
    nombre_estacion_cercana=0
    nombre_destino_cercano=0
    id_estacion_inicial=0
    id_estacion_final=0
    while it.hasNext(it_vertice):
        vert=it.next(it_vertice)
        coor_origen_1=extractor_de_datos(vert,ref_table_llegada,"end station latitude")
        coor_origen_2=extractor_de_datos(vert,ref_table_llegada,"end station longitude")
        cercania_latitud=abs(float(coor_origen_1[0])-coor1)
        cercania_longitud=abs(float(coor_origen_2[0])-coor2)
                   
        if (cercania_latitud+cercania_longitud)<valor_referencia:
            valor_referencia=cercania_latitud+cercania_longitud
            nombre_estacion_cercana=coor_origen_1[1]
            id_estacion_inicial=vert
        
        cercania_latitud_final=abs(float(coor_origen_1[0])-coor_destino_1)
        cercania_longitud_final=abs(float(coor_origen_2[0])-coor_destino_2)

        if (cercania_latitud_final+cercania_longitud_final)<valor_referencia2:
            valor_referencia2=cercania_latitud+cercania_longitud
            nombre_destino_cercano=coor_origen_1[1]
            id_estacion_final=vert

    pila_estacion=Camino_corto(graph,id_estacion_inicial,id_estacion_final)

    return(nombre_estacion_cercana,nombre_destino_cercano)


def busca_caminos(graph,vert1,vert2):
    pass




def extractor_de_datos(id,ref_table,valor_extraible):
    valor=m.get(ref_table,id)
    new_data=me.getValue(valor)
    info=lt.firstElement(new_data)
    return (info[valor_extraible],info["end station name"])

def identificador_de_bicicletas_mantenimiento(graph,ref_table,bikeid,fecha):
    vertices=gr.vertices(graph)
    it_vertice=it.newIterator(vertices)
    conv2=datetime.datetime.strptime(fecha,"%Y-%m-%d")
    lista_estaciones=[]
    time_value=0
    while it.hasNext(it_vertice):
        vert=it.next(it_vertice)
        data_viaje=extractor_de_datos(vert,ref_table,"bikeid")
        if data_viaje[0]==bikeid:
            fecha_viaje=extractor_de_datos(vert,ref_table,"starttime")
            conv1=datetime.datetime.strptime(fecha_viaje[0],"%Y-%m-%d %H:%M:%S.%f")
            juan=conv1.date()
            if conv1.date()==conv2.date():
                estacion=extractor_de_datos(vert,ref_table,"start station name")
                time_value=+int(extractor_de_datos(vert,ref_table,"tripduration")[0])
                if estacion[0] not in lista_estaciones:
                    lista_estaciones.append(estacion[0])
                if estacion[1] not in lista_estaciones:
                    lista_estaciones.append(estacion[1])
    return (time_value,86400-time_value,lista_estaciones)




# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion
# ==============================
def comparar_data(route1,route2):
    r2=route2["key"]
    if (int(route1) == int(r2)):
        return 0
    elif (int(route1) > int(r2)):
        return 1
    else:
        return -1

def comparar_ref(keyname,genero):
    """
    Compara dos referencias, el primero es una cadena. 
    El segundo es entry de un map
    """
    genre=me.getKey(genero)
    if (keyname == genre):
        return 0
    elif (keyname > genre):
        return 1
    else:
        return -1

def lessFunction(item1,item2):
    if item1<item2:
        return True
    return False
