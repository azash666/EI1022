import time

tiempo = time.time()
nuevoTiempo = time.time()
i=0
while(time.time()<tiempo+60):
    i+=1
print (i/60)
