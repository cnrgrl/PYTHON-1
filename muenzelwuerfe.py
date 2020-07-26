import random

einsatz = 5
gewinn = 40
fail = 0
flip_n = 0
tage = 0
gewin_tage = 0

for i in range(1, 1001):
    while fail < einsatz < gewinn:
        wurfen = random.choice([True, False])
        if wurfen == False:
            einsatz -= 1
        else:
            einsatz += 1

        flip_n +=1
    if einsatz == gewinn:
        tage += 1
        gewin_tage += 1
    elif einsatz == fail:
        tage += 1
    einsatz = 5



'''if einsatz == gewinn:
    print("WOOOOw DU HAST GEWON!!")
elif einsatz == fail:
    print("Sorry sie mussen RAUS!!")'''

print("Wurf zahl: ",flip_n)
print(tage)
print(gewin_tage)
prozent=float(gewin_tage/tage)
print(prozent)