import sys


#Primera versión

Tablero = []

for i in range(8):
    
    y = 8-i

    for j in range(8):

        punto = (j+1,y)

        Tablero.append(punto)



def recibeCoordenadasFicha():


    repitePregunta = True


    while repitePregunta == True:
        


        ejeXInicial = 0

   
        ingresoLetra = input("Ingresa la letra de la ubicación: ")

        letra = ingresoLetra.upper()


        if letra == "A":
        
            ejeXInicial = 1

            repitePregunta = False

        elif letra == "B":
        
            ejeXInicial = 2

            repitePregunta = False

        elif letra == "C":
        
            ejeXInicial = 3

            repitePregunta = False

        elif letra == "D":
        
            ejeXInicial = 4    

            repitePregunta = False

        elif letra == "E":
        
            ejeXInicial = 5  

            repitePregunta = False

        elif letra == "F":
        
            ejeXInicial = 6   

            repitePregunta = False       

        elif letra == "G":
        
            ejeXInicial = 7     

            repitePregunta = False   

        elif letra == "H":
        
            ejeXInicial = 8   

            repitePregunta = False  

        else:

            print("Ingresa una letra de la A a la H")

            repitePregunta = True

    repitePregunta = True

    while repitePregunta == True:

        ejeYInicial = int(input(("Ingresa el número de la ubicación: ")))

        if ejeYInicial>0 and ejeYInicial<9:

            repitePregunta = False

        else:

            repitePregunta = True

    
    puntoInicial = (ejeXInicial,ejeYInicial)


    return puntoInicial


####METODOS PARA CALCULAR EL MOVIMIENTO DE LAS FICHAS####


def calculaMovimientoAlfil(puntoInicial):

    Alfil = []

    Alfil.append(puntoInicial)

    ejeX,ejeY = puntoInicial   


    while ejeX<8 and ejeY<8:

        ejeX = ejeX+1
        ejeY = ejeY+1

        nuevaCoordenada = (ejeX,ejeY)
    
        Alfil.append(nuevaCoordenada)

    ejeX,ejeY = puntoInicial 

    while ejeX<8 and ejeY>1:

        ejeX = ejeX+1
        ejeY = ejeY-1

        nuevaCoordenada = (ejeX,ejeY)
    
        Alfil.append(nuevaCoordenada)

    ejeX,ejeY = puntoInicial 

    while ejeX>1 and ejeY>1:

        ejeX = ejeX-1
        ejeY = ejeY-1

        nuevaCoordenada = (ejeX,ejeY)

        Alfil.append(nuevaCoordenada)

    ejeX,ejeY = puntoInicial 

    while ejeX>1 and ejeY<8:
        
        ejeX = ejeX-1
        ejeY = ejeY+1

        nuevaCoordenada = (ejeX,ejeY)

        Alfil.append(nuevaCoordenada)

    ejeX,ejeY = puntoInicial 
    

    return Alfil

def calculaMovimientoReina(puntoInicial):

    Reina = []

    Reina.append(puntoInicial)

    ejeX,ejeY = puntoInicial


    while ejeY<8:
   
        ejeY = ejeY+1

        nuevaCoordenada = (ejeX,ejeY)
    
        Reina.append(nuevaCoordenada)

    ejeX,ejeY = puntoInicial     

    while ejeX<8 and ejeY<8:

        ejeX = ejeX+1
        ejeY = ejeY+1

        nuevaCoordenada = (ejeX,ejeY)
    
        Reina.append(nuevaCoordenada)

    ejeX,ejeY = puntoInicial 

    while ejeX<8:
       
        ejeX = ejeX+1

        nuevaCoordenada = (ejeX,ejeY)
    
        Reina.append(nuevaCoordenada)

    ejeX,ejeY = puntoInicial  

    while ejeX<8 and ejeY>1:

        ejeX = ejeX+1
        ejeY = ejeY-1

        nuevaCoordenada = (ejeX,ejeY)
    
        Reina.append(nuevaCoordenada)

    ejeX,ejeY = puntoInicial

    while ejeY>1:

        ejeY = ejeY-1

        nuevaCoordenada = (ejeX,ejeY)
    
        Reina.append(nuevaCoordenada)

    ejeX,ejeY = puntoInicial

    while ejeX>1 and ejeY>1:

        ejeX = ejeX-1
        ejeY = ejeY-1

        nuevaCoordenada = (ejeX,ejeY)

        Reina.append(nuevaCoordenada)

    ejeX,ejeY = puntoInicial

    while ejeX>1:

        ejeX = ejeX-1

        nuevaCoordenada = (ejeX,ejeY)

        Reina.append(nuevaCoordenada)

    ejeX,ejeY = puntoInicial 

    while ejeX>1 and ejeY<8:
        
        ejeX = ejeX-1
        ejeY = ejeY+1

        nuevaCoordenada = (ejeX,ejeY)

        Reina.append(nuevaCoordenada)

    ejeX,ejeY = puntoInicial 
    
    return Reina

