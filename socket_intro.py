import sys
import socket


# Create a TCP/IPv4 socket
def get_socket():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return sock
    except socket.error as err:
        print(f'{err}: There was an error creating the socket')


# find the hostname of the server
def get_host_by_name(host_name):
    try:
        host_ip = socket.gethostbyname(host_name)
        print(host_ip)
        return host_ip
    except socket.gaierror:
        print('There was an error resolving the host')


def connect_to_server(sock, host, port):
    try:
        sock.connect((host, port))
        return True
    except socket.error as err:
        print(f'{err}: There was an error connecting to the server')
        return False


# connect to google.com on port 80
def google():
    host = "www.google.com"
    port = 80
    sock = get_socket()
    host_ip = get_host_by_name(host)
    connected = connect_to_server(sock, host_ip, port)
    if connected:
        print(f'Connected to {host} on port {port}')
    else:
        print('Connection failed')


# bind the socket to the host and port
def create_server(host="", port=65432):
    # a server socket is created and bound to a host and port
    # a server socket does not send or receive data, it produces client sockets, which do

    # Create a TCP/IPv4 socket
    sock = get_socket()
    # Bind the socket to the host and port
    sock.bind((host, port))
    # Listen for incoming connections
    # The argument to listen is the number of unaccepted connections that the system will
    # allow before refusing new connections
    sock.listen(5)
    print(f'Listening on {host} on port {port}')

    while True:
        # Accept a connection
        # conn is a new socket object usable to send and receive data on the connection
        # addr is the address bound to the socket on the other end of the connection
        conn, addr = sock.accept()
        print(f'Connected by {addr}')
        conn.send(b'Hello, world')
        conn.close()
        break


class MySocket:
    MSGLEN = 8192

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        total_sent = 0
        while total_sent < self.MSGLEN:
            sent = self.sock.send(msg[total_sent:])
            # message is sent in chunks
            # message completely sent
            if sent == 0:
                raise RuntimeError("socket connection broken")
            total_sent = total_sent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < self.MSGLEN:
            chunk = self.sock.recv(min(self.MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("Socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)
