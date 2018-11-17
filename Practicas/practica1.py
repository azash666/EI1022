from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
import random

from Practicas.labyrinthviewer import LabyrinthViewer


def create_labyrinth(rows, cols):
    vertices = [(r, c) for r in range(rows) for c in range(cols)]
    mfs = MergeFindSet()
    for v in vertices:
        mfs.add(v)

    edges = []
    for (r ,c) in vertices:
        if r+1<rows:
            edges.append(((r,c),(r+1,c)))
        if c+1<cols:
            edges.append(((r,c),(r,c+1)))

    random.shuffle(edges)

    corridors = []

    for (u,v) in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u,v)
            corridors.append((u,v))

    return UndirectedGraph(E=corridors)


def path(g: "UndirectedGraph<T>", v_entrada: "T", v_salida: "T") -> "List<(T,T)>":
    #Primero creo una lista de aristas:
    def recorrido_desde(u,v):
        seen.add(v)
        aristas.append((u,v))
        for suc in g.succs(v):
            if suc not in seen:
                recorrido_desde(v, suc)
    aristas = []
    seen = set()
    recorrido_desde(v_entrada, v_entrada)

    #Segundo creo un diccionario de BackPointers:
    bp = {}
    for (u,v) in aristas:
        bp[v] = u

    #Recorremos el laberinto desde la salida:
    camino = []
    v=v_salida
    camino.append(v)
    while bp[v]!=v:
        v=bp[v]
        camino.append(v)

    #Le damos la vuelta al camino
    camino.reverse()
    return camino



if __name__ == '__main__':
    cols = 2
    rows = 2
    lab = create_labyrinth(rows,cols)
    pato = path(lab, (0,0), (rows-1,cols-1))
    viewer = LabyrinthViewer(lab, canvas_width=1200, canvas_height=800, margin=10)
    viewer.add_path(pato, "#0000ff")
    viewer.run()