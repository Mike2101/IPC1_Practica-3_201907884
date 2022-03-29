
import random

 #### clases

class Comida():
     
    def __init__(self, posx, posy):
         self.posx = posx
         self.posy = posy
         self.isEat = False

    def getPosX(self):
        return self.posx

    def getPosY(self):
        return self.posy

    def isComido(self):
        return self.isEat

    def setPosY(self, _posy):
        self.posy = _posy

    def setPosX(self, _posx):
        self.posx = _posx

    def setEat(self):
        self.isEat = True

class pared():
    def __init__(self,posx,posy):
        self.posx = posx
        self.posy = posy
        self.Comido = True
    
    def setPosY(self, _posy):
        self.posy = _posy

    def isComido(self):
        return self.Comido

    def setPosX(self, _posx):
        self.posx = _posx
    
    def getPosX(self):
        return self.posx

    def getPosY(self):
        return self.posy

class Player():
    def __init__(self, nombre):
        self.nombre = nombre
        self.posx = 0
        self.posy = 0
        self.puntos = 0
        self.movimientos = 0

    def getPosX(self):
        return self.posx

    def getPosY(self):
        return self.posy

    def getMovimientos(self):
        return self.movimientos

    def getPuntos(self):
        return self.puntos

    def setPosY(self, _posy):
        self.posy = _posy

    def setPosX(self, _posx):
        self.posx = _posx

    def addMovimiento(self):
        self.movimientos = self.movimientos + 1

    def addPuntos(self):
        self.puntos = self.puntos + 5


def imprimirTablero(tablero):
    for fila in tablero:
        print("\t| {0[0]} {0[1]} {0[2]} {0[3]} {0[4]} {0[5]} {0[6]} {0[7]} {0[8]} {0[9]} {0[10]} {0[11]} {0[12]} | ".format(fila))

def pintarTablero(lista_comida, lista_paredes, jugador): #lleva lista_paredes

    tablero = [
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "]
    ]

    for comida in lista_comida:
        if not comida.isComido():
            tablero[comida.getPosX()][comida.getPosY()] = "@"
   
    for pared in lista_paredes:
        if True== pared.isComido():
           tablero[pared.getPosX()][pared.getPosY()] = "#"
            
   
    tablero[jugador.getPosX()][jugador.getPosY()] = "C"
    return tablero

def crearListaComidas(lista_comida, comidas: int):
    index = 0
    while index < comidas:
        #### - 0 - 12
        posx_comida_generada = random.randint(0,12)
        posy_comida_generada = random.randint(0,12)
        estaOcupado = False
        for comidas_busqueda in lista_comida:
            if comidas_busqueda.getPosX() == posx_comida_generada and comidas_busqueda.getPosY() == posy_comida_generada:
                estaOcupado = True
        
        if not estaOcupado:
            comida_creada = Comida(posx_comida_generada, posy_comida_generada)
            lista_comida.append(comida_creada)
            index = index + 1

def siguienteHayComida(jugador, lista_comida):
    for comida in lista_comida:
        if jugador.getPosX() == comida.getPosX() and jugador.getPosY() == comida.getPosY():
            comida.setEat()
            jugador.addPuntos()
            return True
    return False

def aunHayComidas(lista_comidas):
    for comida in lista_comidas:
        if not comida.isComido():
            return False
    return True

def crearParedes(lista_paredes,paredes: int):
    index = 0
    while index < paredes:
        #### - 0 - 12
        posx_pared_generada = random.randint(0,12)
        posy_pared_generada = random.randint(0,12)
        estaOcupado = False
        for pared_busqueda in lista_paredes:
            if pared_busqueda.getPosY() == posx_pared_generada and pared_busqueda.getPosX() == posy_pared_generada:
                estaOcupado = True
        
        if not estaOcupado:
            pared_creada = pared(posx_pared_generada, posy_pared_generada)
            lista_paredes.append(pared_creada)
            index = index + 1
    for p in lista_paredes:
        print(p.getPosX(),p.getPosY())

