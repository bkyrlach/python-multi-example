from multiprocessing import Process, Queue, Lock
import threading, time
import lights;
import motor;

lq = Queue()
mq = Queue()
lights = lights.Lights()
motor = motor.Motor()

if __name__ == '__main__':
  print("Hello")

  light_process = Process(target=lights.start, args=( lq, ))
  light_process.start()

  motor_process = Process(target=motor.startController, args=(mq, ))
  motor_process.start()

  done = False
  while (not done):
    time.sleep(1)
    command = raw_input("Lights or motor?")
    if command == "lights":
      color = raw_input("What color should we make the lights? ")
      lq.put(color)
    elif command == "motor":
      speed = raw_input("What speed should we set the motor to? ")
      mq.put(speed)
    elif command == "quit":
      lq.put("quit")
      mq.put("quit")
      time.sleep(5)
      done = True
    else:
      print("I didn't recognize that command.")
