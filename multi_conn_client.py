import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()
messages = [b"Message 1 from client.", b"Message 2 from client."]

def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(num_conns):
        connid = i + 1
        print(f"starting connection {connid} to {server_addr}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ  | selectors.EVENT_WRITE
        data = types.SimpleNamespace(
            connid=connid,
            msg_total=sum(len(msg) for msg in messages),
            recv_total=0,
            messages=messages.copy(),
            outb=b""
        )
        sel.register(sock, events, data=data)


host, port, num_conns = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
start_connections(host, port, num_conns)
