
import socket
import pickle
from random import seed
from random import randint

host = socket.gethostname()
port = 12345

op = input("Enter the operation number")
packet = []
packet.append(int(op))
for i in range(100):
    packet.append(randint(1, 100))

print(packet)
packet = pickle.dumps(packet)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host, port))
clientSocket.send(packet)
