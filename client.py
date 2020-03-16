from multiprocessing import Process
import socket;
import time;

class Client:

    def send(self, s):
        done = False
        while (not done):
            time.sleep(10)
            s.send("Test message")
            
    def recv(self, s):
        done = False
        while (not done):
            data = s.recv(1024)
            if((not data) or (data[0] == 120)):
                done = True
            else:
                print(data)

if __name__ == '__main__':
    c = Client()

    print("Hello")
    s = socket.socket()
    s.connect(("localhost", 1234))

    time.sleep(1)
    
    sp = Process(target=c.send, args=( s, ))
    sp.start()

    rp = Process(target=c.recv, args=( s, ))
    rp.start()