import random

einsatz = 5
gewinn = 25
fail = 0
flip_n = 0
tage = 0
gewin_tage = 0

for i in range(1, 10001):
    while fail < einsatz < gewinn:
        wurfen = random.choice([True, False])
        if wurfen == False:
            einsatz -= 1
        else:
            einsatz += 1
        flip_n +=1
        hintereinander=0
        while hintereinander<10:

            if einsatz == gewinn:
                 tage += 1
                 gewin_tage += 1
                 hintereinander+=1

            elif einsatz == fail:
                tage += 1
                hintereinander=0
    einsatz = 5



'''if einsatz == gewinn:
    print("WOOOOw DU HAST GEWON!!")
elif einsatz == fail:
    print("Sorry sie mussen RAUS!!")'''
print("#######################")
print("Wurf zahl: ",flip_n)
print(tage)
print(gewin_tage)
prozent=float(gewin_tage/tage)
print(prozent)
print(hintereinander)