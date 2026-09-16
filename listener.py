import socket

class listener:
    def __init__(self, host, port, backlog=1000):
        self.seeker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.seeker.bind((host,port))

    def start(self):
        self.seeker.listen()

    def stop(self):
        self.seeker.close()

    def accept(self):
        return self.seeker.accept()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.stop()