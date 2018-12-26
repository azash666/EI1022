def buscaPuntoFijo_rec(v):
    def rec(inicio: int, fin: int):
        if inicio - fin ==0: return None
        puntoMedio=(inicio+fin)//2
        if (puntoMedio == v[puntoMedio]):
            return puntoMedio
        if puntoMedio > v[puntoMedio]:
            return rec(puntoMedio, fin)
        return rec(inicio, puntoMedio)

    return rec(0,len(v))

def buscarPico_rec(v):
    def rec(ini: int, fin: int):
        if fin-ini==1: return ini
        medio = (ini+fin)//2
        if v[medio]<v[medio-1]:
            return rec(ini, medio)
        return rec (medio, fin)

    return rec(0,len(v))

def buscaSubVectorMaximo_rec(v):
    def rec(ini, fin):
        if fin-ini==1: return v[]
        medio=(ini+fin)//2
        mejorIzda = rec(ini,medio)
        mejorDcha = rec(medio, fin)
        sumaizda = []
        sumaDcha = []
        i=0
        while(i>medio-ini):



vector = [-1,1,3,4,6,7,8,34,36]
print(buscaPuntoFijo_rec(vector))
print(buscarPico_rec(vector))