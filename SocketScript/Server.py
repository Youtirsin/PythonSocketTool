#coding:utf-8
import socket
import threading
s=socket.socket()
Clients=list()
s.bind((socket.gethostbyname(socket.gethostname()),10010))
s.listen(5)
print socket.gethostbyname(socket.gethostname())+':10010'
print 'Offering Service...'
def SpreadMsg(Client,Clients):
        while True:
                try:
                        msg=Client[0].recv(1024)
                        msg=Client[1]+':'+msg
                        print msg
                        for client in Clients:
                                if client is not Client:
                                        client[0].send(msg)
                except Exception:
                        Client[0].close()
                        Clients.remove(Client)
                        break
if __name__=='__main__':
    Client=list()
    while True:
        client,add=s.accept()
        print add[0]+' joined'
        Client=[client,add[0]]
        threading.Thread(target=SpreadMsg,args=(Client,Clients,)).start()
        Clients.append(Client)