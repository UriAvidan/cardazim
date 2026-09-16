import argparse
import sys
import socket
import struct
import threading
import time


class Connection:
    def __init__(self, connection: socket.socket):
        self.connection = connection

    def __repr__(self):
        connected_to_port = self.connection.getpeername()
        print(
            f"<Connection from {connected_to_port}  to {socket.gethostbyname('localhost')} >"
        )

    def send_message(self, message: bytes):
        header = len(message)
        full_message = struct.pack("<I", header) + struct.pack(f"<{header}s", message)
        self.connection.sendall(full_message)

    def recieve_message(self):
        message = b""

        while True:
            packet_message = b""
            num = self.connection.recv(4)
            if not num:
                break
            num = struct.unpack("<I", num)[0]

            while num > len(packet_message):
                data = self.connection.recv(num - len(packet_message))
                if len(data) == 0:
                    raise Exception("Connection lost before end of message")
                packet_message += data

            if packet_message:
                message += packet_message
        return message.decode("utf-8")

    def close(self):
        print("connection closed")
        self.connection.close()

    def connect(cls, host, port):
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((host, port))

        return Connection(conn)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()
