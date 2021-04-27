import socket
import pickle

host = socket.gethostname()
port = 12345
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket object
serverSocket.bind((host, port))
print("Waiting for clients..")
serverSocket.listen(5)
sum =0
avg = 0

def Reverse(lst):
    return [ele for ele in reversed(lst)]

while True:
    conn, addr = serverSocket.accept()
    print(f"Connection with {addr} established successfully")
    packet = conn.recv(1024)
    packet = pickle.loads(packet)
    op_no = packet[0]
    data = packet[1:]
    if op_no == 1:
        for i in data:
            sum = sum+i
        avg = sum/len(data)
        print(f'Sum = {sum}, Average = {avg}')

    elif op_no == 2:
        maximum = max(data)
        minimum = min(data)
        print(f'Maximum Number: {maximum}, Minimum Number: {minimum}')
    elif op_no == 3:
        rev = Reverse(data)
        print(rev)
    elif op_no == 4:
        sorted_arr = sorted(data)
        print(sorted_arr)

conn.close()
