import socket
import time


def echo_client():
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            try:
                s.sendall(b"Hello, world")
                data = s.recv(1024)
                print(f"Received {data!r}")
                time.sleep(3)
            except KeyboardInterrupt:
                print("caught keyboard interrupt, exiting")
                break
        s.close()


if __name__ == "__main__":
    echo_client()
