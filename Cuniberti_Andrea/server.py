
import socket
import turtle
from ast import literal_eval

IpAddress = 'localhost'
port = 5004

tart = turtle.Turtle()
mossa = 0
lung = 0

srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

srv.bind((IpAddress,port))

while(True):
    #invio del messaggio

    #ricezione del messaggio
    data, address = srv.recvfrom(8036)
    print(f"msg from client: {data}")

    data = literal_eval(data)

    tart = data[0]

    mossa = data[1]

    lung = data[2]
    
    switcher = {
        1 : "tart.forward(lung)",
        2 : "tart.backward(lung)",
        3 : "tart.left(lung)",
        4 : "tart.right(lung)"
    }

    switcher.get(eval(mossa))

    data = (f"{tart}")
    #si può interrompere il collegamento digitando '$stop'
    if str(data,encoding="ascii") == "$stop":
        break
    
    #invio messaggio di conferma
    if data:
        sent = srv.sendto(data, address)
        print (f"sent {data} bytes back to {IpAddress}")

srv.close()