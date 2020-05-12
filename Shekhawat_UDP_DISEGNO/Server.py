import socket
import turtle
#import threading
#import time
#from queue import Queue


ip = '127.0.0.1'
host = 80
indirizzo = (ip,host)
counter = 0 

#NUMERO_THREAD = 2
#WORK = [1,2]
#lavori = Queue()
nomi = []
ipA = [] 

"""def disegno(s):

    comm, address = s.recvfrom(4096)
    comm.decode()
    comm = comm.split("_")
    x=0

    while True:
        if address == ipA[x]:
            sog = nomi[x]
            break
        else:
            x=x+1

    comm[1] = float(comm[1])

        if comm[0] == "Forward":
            print("Forward")
            sog.forward(comm[1])
        if(comm[0] == "backward"):
            print("backward")
            sog.backward(comm[1])
        if(comm[0] == "right"):
            print("right")
            sog.right(comm[1])
        if(comm[0] == "left"):
            print("left")
            sog.left(comm[1])
"""
            
def creoSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return s

def bindo(indirizzo, s):
    s.bind(indirizzo)

def accettazione(s):
   while True:
        controllo = True
        comm, address = s.recvfrom(4096)
        comm.decode()
        print(f"Nome Scelto{comm}")
        print(f"Connesso a {address}")
        for x in ipA:
                if x == "address":
                    sog = nomi[x]
                    controllo = False

        
        if controllo == True:
                comm = turtle.Turtle()
                nomi.append(comm)
                ipA.append(address)
                print(f"Connesso a {address}")
    
        if controllo == False:
            comm = comm.split("_")
            if comm[0] == "Forward":
                print("Forward")
                sog.forward(comm[1])
            if(comm[0] == "backward"):
                print("backward")
                sog.backward(comm[1])
            if(comm[0] == "right"):
                print("right")
                sog.right(comm[1])
            if(comm[0] == "left"):
                print("left")
                sog.left(comm[1])  

"""
#def creo_Thread():
    for _ in range(NUMERO_THREAD):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()
    
#def creo_Work():
    for x in range(WORK):
        lavori.put(x)

    lavori.join()

#def work():
    while True:
        l = lavori.get()
        if l == 1:
            accettazione(creoSocket())
        if l == 2:
            disegno(creoSocket())
"""
def main():
    s=creoSocket()
    bindo(indirizzo,s)
    accettazione(s)
    #creo_Thread()
    #creo_Work
    #work()
    

if __name__ == "__main__":
   main()
   socket.close()

