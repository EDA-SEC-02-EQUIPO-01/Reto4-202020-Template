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
        m.addTrip(reference["referencia"],reference["referencia_llegada"],reference["referencia_estaciones"],citibike, trip)
    grafo_final=m.conections(citibike,reference)
    return grafo_final

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
    return m.buscar_estaciones_peor_top(graph["grafo"],reference_table["referencia_llegada"])

def Rutaresistencia(grafo,tiempo, estacion_inicio):
    r= m.resistencia(grafo,tiempo, estacion_inicio)
    return r

def retornar_ruta_de_interes(graph,ref_table_llegada,coor1,coor2,coor_destino_1,coor_destino_2):
    r=m.ruta_de_interes(graph["grafo"],ref_table_llegada["referencia_llegada"],coor1,coor2,coor_destino_1,coor_destino_2)
    return r

def retornar_identificador_de_bicicletas_mantenimiento(graph,ref_table,bikeid,fecha):
    return m.identificador_de_bicicletas_mantenimiento(graph["grafo"],ref_table["referencia_llegada"],bikeid,fecha)

def retornar_ruta_circula(graph,ref_table,tiempo,id_estacion):
    return m.ruta_circula(graph["grafo"],ref_table["referencia_llegada"],tiempo,id_estacion)

def recomendador_de_rutas(grafo,ref,rango):
    r=m.Recomendador_de_Rutas(grafo,ref,rango)
    return r

def Identificacion_de_estaciones_para_publicidad(graph,ref,rango):
    r=m.estaciones_para_publicidad(graph,ref,rango)
    return r
