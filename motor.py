from multiprocessing import Process, Value
import threading, time

class Motor:
  def startController(self, q):
    speed = Value('d', 0.0)
    run_process = Process(target=self.start, args=( speed, ))
    run_process.start()
    done = False
    while (not done):
      m = q.get()
      if m == "quit":
        speed.value = -1
        done = True
      else:
        speed.value = float(m)
        
  def start(self, speed):
    done = False
    while (not done):
      time.sleep(1)
      if speed.value < 0:
        done = True
      else:
        print("Motor is now at speed: " + str(speed.value))
