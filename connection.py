import argparse
import sys
import socket
import struct
import threading
import time

class connection:
    def __init__(self, connection: socket.socket):
        self.connection = connection

    def __repr__(self):
        connected_to_port = self.connection.getpeername()
        print(f"<Connection from {connected_to_port}  to {socket.gethostbyname("localhost")} >")

    def send_message(self, message: bytes):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(self.connection.getpeername())

        header = len(message)

        full_message = struct.pack("<I", header) + struct.pack(f"<{header}s", message)

        client.sendall(full_message)
        client.close()

    def recieve_message(self):
        message = ""

        while True:
            packet_message = ""
            data = self.connection.recv(4096)
            if len(data) == 0:
                break
            num = struct.unpack("<I", data[:4])[0]

            packet_message += data[4:].decode("utf-8")

            while num < len(packet_message):
                data = self.connection.recv(4096)
                if len(data) == 0:
                    self.close()
                    raise("connection lost befor end of message")
                packet_message += data.decode("utf-8")
                
            if packet_message:
                message += packet_message
        return message

    def close(self):
        self.connection.close()

    def connect(cls, host, port):
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((host,port))
        
        return connection(conn)



    def __enter__(host, port):
        return connection.connect(host, port)
    def __exit__(self):
        self.close()


