import Tkinter as Tk
import socket
import threading
import sys
reload(sys)
sys.setdefaultencoding('utf8')
if __name__=='__main__':
    s=socket.socket()
    host=raw_input('input the hostIP:')
    port=raw_input('input the port:')
    s.connect((host,int(port)))
    root=Tk.Tk('ClientGUI')
    root.geometry('500x500')
    root.config()
    text=Tk.Text(root,state='disable',width=300)
    entry=Tk.Entry(root,width=300)
    text.pack()
    entry.pack()
    def recv():
        while True:
            msg=s.recv(1024)
            text.config(state='normal')
            text.insert('end',msg+'\n')
            entry.delete(0,len(msg))
            text.config(state='disable')
    threading.Thread(target=recv,args=()).start()
    def entrySend():
        msg=entry.get()
        s.send(msg)
        text.config(state='normal')
        text.insert('end',msg+'\n')
        entry.delete(0,len(msg))
        text.config(state='disable')
        return msg
    def msgEnter(event):
        if event.keysym=='Return':
            entrySend()
    btn=Tk.Button(root,width=10,text='send',command=entrySend)
    btn.pack()
    root.bind('<Key>',msgEnter)
    while True:
        root.mainloop()