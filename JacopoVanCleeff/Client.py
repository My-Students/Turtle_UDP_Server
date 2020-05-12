import socket

server_ip = 'localhost'
server_port = 8500

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  

    while(True):
        equation = input("Inserire una stringa con il comando diviso da un trattino dalla quantità ")     

        client.sendto(equation.encode(), (server_ip, server_port)) 

        if(equation[0:] == "close()"): 
            break

    client.close()

if __name__ == "__main__":
    main()