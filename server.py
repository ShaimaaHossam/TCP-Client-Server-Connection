import socket
import pickle

host = socket.gethostname()
port = 12345
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket object
serverSocket.bind((host, port))
print("Waiting for clients..")
serverSocket.listen(5)


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
        sum = 0
        avg = 0
        for i in data:
            sum = sum+i
        avg = sum/len(data)
        packet = [f'Sum is {sum}', f'Average is {avg}']

    elif op_no == 2:
        maximum = max(data)
        minimum = min(data)
        packet = [f'Max is {maximum}', f'Min is {minimum}']
    elif op_no == 3:
        rev = Reverse(data)
        packet = [f'Reversed Array is {rev}']
    elif op_no == 4:
        sorted_arr = sorted(data)
        packet = [f'Sorted Array is {sorted_arr}']

    packet = pickle.dumps(packet)
    conn.send(packet)


conn.close()
