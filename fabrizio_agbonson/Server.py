import socket
import turtle
import random

colors  = ["red","green","blue","orange","purple","pink","yellow"]
bind_adr = ("localhost",10000)
SPEED = 100


def turtle_movement(t:turtle,mov):
    if mov == "w":
        t.forward(SPEED)
        pass
    if mov == "a":
        t.left(90)
        pass
    if mov == "d":
        t.right(90)
        pass
    if mov == "s":
        t.backward(SPEED)
        
    
        
def Crea_turtle()-> turtle:
    Player = turtle.Turtle()
    color = random.choice(colors)
    Player.color(color)
    Player.shape("turtle")
    
    Player.penup()
    
    return Player
    

user_dict = {}


with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    s.bind(bind_adr)
    

    print("creo il server...")
    print("avvio del server..")
    print("server[on]")
    
    while True:
        data_mov , addr = s.recvfrom(4096)

        if addr[1] in user_dict.keys():
            turtle_movement(user_dict[addr[1]], data_mov.decode())
        else:
            play = Crea_turtle()
            user_dict[addr[1]] = play
            turtle_movement(play, data_mov.decode())
    
