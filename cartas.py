import random

palos=('0','c','e','b')
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
        ind= random.randint(0,39)
        cartaBaraj= b[ind]
        
        while cartaBaraj in bBarajada:
            ind= random.randint(0,39)
            cartaBaraj= b[ind]

        bBarajada.append(cartaBaraj)
    

    return bBarajada



