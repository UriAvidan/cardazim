import argparse
import socket
import struct
import sys

from connection import Connection

###########################################################
####################### YOUR CODE #########################
###########################################################


def send_data(server_ip, server_port, data):

    with Connection.connect(Connection, server_ip, server_port) as client:
        data = bytes(data, "utf-8")

        client.send_message(data)



###########################################################
##################### END OF YOUR CODE ####################
###########################################################


def get_args():
    parser = argparse.ArgumentParser(description="Send data to server.")
    parser.add_argument("server_ip", type=str, help="the server's ip")
    parser.add_argument("server_port", type=int, help="the server's port")
    parser.add_argument("data", type=str, help="the data")
    return parser.parse_args()


def main():
    """
    Implementation of CLI and sending data to server.
    """
    args = get_args()
    send_data(args.server_ip, args.server_port, args.data)


if __name__ == "__main__":
    sys.exit(main())
