import random

palos=('o','c','e','b')
cartas=('A','2','3','4','5','6','7','S','C','R')


def creaBaraja():

    baraja=[]

    for palo in palos:
        for carta in cartas:
            naipe= carta+palo
            baraja.append(naipe)

    return baraja

def barajar(b):
    
    bBarajada=[]
    for item in b:
        ind= random.randint(0,len(b)-1)
        cartaBaraj= b[ind]
        
        while cartaBaraj in bBarajada:
            ind= random.randint(0,len(b)-1)
            cartaBaraj= b[ind]

        bBarajada.append(cartaBaraj)
        
    b[:] =bBarajada
    return b


def repartir(b, players,cards):
    b=b[:]
    res= []
    for p in range(players):
        res.append([])  #crea tantas listas vacias como jugadores
    for ic in range (cards):
        for ij in range (players):
            carta = b.pop(0)
            res[ij].append(carta)

    return res


def invertir(b):
    for i in range (len(b)//2):
        aux= b[i]
        b[i]= b[-1-i]
        b[-1-i]= aux
