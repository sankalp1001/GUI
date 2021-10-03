#server
import socket
import threading 

HEADER= 64
PORT= 49170 #choose the port through which the data gets trasnferred**
SERVER=socket.gethostbyname(socket.gethostname()) #get the ip add of the device 
ADDR =(SERVER,PORT)
FORMAT ='utf-8'
DISCONNECT_MSG= 'DISCONNECTED'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #get the type of ip addr
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"New connection{addr} connected\n")
    connected = True
    while connected:
      msg_length = int(conn.recv(HEADER).decode(FORMAT))
      msg = conn.recv(msg_length).decode(FORMAT)
      if msg == DISCONNECT_MSG:
         connected= False
      print(f"{addr} sent {msg}") 
    conn.close()

def start():
  server.listen()
  print(f'Server is listening on {SERVER}\n')
  while True:
   conn,addr= server.accept() 
   thread=threading.Thread(target=handle_client,args=(conn,addr))
   thread.start()
   print(f"No of connections {threading.activecount()-1}\n")
print("server starting/n")
start()
#client
import socket


HEADER= 64
PORT= 49170 #choose the port through which the data gets trasnferred**
FORMAT ='utf-8'
SERVER=socket.gethostbyname(socket.gethostname()) #get the ip add of the device 
DISCONNECT_MSG= 'DISCONNECTED'
ADDR = (SERVER,PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World!")

send(DISCONNECT_MSG)

