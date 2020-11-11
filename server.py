import socket
import threading
import zlib
import mss

WIDTH = 768 #default
HEIGHT = 432 #default

def setup():
    print()
    print("Before starting the server, complete the setup: ")
    global WIDTH
    global HEIGHT
    flag = input(f"Do you want to use default width and height as ({WIDTH},{HEIGHT}) (y/n): ")
    if flag == 'n' or flag == 'N':
        print("How much portion of the screen do you want to cover while screen-sharing: ")
        WIDTH = int(input("WIDTH: [would be covered from top-left corner] "))
        HEIGHT = int(input("HEIGHT: [would be covered from top-left corner] "))

def handle_client(conn, addr):
    print(f'Client connected [{addr}]')
    with mss.mss() as sct:
        rect = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}

        screenRecord = True
        while screenRecord:

            img = sct.grab(rect)

            pixels = zlib.compress(img.rgb, 6)

            size = len(pixels)

            size_len = (size.bit_length() + 7) // 8

            size_bytes = size.to_bytes(size_len, 'big')
            
            try:
                conn.send(bytes([size_len]))
                conn.send(size_bytes)
                conn.sendall(pixels)
            except:
                print(f'Client Disconnected [{addr}]')
                screenRecord = False

def start_server():
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 9999
    ADDR = (HOST, PORT)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    try:
        server.listen()
        print(f'Server started on {HOST}:{PORT}')

        connected = True
        while connected:
            conn, addr = server.accept()
            thread = threading.Thread(target = handle_client, args = (conn, addr))
            thread.start()
    
    finally:
        server.close()


if __name__ == "__main__":
    setup()
<<<<<<< HEAD
    start_server()
=======
    start_server()
>>>>>>> 0c78b019b8df831a4c9bbd0b23baa196ea57edab
