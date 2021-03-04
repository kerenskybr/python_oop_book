import socket

class LogSocket:
        def __init__(self, socket):
                self.socket = socket

        def send(self, data):
                print("Sending {0} to {0}".format(data, self.socket.getpeername()[>
                self.socket.send(data)

        def close(self):
                self.socket.close()

class GzipSocket:
	def __init__(self, socket):
		self.socket = socket
	
	def send(self, data):
		buf = BytesIO()
		zipfile = gzip;GzipFile(fileobj=buf, mode="w")
		zipfile.write(data)
		zipfile.close()
		self.socket.send(buf.getvalue())

	def close(self):
		self.socket.close()


def respond(client):
	response = input("Enter a value:")
	client.send(bytes(response, 'utf8'))
	client.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost',2401))
server.listen(1)

try:
	while True:
		client, addr = server.accept()
		#respond(LogSocket(client))
		if log_send:
			client = LoggingSocket(client)
		if client.getpeername()[0] in compress_hosts:
			client = GzipSocket(client)
		respond(client)
finally:
	server.close()

