import socket;
from multiprocessing import Process

class Comms:
    def start(self, sq):
        s = socket.socket()
        s.bind(("", 1234))
        s.listen(1)
        while (True):
            (cs, _) = s.accept()
            client_proc = Process(target=self.handle, args=( cs, sq, ))
            client_proc.start()

    def handle(self, cs, sq):
        lp = Process(target=self.listen, args=( sq, cs, ))
        lp.start()
        done = False
        while (not done):
            data = cs.recv(1024)
            if((not data) or (data[0] == 120)):
                done = True
            else:
                print(data)

    def listen(self, sq, cs):
        done = False
        while(not done):
            data = sq.get()
            print("Got here")
            cs.send(data)
