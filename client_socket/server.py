import argparse
import sys
import socket
import struct

###########################################################
####################### YOUR CODE #########################
###########################################################


def run_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()

    while True:
        conn, addr = server.accept()
        message = ""
        while True:
            data = conn.recv(4096)
            if not data:
                break
            message += struct.unpack("<", data)
            print(f"From client: {message}")
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
