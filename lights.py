class Lights:
  def start(self, q):
    done = False
    while (not done):
      m = q.get()
      if m == "quit":
        done = True
      else:
        print("Lights are now: " + m)
