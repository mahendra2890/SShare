import socket
import zlib
import pygame

WIDTH = 768 # default
HEIGHT = 432 # default
HOST = "0.0.0.0" # default
PORT = 9999 # default

def setup():
    global WIDTH 
    global HEIGHT
    global HOST
    print()
    print("To connect to server, complete the setup: ")
    print()
    HOST = input("Enter the IP address of server (IPv4): ")
    print()
    print("Enter the dimension [should be same as server]")
    WIDTH = int(input("WIDTH: "))
    HEIGHT = int(input("HEIGHT: "))

def getAll(conn, length):
    buffer = b''
    while len(buffer) < length:
        data = conn.recv(length - len(buffer))
        if not data:
            return data
        buffer += data
    return buffer

def connect_to_server():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    clock = pygame.time.Clock()   

    ADDR = (HOST, PORT)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect(ADDR)
        watching = True
        while watching:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break
            size_len = int.from_bytes(server.recv(1), byteorder='big')

            size = int.from_bytes(server.recv(size_len), byteorder='big')
            
            pixels = zlib.decompress(getAll(server, size))
            
            img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')
            
            screen.blit(img, (0, 0))
            
            pygame.display.flip()
            
            clock.tick(60)
    finally:
        server.close()

if __name__ == '__main__':
    setup()
    connect_to_server()
