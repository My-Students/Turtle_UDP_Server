import socket
import turtle
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
design = turtle.Turtle()
s.bind(('localhost',2000))
while(True):
    data,address = s.recvfrom(4096)
    data_string = data.decode()
    if(data_string == "5"):
        print("Shutdown.")
        break
    else:
        x = data_string.split(",") #x = vettore con 2 valori, es. ["2","40"]
        command(int(x[0]))

s.close

def command(number):
    switcher = {
        1: design.right(int(x[1])),
        2: design.left(int(x[1])),
        3: design.forward(int(x[1])),
        4: design.backward(int(x[1]))
    }