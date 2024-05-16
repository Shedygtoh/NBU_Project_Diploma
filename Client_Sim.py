# echo-client.py

import socket
import time
import random

HOST = ""  # The server's hostname or IP address
PORT = 1010  # The port used by the server

multy_loop = 0;
while multy_loop <= 1000:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # s.sendall(b"Hello, world")
        data = s.recv(1024)
        stringdata = data.decode('utf-8')
        stringdata2 = "GET STREAM DIGITAL"
        #print (stringdata)
        #print (stringdata2 == stringdata)
        if (stringdata == stringdata2):
            vibro = random.randint(-1024, 1024)
            measurement = "DIGITAL," + str(vibro) + "0.15,0.05,0.86,22,-0.00,-0.00,-0.00,36"
            s.sendall(measurement.encode())
            print(f"Received {data!r}")
            s.close()
    time.sleep(1)
    multy_loop += 1
