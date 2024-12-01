import socket  # noqa: F401
import threading



def main():

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    connection, _= server_socket.accept()
    while connection.recv(1024):
        connection.sendall(b"+PONG\r\n")
        thread = threading.Thread(target=connect, args=[connection,address])
        thread.start()

def connect(connect: socket.socket):


if __name__ == "__main__":
    main() 2 vb 7