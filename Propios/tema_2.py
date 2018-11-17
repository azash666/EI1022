from algoritmia.datastructures.queues import Fifo
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.utils import argmin

from Practicas.graph2dviewer import Graph2dViewer
from Practicas.labyrinthviewer import LabyrinthViewer
from Practicas.practica1 import create_labyrinth


def recorredor_vertices_anchura(grafo: "Graph<T>", v_inicial: "T") -> "List<T>":
    vertices = []
    queue =Fifo()
    seen = set()
    queue.push(v_inicial)
    seen.add(v_inicial)
    while len(queue)>0:
        v = queue.pop()
        vertices.append(v)
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push(suc)
    return vertices

def recorredor_aristas_anchura(grafo: "Graph<T>", v_inicial: "T") -> "List<T>":

    aristas = []
    queue = Fifo()
    seen = set()
    queue.push((v_inicial,v_inicial))
    seen.add(v_inicial)
    while len(queue)>0:
        u,v = queue.pop()
        aristas.append((u,v))
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v,suc))
    return aristas


def recorredor_vertices_profundidad(grafo: "Graph<T>", v_inicial: "T") -> "List<T>":
    def recorrido_desde(v):
        seen.add(v)
        vertices.append(v)
        for suc in grafo.succs(v):
            if suc not in seen:
                recorrido_desde(suc)


    seen = set()
    vertices = []
    recorrido_desde(v_inicial)
    return vertices


def recorredor_aristas_profundidad(grafo: "Graph<T>", v_inicial: "T") -> "List<T>":
    def recorrido_desde(u,v):
        seen.add(v)
        aristas.append((u,v))
        for suc in grafo.succs(v):
            if suc not in seen:
                recorrido_desde(v,suc)

    seen = set()
    aristas = []
    recorrido_desde(v_inicial, v_inicial)
    return aristas


def componentes_conexos(g: "UndirectedGraph<T>") -> "List<List<T>>":
    vertices_no_visitados=set(g.V)
    resultado = []
    while len(vertices_no_visitados)>0:
        u=vertices_no_visitados.pop()
        vertices_visitados = recorredor_aristas_anchura(g,u)
        vertices_no_visitados -= set(vertices_visitados)
        resultado.append(vertices_visitados)
    return resultado


def recuperador_camino(lista_aristas: "List<(T,T)>", v: "T") -> "List<T>":
    #Creamos diccionario de back pointers
    backPointers = {}
    for o,d in lista_aristas:
        backPointers[d]=o
    #Creamos un listado desde la salida, yendo hacia atrás
    camino = []
    camino.append(v)
    while backPointers[v]!= v:
        v=backPointers[v]
        camino.append(v)
    #Invertimos el camino
    camino.reverse()
    return camino


#Algoritmo de Dijkstra para hayar el camino mas corto desde un punto a otro en un grafo ponderado
def dijkstra(G: "Graph<T>", d: "(T,T)->Float", v_inicial: "T", v_final: "T") -> "List<(T,T)>":
    recorrido_aristas = []
    D = {}
    for v in G.V: D[v] = float("infinity")
    d[v_inicial] = 0
    in_fringe_from = {}
    in_fringe_from[v_inicial] = v_inicial
    added = set()
    while len(in_fringe_from)>0:
        v_destino = argmin(in_fringe_from.keys(), lambda  v: D[v])
        #Devuelve la key de cuyo D es menor
        added.add(v_destino)
        v_origen = in_fringe_from[v_destino]
        recorrido_aristas.append((v_origen, v_destino))
        del in_fringe_from[v_destino]
        if v_destino == v_final: break
        for w in G.succs(v_destino):
            if w not in added and D[v_destino] + d(v_destino, w)< D[w]:
                D[w] = D[v_destino] + d(v_destino, w)
                in_fringe_from[w] = v_destino
    return recorrido_aristas


def marca_pasos_desde(g: "UndirectedGraph<T>", v_entrada: "T") -> "Dictionary[Cells]->Int":
    CuentaPasos = {}
    CuentaPasos[v_entrada]=0
    #Seguimos el modelo de recorre_vertices_anchura
    queue = Fifo()
    seen = set()
    queue.push(v_entrada)
    seen.add(v_entrada)
    while len(queue)>0:
        v=queue.pop()
        for suc in g.succs(v):
            if suc not in seen:
                queue.push(suc)
                seen.add(suc)
                #Los pasos de esa casilla son uno más que los de su padre
                CuentaPasos[suc]=CuentaPasos[v]+1
    return CuentaPasos



if __name__ == "__main__":
    g = create_labyrinth(3,3)
    print(marca_pasos_desde(g,(0,0)))
    viewer = LabyrinthViewer(g, canvas_width=120, canvas_height=80, margin=5)
    viewer.run()