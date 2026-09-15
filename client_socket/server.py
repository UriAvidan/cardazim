import argparse
import sys
import socket
import struct
import threading
import time
###########################################################
####################### YOUR CODE #########################
###########################################################


def run_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()
    connections = {}
    threads = []

    while True:
        conn, addr = server.accept()
        if not addr in connections.items():
            connections[conn] = addr
            t = threading.Thread(target=handle_client, args=(conn, addr))
            threads.append(t)
            t.start()


def handle_client(conn, addr):
    message = ""

    while True:
        packet_message = ""
        data = conn.recv(4096)
        if len(data) == 0:
            break
        num = struct.unpack("<I", data[:4])[0]
        packet_message += data[4:].decode("utf-8")
        while num < len(packet_message):
            data = conn.recv(4096)
            if len(data) == 0:
                break
            packet_message += data.decode("utf-8")
        if packet_message:
            message += packet_message
    print(f"From client: {message}")
    # time.sleep(5)
    conn.close()
    print("client disconnected")


###########################################################
##################### END OF YOUR CODE ####################
###########################################################


def get_args():
    parser = argparse.ArgumentParser(description="Send data to server.")
    parser.add_argument("server_ip", type=str, help="the server's ip")
    parser.add_argument("server_port", type=int, help="the server's port")
    return parser.parse_args()


def main():
    """
    Implementation of CLI and sending data to server.
    """
    args = get_args()
    try:
        run_server(args.server_ip, args.server_port)
    except Exception as error:
        print(f"ERROR: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
