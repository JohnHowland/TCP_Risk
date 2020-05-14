from network import Network
from UI import Board
from _thread import *
import time


def main():
    run = True
    #    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player: ", player)

    while run:
        try:
            reply = n.send("get")
            print(reply)
        except:
            run = False
            print("Couldn't get game.")
            break

        try:
            reply = n.send("reset")
            print(reply)
        except:
            run = False
            print("Couldn't get game.")
            break

        time.sleep(10)
        run = False

    reply = n.send("exit")
    print(reply)

lol = Board()
#lol.display()
print("before new thread")
start_new_thread(lol.display, ())
print("after new thread")
main()
