def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


original = "zsrmaq2wqmkmof2svqamowrodfmomaqw2aqodrm|" \
           "sgcofomsmeafesmnzofdabmzsrmeshmea1spoem|" \
           "a2msgcmea3odfj2ovmarwzoem2ovmsr2armsr a|" \
           "bm22zofdabmzsmaroddsqm ea1sdwpwqsdma2ms|" \
           "gcmazmddabmkmkmnealdsgtsdmeo1mg2m22aqab|" \
           "modswqsdobmwemoboesrmovmzods2sumadfesfe|" \
           "smsgcofomsfesmnarwqsdnaeoqodtmzomaro2sr2aqmo"
#original = reverse(original)
claveletras = "abcdefghijklmnopqrstuvwxyz0123456789 "


cantidad = {}
cantidad["|"]=0
for letra in claveletras:
    cantidad[letra]=0
for letra in original:
    cantidad[letra] += 1
for letra in claveletras:
    print(letra, cantidad[letra])

clave = {}
clave["a"] = "-"
clave["b"] = "-"
clave["c"] = "-"
clave["d"] = "-"
clave["e"] = "-"
clave["f"] = "0"
clave["g"] = "-"
clave["h"] = "-"
clave["i"] = "-"
clave["j"] = "-"
clave["k"] = "-"
clave["l"] = "-"
clave["m"] = " "
clave["n"] = "-"
clave["ñ"] = "-"
clave["o"] = "-"
clave["p"] = "-"
clave["q"] = "m"
clave["r"] = "-"
clave["s"] = "-"
clave["t"] = "-"
clave["u"] = "-"
clave["v"] = "-"
clave["w"] = "-"
clave["x"] = "-"
clave["y"] = "-"
clave["z"] = "-"
clave[" "] = "-"
clave["0"] = "-"
clave["1"] = "-"
clave["2"] = "l"
clave["3"] = "-"
clave["4"] = "-"
clave["5"] = "-"
clave["6"] = "-"
clave["7"] = "-"
clave["8"] = "-"
clave["9"] = "-"
clave["|"] = "\n"


solucion = ""
for letra in original:
    solucion += clave[letra]
print(solucion)