def calculaMovimientoCaballo(puntoInicial):

    Caballo = []

    Caballo.append(puntoInicial)

    ejeX,ejeY = puntoInicial


    if ejeX<8 and ejeY<8:

        ejeX = ejeX+1
        ejeY = ejeY+2

        nuevaCoordenada = (ejeX,ejeY)

        Caballo.append(nuevaCoordenada)


        ejeX,ejeY = puntoInicial

        ejeX = ejeX+2
        ejeY = ejeY+1

        nuevaCoordenada = (ejeX,ejeY)

        Caballo.append(nuevaCoordenada)


    ejeX,ejeY = puntoInicial    

    if ejeX<8 and ejeY>1:

        ejeX = ejeX+2
        ejeY = ejeY-1

        nuevaCoordenada = (ejeX,ejeY)

        Caballo.append(nuevaCoordenada)


        ejeX,ejeY = puntoInicial    

        ejeX = ejeX+1
        ejeY = ejeY-2

        nuevaCoordenada = (ejeX,ejeY)

        Caballo.append(nuevaCoordenada)


    ejeX,ejeY = puntoInicial

    if ejeX>1 and ejeY>1:

        ejeX = ejeX-1
        ejeY = ejeY-2 

        nuevaCoordenada = (ejeX,ejeY)

        Caballo.append(nuevaCoordenada)


        ejeX,ejeY = puntoInicial

        ejeX = ejeX-2
        ejeY = ejeY-1

        nuevaCoordenada = (ejeX,ejeY)

        Caballo.append(nuevaCoordenada)


    ejeX,ejeY = puntoInicial

    if ejeX>1 and ejeY<8:

        ejeX = ejeX-2
        ejeY = ejeY+1

        nuevaCoordenada = (ejeX,ejeY)

        Caballo.append(nuevaCoordenada)


        ejeX,ejeY = puntoInicial

        ejeX = ejeX-1
        ejeY = ejeY+2

        nuevaCoordenada = (ejeX,ejeY)

        Caballo.append(nuevaCoordenada)


    return Caballo


def calculaMovimientoataquePeon(puntoInicial):

    Peon = []

    Peon.append(puntoInicial)

    ejeX,ejeY = puntoInicial


    if ejeX<8 and ejeY<8:

        ejeX = ejeX+1
        ejeY = ejeY+1

        nuevaCoordenada = (ejeX,ejeY)

        Peon.append(nuevaCoordenada)


    ejeX,ejeY = puntoInicial   

    if ejeX>1 and ejeY<8:

        ejeX = ejeX-1
        ejeY = ejeY+1

        nuevaCoordenada = (ejeX,ejeY)

        Peon.append(nuevaCoordenada)



    return Peon



def calculaMovimientoTorre(puntoInicial):

    Torre = []

    Torre.append(puntoInicial)

    ejeX,ejeY = puntoInicial

    while ejeY<8:

        ejeY = ejeY+1

        nuevaCoordenada = (ejeX,ejeY)

        Torre.append(nuevaCoordenada)


    ejeX,ejeY = puntoInicial

    while ejeX<8:

        ejeX = ejeX+1

        nuevaCoordenada = (ejeX,ejeY)

        Torre.append(nuevaCoordenada)

    ejeX,ejeY = puntoInicial    


    while ejeY>1:

        ejeY = ejeY-1

        nuevaCoordenada = (ejeX,ejeY)

        Torre.append(nuevaCoordenada)


    ejeX,ejeY = puntoInicial

    while ejeX>1:

        ejeX = ejeX-1

        nuevaCoordenada = (ejeX,ejeY)

        Torre.append(nuevaCoordenada)    


    return Torre    


