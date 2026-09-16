import socket


class Listener:
    def __init__(self, host, port, backlog=1000):
        self.seeker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.seeker.bind((host, port))
        self.backlog = backlog

    def start(self):
        self.seeker.listen()

    def stop(self):
        self.seeker.close()

    def accept(self):
        return self.seeker.accept()

    def __repr__(self):
        print(
            f"Listener (port={self.seeker.getpeername()[1]}, host={self.seeker.getpeername()[0]}, backlog={self.backlog})"
        )

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.stop()
