import socket
import time
import sys
import threading
startTime = time.time()

#doing the visual


print("-" * 50)
print("PORT SCANNER BY RED")
print("-" * 50)

print("PRESS 1 FOR IP")
print("PRESS 2 FOR WEBSITE")

dio = input()


def diod():
    if dio == "1":
      print("Enter ip")
      jojo = input()
    for port in range(1, 1001):
        try:
            s = socket.socket()
            res = s.connect((jojo, port))
            print("Port open at:", port)
            s.close()
        except:
            print("Port closed at:", port)
threading.threading.Thread(target=diod).start
print("Scan finished")
#time.Time() - start time