def imprimeTablero(posicionAlfil,posicionReina,posicionCaballo,posicionPeon,posicionTorre):

    contador = 0

    Rey = (4,8,)

    print()
    
    for i in range(0,len(Tablero),1):

        if Rey ==Tablero[i]:
    
            sys.stdout.write(" nK   ")
    
        elif posicionAlfil==Tablero[i]:

            sys.stdout.write(" bA   ")
        elif posicionReina==Tablero[i]:
    
            sys.stdout.write(" bR   ")   
        elif posicionCaballo==Tablero[i]:
    
            sys.stdout.write(" bC   ")
        elif posicionPeon==Tablero[i]:
    
            sys.stdout.write(" bP   ")

        elif posicionTorre==Tablero[i]:
    
            sys.stdout.write(" bT   ")             

        else:

            sys.stdout.write(" °    ") 

        contador = contador+1

        if contador == 8 or contador == 16 or contador == 24 or contador == 32 or contador == 40 \
        or contador == 48 or contador == 56:

            print() 
            print()
            print()

def defineJaque(Alfil,Reina,Caballo,Peon,Torre):

    Rey = [(4,8,)]

    if Rey[0] in Alfil[:]:

        print("\n\n El rey está en Jaque con el alfil")

    elif Rey[0] in Reina[:]:
    
        print("\n\n El rey está en Jaque con la reina") 

    elif Rey[0] in Caballo[:]:
    
        print("\n\n El rey está en Jaque con el caballo")

    elif Rey[0] in Peon[:]:
    
        print("\n\n El rey está en Jaque con el peón")

    elif Rey[0] in Torre[:]:

        print ("\n\n El rey está en jaque con la Torre")    

    else: 

        print("\n\n El rey no está en jaque con ninguna ficha")             


    





       
##########EJECUCIÓN####################


print("\n\n En una partida de ajedrez, el jugador que usa las fichas negras cuenta solo con su rey, mientras \n \
que el jugador que usa las fichas blancas cuenta aún con un alfil, su reina, un caballo, un peón y una torre. \n \n \
El presente programa te da la posibilidad de escoger la posición en la que se encuentran las fichas blancas que\n \
aún están en el juego y te enseñará como se verían en el tablero junto al rey contrincante. Al final te dirá si\n \
el rey negro queda en jaque con alguna ficha blanca y con cual.")


print(" \n Las fichas están representadas en el tablero por las siguientes convenciones:  \n \n \
Rey negro = nK \n \
Alfil blanco = bA \n \
Reina blanca = bR \n \
Caballo blanco = bC \n \
Peon blanco = bP \n \
Torre blanco = bT \n") 

print("\nEl tablero se verá reflejado de la siguiente manera: \n")

for i in range(8):

    print()

    for j in range(8):

        sys.stdout.write(" °")





print("\n\nIngresa la posición del alfil (Letra/número): \n")

posicionAlfil = recibeCoordenadasFicha()

Alfil = calculaMovimientoAlfil(posicionAlfil)

print("Ingresa la posición de la reina (Letra/número): \n")

posicionReina = recibeCoordenadasFicha()

Reina = calculaMovimientoReina(posicionReina)

print("Ingresa la posición de el caballo (Letra/número): \n")

posicionCaballo = recibeCoordenadasFicha()

Caballo = calculaMovimientoCaballo(posicionCaballo)

print("Ingresa la posición del peón (Letra/número): \n")

posicionPeon = recibeCoordenadasFicha()

Peon = calculaMovimientoataquePeon(posicionPeon)

print("Ingresa la posición de la torre (Letra/número): \n")

posicionTorre = recibeCoordenadasFicha()

Torre = calculaMovimientoTorre(posicionTorre)


contador = 0

imprimeTablero(posicionAlfil,posicionReina,posicionCaballo,posicionPeon,posicionTorre)

defineJaque(Alfil,Reina,Caballo,Peon,Torre)

    



