#coding:utf-8
import socket
import threading
s=socket.socket()
host=raw_input('input the hostIP:')
port=raw_input('input the port:')
s.connect((host,int(port)))
print 'Connected...'
def recv():
        while True:
                print s.recv(1024)
def send():
        while True:
                s.send(raw_input())
threading.Thread(target=recv,args=()).start()
threading.Thread(target=send,args=()).start()
