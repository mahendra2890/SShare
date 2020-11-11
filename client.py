import socket
import zlib
import pygame

WIDTH = 1366 # default
HEIGHT = 768 # default
HOST = "127.0.1.1" # default
PORT = 9999 # default


def setup():
    global WIDTH 
    global HEIGHT
    global HOST
    print()

def getAll(conn, length):
    buffer = b''
    while len(buffer) < length:
        data = conn.recv(length - len(buffer))
        if not data:
            return data
        buffer += data
    return buffer

def connect_to_server():
    global WIDTH 
    global HEIGHT
    global HOST

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    
    fake_screen = screen.copy()
    ake_screen = screen.copy()
    ke_screen = screen.copy()
    
    clock = pygame.time.Clock()   

    ADDR = (HOST, PORT)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect(ADDR)
        watching = True
        lHEIGHT = HEIGHT
        lWIDTH = WIDTH
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
                elif event.type == pygame.VIDEORESIZE:
                    print(event.dict['size'])
                    lWIDTH,lHEIGHT = event.dict['size']
            
            screen.blit(pygame.transform.scale(fake_screen, (lWIDTH,lHEIGHT)), (0, 0))
            pygame.display.flip()
            
            clock.tick(60)
    finally:
        server.close()

if __name__ == '__main__':
    setup()
    connect_to_server()
