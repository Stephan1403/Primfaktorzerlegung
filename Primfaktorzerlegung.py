
#________Primfaktorzerlegung___________


def isPrimzahl(zahl):
    faktor = zahl   

    for i in range (1, zahl - 1 ):                       
        if zahl % (faktor - i) == 0:                    
            return False
        
    return True

#gibt die nächst große Primzahl zurück
def nextPrimzahl(letzteZahl):
    aktuelleZahl = letzteZahl + 1

    while not isPrimzahl(aktuelleZahl):
        aktuelleZahl = aktuelleZahl + 1 

    return aktuelleZahl

#main
if __name__ == "__main__":
    zahlInput = 937
    
    primfaktor = 2
    primfaktoren = []
    zahl = zahlInput

    if isPrimzahl(zahl):
        print("Deine Zahl ist bereits eine Primzahl")
        primfaktoren.append(zahl)
        

    else:

        while True: 
            if zahl % primfaktor == 0:                     
                primfaktoren.append(primfaktor)             
                zahl = zahl / primfaktor                    
                primfaktor = 2                              
                if zahl == 1:                               
                    break

            else:
                primfaktor = nextPrimzahl(primfaktor)       


        
    print("Die Zahl " +str(int(zahlInput)) + " kann in folgende Primfaktoren zerlegt werden: \n" + str(primfaktoren))