def siguienteHayComida(jugador, lista_comida):
    for comida in lista_comida:
        if jugador.getPosX() == comida.getPosX() and jugador.getPosY() == comida.getPosY():
            comida.setEat()
            jugador.addPuntos()
            return True
    return False

def movimientos(jugadorActual, lista_comidas, Paredes):
    menu = """
        _____________________________
        MENU
        d/6. mover adelante
        a/4. mover atras
        w/8. arriba
        s/5. abajo
        e. volver al menu principal
        ______________________________
    """

    while True:
        print(menu)
        mov = input("Movimiento: ")
        posxAct = jugadorActual.getPosX()
        posyAct = jugadorActual.getPosY()
        pos_auxX=posxAct
        pos_auxY=posyAct
        if (mov == 'w' or mov == '8') and posxAct>0:
            pos_auxX = pos_auxX-1
        if (mov == 's' or mov == '5') and posxAct<12:
            pos_auxX = pos_auxX+1
        if (mov == 'a' or mov == '4') and posyAct>0:
            pos_auxY = pos_auxY-1
        if (mov == 'd' or mov == '6') and posyAct<12:
            pos_auxY = pos_auxY+1
        count=0
        for pared in Paredes:
            if(pared.getPosY()==pos_auxY and pared.getPosX()==pos_auxX):
               count+=1
        if(count==0):
            if (mov == 'w' or mov == '8') and posxAct>0:
                posxAct = posxAct-1
                jugadorActual.addMovimiento()
            if (mov == 's' or mov == '5') and posxAct<12:
                posxAct = posxAct+1
                jugadorActual.addMovimiento()
            if (mov == 'a' or mov == '4') and posyAct>0:
                posyAct = posyAct-1
                jugadorActual.addMovimiento()
            if (mov == 'd' or mov == '6') and posyAct<12:
                posyAct = posyAct+1
                jugadorActual.addMovimiento()
            if mov == "e":
                menu_inicial()
                break

            jugadorActual.setPosX(int(posxAct))
            jugadorActual.setPosY(int(posyAct))
            print(posxAct, posyAct)
            mov = siguienteHayComida(jugadorActual, lista_comidas)
            
        print(" - "+str(jugadorActual.nombre)+" - PUNTOS: {0} - MOVIMIMENTOS: {1}".format(jugadorActual.getPuntos(), jugadorActual.getMovimientos()))
        tablero = pintarTablero(lista_comidas,Paredes, jugadorActual)
        imprimirTablero(tablero)
        if jugadorActual.getPuntos() >= 40 or aunHayComidas(lista_comidas):
            break   
        


        # lista paredes[xxxxxxxxxxxxxxxxxxxxxxx] 
        #mov = siguienteHayComida(jugadorActual, lista_comidas)
         

def juego(jugador):

    ### --- definir las comidas
    comidas_solicitadas = int(144*0.4)
    lista_comidas = []
    paredes = int(144*0.3)
    lista_paredes = []
    crearListaComidas(lista_comidas, comidas_solicitadas)
    crearParedes(lista_paredes,paredes)

    jugador.setPosX(2)
    jugador.setPosY(2)

    ### inicializar el tablero de juego
    tablero = pintarTablero(lista_comidas, lista_paredes, jugador) #lleva lista_paredes
    imprimirTablero(tablero)
    
    ## logica de juego
    movimientos(jugador, lista_comidas, lista_paredes) #lleva lista_paredes

def inicio():
    name = input('Ingrese su nombre para comenzar a jugar: ')
    jugador = Player(name)
    juego(jugador)

def menu_inicial():
     n = "0"
     while n != "3":
          print("Bienvenidos a PAC-MAN")
          print("----------------------")
          print("1). iniciar juego")
          print("2). Tabla de posiciones")
          print("3). Salir ")
          print("----------------------")
          n = str(input("ingrese una opcion: "))
      #pasandole la opcion
          if n == "1":
           inicio()
          elif n == "2":
           print("no hay papel")
          elif n == "3":
           print("==================================")
           print("       Gracias por jugar :3       ")
           print("==================================")
           break
          else:
           print("----------------------------")
           print("ingrese una opcion correcta")
           print("----------------------------")

#Comienza el programa   
menu_inicial()

    

