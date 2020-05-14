import socket
from _thread import *
import pickle

SERVER = "192.168.1.209"
PORT = 5558

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((SERVER, PORT))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Stared!")

connected = set()
games = {}
idCount = 0


def threaded_client(conn, p):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if not data:
                break
            else:
                if data == "reset":
                    print("received reset")
                    # game.reset_went()
                elif data == "get":
                    print("received get")
                    # game.play(p, data)
                elif data == "exit":
                    print("received exit")
                    break
                else:
                    print("received garbage")

                #reply = game
                conn.sendall(str.encode(f"Sending a response to: {data}"))
        except:
            break

    print("Lost connection")
    try:
        print("Closing game ", addr)
    except:
        pass
    conn.close()


player_number = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, player_number))
    player_number += 1
