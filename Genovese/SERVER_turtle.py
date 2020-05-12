import turtle
import socket
import time
import sys
import random

colors = ["red", "blue", "green", "yellow", "pink", "brown", "cyan", "magenta", "purple", "orange"]
VAL_ERRATO = "Valore errato, inserisci un movimento(w/a/s/d) '=' ed i pixel o i gradi(numero intero)"
giocatori=[]
porte= []
mov=0

def creaGioc(i):
    giocatori.append(turtle.Turtle())
    color = random.choice(colors)
    giocatori[len(giocatori)-1].color(color)

def muovi(i, wasd, PxGr, addr):
    if (wasd == 'w' or wasd == 'W'):
        giocatori[i].forward(PxGr)

    elif (wasd == "s" or wasd == "S"):
        giocatori[i].backward(PxGr)

    elif (wasd == "a" or wasd == "A"):
        giocatori[i].left(PxGr)

    elif (wasd == "d" or wasd == "D"):
        giocatori[i].right(PxGr)
    else:
        #controllo poco utile
        srv.sendto(VAL_ERRATO, addr)
    
    
#def main():
IpAddress = '0.0.0.0'
port = 5004

srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

srv.bind((IpAddress, port))

#print(porte)

while (True):

    # ottengo il movimento (w,a,s,d) e l'address
    mov, address = srv.recvfrom(8036)
    movimento = mov.decode().split("=")
    movimento[1] = float(movimento[1])
    print(movimento[1])
    i=0
    for i in range(0, len(porte)+1):
        if (i > len(porte)-1):
            print("primo if")
            porte.append(address[1])
            creaGioc(i)
            print(movimento[1], address)
            muovi(i, movimento[0], movimento[1], address)
            break
        if(address[1]==porte[i]):
            print("secondo if")
            muovi(i, movimento[0], movimento[1], address)
            break

        print(porte)

    print(f"il giocatore {address[1]} fa: {movimento[0]} di {movimento[1]}")
    mov = 0


srv.close()


#if __name__ == "__main__":
#    main()
