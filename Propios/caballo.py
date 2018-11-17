from copy import deepcopy

from bt_scheme import PartialSolution, BacktrackingSolver, State, Solution
from typing import *
from random import random, seed

def horse_solve(tablero: "List[Tuple[int, int], ...]"):
    class KnapsackPS(PartialSolution):
        #def __init__(self, solucionParcial: Tuple[int, ...], valorActual: int, pesoActual: int):         # IMPLEMENTAR: Añade los parámetros que tú consideres
        def __init__(self, solucion: Tuple[Tuple[int, int], ...], x: int, y: int):  # IMPLEMENTAR: Añade los parámetros que tú consideres

            self.solucion = solucion
            self.x = x
            self.y = y
            self.n = len(self.solucion)

        def is_solution(self) -> bool:      # IMPLEMENTAR
            return self.n==len(tablero) and (0,0) in self.getSiguientes()

        def get_solution(self) -> Solution: # IMPLEMENTAR
            return self.solucion

        def successors(self) -> Iterable["KnapsackPS"]:# IMPLEMENTAR
            if not self.is_solution():
                for pos in self.getSiguientes():
                    if pos in tablero and pos not in self.solucion:
                        if self.noDisjunto(pos):
                            yield KnapsackPS(self.solucion+(pos,), pos[0], pos[1])

        def getSiguientes(self):
            return [(self.x-1, self.y-2),(self.x-2, self.y-1),(self.x-1, self.y+2),(self.x-2, self.y+1),(self.x+1, self.y-2),(self.x+2, self.y-1),(self.x+1, self.y+2),(self.x+2, self.y+1)]

        def noDisjunto(self, pos):
            if len(self.solucion)+1 is len(tablero): return True
            for i in tablero:
                if i not in self.solucion+(pos,):
                    aux=i
                    break
            suma=1
            vertices = []
            queue = []
            seen = set()
            queue.append(aux)
            seen.add(aux)
            while len(queue) > 0:
                v = queue[0]
                suma+=1
                queue.remove(v)
                vertices.append(v)
                for suc in self.getSiguientes2(v[0], v[1]):
                    if suc not in seen and suc != pos and suc not in self.solucion and suc in tablero:
                        seen.add(suc)
                        queue.append(suc)
            return (suma + self.n) == len(tablero)



        def getSiguientes2(self,x, y):
            return [(x-1, y-2),(x-2, y-1),(x-1, y+2),(x-2, y+1),(x+1, y-2),(x+2, y-1),(x+1, y+2),(x+2, y+1)]



    initialPS = KnapsackPS(((0,0),), 0, 0)                # IMPLEMENTAR: Añade los parámetros que tú consideres
    return BacktrackingSolver.solve(initialPS)




# Programa principal ------------------------------------------
if __name__ == "__main__":
    tablero = ()
    for i in range(8):
        for j in range(8):
            tablero = tablero + ((i,j),)
    print(tablero)
    print("\n<SOLUCIONES>")
    ficheroF = open("Caballos.txt", "w")
    for sol in horse_solve(tablero):
        print (sol)
        ficheroF.write(str(sol))
        ficheroF.write("\n")
    print("\n<TERMINADO>")
