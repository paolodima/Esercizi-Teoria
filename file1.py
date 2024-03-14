import math

while True  :

    print("*****Questo fantastico programma ti da la possibilita'di eseguire diverse operazioni******\n Scegliere tra le seguenti opzioni:\n 1] Addizione\n 2] Sottrazione\n 3] Moltiplicazione\n 4] Divisione\n 5] Radice Quadrata\n 6] Calcolo perimetro")
    scelta = int(input("Inserisci qui il numero dell'operazione desiderata: "))

    if scelta == 1 :
        print("Hai scelto addizione !")
        n1 = int(input("Inserisci il primo numero : "))
        n2 = int(input("insrisci il secondo numero : "))
        print("il risultato della somma e': ", n1 + n2)

        print("1] Fai una nuova operazione\n2] Esci ")
        menu = int(input("Scelta: "))
        if menu == 1 :
            continue 
        else : 
            break
                

    elif scelta == 2 :
        print("Hai scelto sottrazione !")
        n1 = int(input("Inserisci il primo numero : "))
        n2 = int(input("insrisci il secondo numero : "))
        print("il risultato della sottrazione e': ", n1 - n2)
        print("1] Fai una nuova operazione\n2] Esci ")
        menu = int(input("Scelta: "))
        if menu == 1 :
            continue 
        else : 
            break

    elif scelta == 3 :
        print("Hai scelto moltiplicazione !")
        n1 = int(input("Inserisci il primo numero : "))
        n2 = int(input("insrisci il secondo numero : "))
        print("il risultato della moltiplicazione e': ", n1 * n2)
        print("1] Fai una nuova operazione\n2] Esci ")
        menu = int(input("Scelta: "))
        if menu == 1 :
            continue 
        else : 
            break

    elif scelta == 4 :
        print("Hai scelto divisione !")
        n1 = int(input("Inserisci il primo numero : "))
        n2 = int(input("insrisci il secondo numero : "))
        print("il risultato della divisione e': ", n1 / n2)
        print("1] Fai una nuova operazione\n2] Esci ")
        menu = int(input("Scelta: "))
        if menu == 1 :
            continue 
        else : 
            break

    elif scelta == 5 :
        print("Hai scelto Radice quadrata !")
        n1 = int(input("Inserisci il numero di cui si vuole fare la Radice quadrata : "))
        print("la radice quadrata di", n1, "e': ", math.sqrt(n1))
        print("1] Fai una nuova operazione\n2] Esci ")
        menu = int(input("Scelta: "))
        if menu == 1 :
            continue 
        else : 
            break

    elif scelta == 6 :
        print("Hai scelto il calcolo del perimetro!\n Puoi scegliere tra le seguenti figure : \n 1] Quadrato\n 2] Cerchio\n 3] Rettangolo\n 4] Triangolo")
        scelta_figura = int(input("Inserire il numero corrispondente alla figura desiderata: "))
	
    if scelta_figura == 1:
		
        print("Hai scelto Quadrato!")
        lato = int(input("inserire lato del quadrato: "))
        print("Il perimetro del tuo quadrato e': ", lato *4)
        print("1] Fai una nuova operazione\n2] Esci ")
        menu = int(input("Scelta: "))
        if menu == 1 :
            continue 
        else : 
            break

    elif scelta_figura == 2:            
        print("Hai scelto Cerchio!")
        raggio = int(input("inserire il raggio del cerchio : "))
        print("La circonferenza del cerchio e': ", 2 * 3.14 * raggio)
        print("1] Fai una nuova operazione\n2] Esci ")
        menu = int(input("Scelta: "))
        if menu == 1 :
            continue 
        else : 
            break

    elif scelta_figura == 3:            
        print("Hai scelto Rettangolo!")
        base = int(input("inserire base del rettangolo : "))
        altezza = int(input("inserire altezza del rettangolo : "))
        print("Il perimetro del Rettangolo e': ", 2 * base + 2* altezza)
        print("1] Fai una nuova operazione\n2] Esci ")
        menu = int(input("Scelta: "))
        if menu == 1 :
            continue 
        else : 
            break

    elif scelta_figura == 4:             
        print("Hai scelto Triangolo!")
        base = int(input("inserire base del triangolo : "))
        altezza = int(input("inserire altezza del triangolo : "))
        print("Il perimetro del Triangolo e': ",  (base * altezza)/2)
        print("1] Fai una nuova operazione\n2] Esci ")
        menu = int(input("Scelta: "))
        if menu == 1 :
            continue 
        else : 
            break



    else :
	
	    print("Mi discpiace, questa scelta non e' disponibile :(")

