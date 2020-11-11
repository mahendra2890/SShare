import socket
import zlib
import pygame

WIDTH = 768 # default
HEIGHT = 432 # default
<<<<<<< HEAD
HOST = "127.0.1.1" # default
=======
HOST = "0.0.0.0" # default
>>>>>>> 0c78b019b8df831a4c9bbd0b23baa196ea57edab
PORT = 9999 # default

def setup():
    global WIDTH 
    global HEIGHT
    global HOST
    print()
    print("To connect to server, complete the setup: ")
    print()
<<<<<<< HEAD
    
    # HOST = input("Enter the IP address of server (IPv4): ")
    # print()
    # print("Enter the dimension [should be same as server]")
    # WIDTH = int(input("WIDTH: "))
    # HEIGHT = int(input("HEIGHT: "))
=======
    HOST = input("Enter the IP address of server (IPv4): ")
    print()
    print("Enter the dimension [should be same as server]")
    WIDTH = int(input("WIDTH: "))
    HEIGHT = int(input("HEIGHT: "))
>>>>>>> 0c78b019b8df831a4c9bbd0b23baa196ea57edab

def getAll(conn, length):
    buffer = b''
    while len(buffer) < length:
        data = conn.recv(length - len(buffer))
        if not data:
            return data
        buffer += data
    return buffer
<<<<<<< HEAD

def connect_to_server():
    global WIDTH 
    global HEIGHT
    global HOST

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    fake_screen = screen.copy()

=======

def connect_to_server():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
>>>>>>> 0c78b019b8df831a4c9bbd0b23baa196ea57edab
    clock = pygame.time.Clock()   

    ADDR = (HOST, PORT)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect(ADDR)
        watching = True
<<<<<<< HEAD
        lHEIGHT = HEIGHT
        lWIDTH = WIDTH
=======
>>>>>>> 0c78b019b8df831a4c9bbd0b23baa196ea57edab
        while watching:
            # pygame.event.pump()
            
            size_len = int.from_bytes(server.recv(1), byteorder='big')

            inpsize = int.from_bytes(server.recv(size_len), byteorder='big')
            
            pixels = zlib.decompress(getAll(server, inpsize))
            
            img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')
            
            fake_screen.blit(img, (0, 0))
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break
<<<<<<< HEAD
                elif event.type == pygame.VIDEORESIZE:
                    print(event.dict['size'])
                    lWIDTH,lHEIGHT = event.dict['size']
            # fake_screen = screen.copy()
            
            # screen.blit(pygame.transform.scale(fake_screen, event.dict['size']), (0, 0))
            ake_screen = pygame.transform.scale(fake_screen, (lWIDTH, lHEIGHT))
            ke_screen = pygame.transform.scale(ake_screen, (WIDTH, HEIGHT))
            
            screen.blit(ke_screen,(0,0))
=======
            size_len = int.from_bytes(server.recv(1), byteorder='big')

            size = int.from_bytes(server.recv(size_len), byteorder='big')
            
            pixels = zlib.decompress(getAll(server, size))
            
            img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')
            
            screen.blit(img, (0, 0))
>>>>>>> 0c78b019b8df831a4c9bbd0b23baa196ea57edab
            
            pygame.display.flip()
            
            clock.tick(60)
<<<<<<< HEAD
    

=======
>>>>>>> 0c78b019b8df831a4c9bbd0b23baa196ea57edab
    finally:
        server.close()

if __name__ == '__main__':
    setup()
    connect_to_server()
