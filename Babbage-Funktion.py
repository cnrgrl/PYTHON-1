#Aufgabe 12: Babbage-Funktion

f=0
for n in range(1,20,1):
    f=n*n+n+41
    print(f,end='-')

    #second version table format

    def babbage(x):
   #Wert der Babbage-Funktion für x 
        return (x * x) + x + 41

def babbage_im_Intervall_bis(n):
  for x in range(1, n+1):
   print (f'{x:2d} {babbage(x):3d}')

# Funktionsaufruf
# babbage_im_Intervall_bis(20)