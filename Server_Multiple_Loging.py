#server_logging_store_data

import socket
import logging
from datetime import datetime
from datetime import date
import os
from _thread import *
import threading 
lock = threading.Lock()
debugg = 1

ServerSideSocket = socket.socket()
host = ''
port = 2010
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)

def multi_threaded_client(connection):
    #lock.acquire()
    # GET STREAM DIGITAL GET STREAM ANALOG
    connection.send(str.encode('GET STREAM DIGITAL'))
    row = ''
    while True:
        data = connection.recv(128)
        row += data.decode('utf-8')
        if (debugg == 1):
            print('received {!r}'.format(data))
        if not data:
            break
        #connection.sendall(str.encode(response))
    if (debugg == 1):
        print(row)
        #connection.send(b"HELLO")
    connection.close()
    if (row != ''):
        now = datetime.now()
        dt_string = now.strftime("%M:%S")# %d/%m/%Y %H
        log_file =  str(address[0])+"_"+now.strftime(" %Y.%m.%d %H")+".txt"
        lock.acquire()
        #logging.basicConfig(filename=str(log_file), level=logging.INFO)
        #logging.info(dt_string + "," + row)
    
        with open(str(log_file), 'a') as f:
            f.write(dt_string + "," + row)
            f.write('\n')

        lock.release()

while True:
    Client, address = ServerSideSocket.accept()
    if (debugg == 1):
        print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    if (debugg == 1):
        print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()
