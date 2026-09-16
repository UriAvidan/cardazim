import argparse
import sys
import socket
import struct
import threading
import time
import connection
import listener
###########################################################
####################### YOUR CODE #########################
###########################################################


def run_server(ip, port):

    with listener.Listener(ip, port) as server:
        connections = {}
        while True:
            conn, addr = server.accept()
            if not addr in connections.items():
                connections[conn] = addr
            t = threading.Thread(target=handle_client, args=(conn, addr))
            t.start()



def handle_client(conn, addr):
    with connection.Connection(conn) as c:
        print(c.recieve_message())



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
    run_server(args.server_ip, args.server_port)


if __name__ == "__main__":
    sys.exit(main())
