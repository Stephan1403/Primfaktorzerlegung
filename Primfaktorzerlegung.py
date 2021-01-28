
#________Primfaktorzerlegung___________

#überprüft, ob es sich um eine primzahl handelt, indem sie prüft, ob sie durch irgendeine Zahl teilbar ist außer 1 und sich selbst
def isPrimzahl(zahl):
    faktor = zahl   

    for i in range (1, zahl - 1 ):                       #schleife die die von 1 bis zu (zahl - 1) durchläuft
        if zahl % (faktor - i) == 0:                     #überprüft beim ersten mal, ob zahl / zahl-1 ohne Rest teilbar ist. Die nächsten Durchgänge jeweils wird der Nenner um 1 veringert
            return False
        
    return True

#gibt die nächst große Primzahl zurück
def nextPrimzahl(letzteZahl):
    aktuelleZahl = letzteZahl + 1

    while not isPrimzahl(aktuelleZahl):                  #solange die aktuelleZahl keine Primzahl ist wird sie um 1 erhöht
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
            if zahl % primfaktor == 0:                      #wenn ja, dann ist primfaktor der erste faktor
                primfaktoren.append(primfaktor)             #primfaktor wird zur liste hinzugefügt
                zahl = zahl / primfaktor                    #der primfaktor wird einmal aus der zahl gezogen
                primfaktor = 2                              #primfaktor wird zurück gesetzt
                if zahl == 1:                               #bricht nach letztem Versuch
                    break

            else:
                primfaktor = nextPrimzahl(primfaktor)       #der nächst hohe primfaktor ersetzt den aktuellen primfaktoren


        

    #result
    print("Die Zahl " +str(int(zahlInput)) + " kann in folgende Primfaktoren zerlegt werden: \n" + str(primfaktoren))


