import random

class Baraja():

    palos =('o','c','e','b')
    cartas=('A','2','3','4','5','6','7','S','C','R')

    def __init__(self):
        self.__creaBaraja()
        

    def __creaBaraja(self):
        self.naipes=[]
        self.mano= []
        for palo in self.palos:
            for carta in self.cartas:
                naipe= carta+palo
                self.naipes.append(naipe)

    def barajar(self):
        bBarajada=[]
        for item in self.naipes:
            ind= random.randint(0,len(self.naipes)-1)
            cartaBaraj= self.naipes[ind]
            
            while cartaBaraj in bBarajada:
                ind= random.randint(0,len(self.naipes)-1)
                cartaBaraj= self.naipes[ind]

            bBarajada.append(cartaBaraj)
            
        self.naipes[:] =bBarajada


    def repartir(self, players,cards):
        
        if self.mano == []:
            for p in range(players):
                self.mano.append([])  #crea tantas listas vacias como jugadores
        else:
            pass
        
        for ic in range (cards):
                for ij in range (players):
                    carta = self.naipes.pop(0)
                    self.mano[ij].append(carta)

        return self.mano
    
    def recoger(self):
        self.__creaBaraja()

if __name__== "__main__":

    b1= Baraja()
    print (b1.naipes)
    b1.barajar()
    bR= b1.repartir(3, 5)

    print(b1.naipes)
    #print(bB)
    print(bR)

    bRR= b1.repartir(3,1)
    print (bRR)
