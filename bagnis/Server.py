import socket
import turtle

#indirizzo e porta di questo server
ip="127.0.0.1"
porta=2512

#creazione del socket e binding
socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket.bind((ip,porta))

#variabili necessarie per la creazione e il movimento delle tartarughe
porte_tartarughe = [] 
tartarughe = {} 

#variabile che indica il movimento
movimento = {}

#crea la tartaruga ed esegue il primo movimento
def creazione_tartaruga(porta_client, azione):
    movimento[porta_client[1]]=10
    tartarughe[porta_client[1]]=turtle.Turtle()
    esegui(porta_client,movimento[porta_client[1]])

#esegue l'azione richiesta dal client
def esegui(porta_client, azione):
    if azione=="w":
        tartarughe[porta_client[1]].forward(movimento[porta_client[1]])
    elif azione=="s":
        tartarughe[porta_client[1]].backward(movimento[porta_client[1]])
    elif azione=="a":
        tartarughe[porta_client[1]].left(movimento[porta_client[1]])
    elif azione=="d":
        tartarughe[porta_client[1]].right(movimento[porta_client[1]]) 
    elif azione=="e":
        movimento[porta_client[1]]+=1 
    elif azione=="q":
        movimento[porta_client[1]]-=1 
    elif azione=="t":
        TerminateProcess
    elif azione=="i":
        tartarughe[porta_client[1]].undo() 

def main():
    while True:
        #leggo i valori passati dal client
        valore_input, porta_client = socket.recvfrom(4096)
        azione=valore_input.decode()[0:]

        #se la tartaruga esiste già la sposto altrimenti ne creo una
        if porta_client[1] in porte_tartarughe:
            esegui(porta_client,azione)
        else:
            porte_tartarughe.append(porta_client[1])
            creazione_tartaruga(porta_client,azione)
            #dati per il server
            print(f"creazione tartaruga con porta: {porta_client[1]}")

        #dati per il server
        print(f"porta: {porta_client[1]} - comando: {azione} - movimento: {movimento[porta_client[1]]}")

if __name__ == "__main__":
    main()



