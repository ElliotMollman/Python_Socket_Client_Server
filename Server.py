import socket
def receive_data(host, server_port, reply):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCP_sock:
		# socket.AF_INET tells python the address family we are using, which is ipv4. We can use socket.AF_INET6 for ipv6 addresses.
		# SOCK_STREAM is the socket type for TCP, and the timeout for packets is specified
		TCP_sock.bind((host, server_port))
		# Will bind to itself to the client host and port we want to listen to.
		TCP_sock.listen(5)
		print(f"listening for connections...on port {server_port}\n")
		# Open to connections, with a maximum of 5 at once. No other processes will run while waiting for a connection
		conn, client_addr = TCP_sock.accept()
		with conn:
			conn.settimeout(5)
			#This method controls how long the socket will wait for an operation \(like connect(), recv(), or send()) to complete.
			print(f"Connected to: {client_addr}")
			while True:
				try:
					data = conn.recv(2048)
					if data:
						print("Data from Client: " + data.decode('utf-8'))
						# Receiving a maximum of 1 kilobyte of data from client. The recv() function is blocking by default like listen().
					elif not data:
						# If the server doesn't receive any data, then it terminates the connection.
						break
					conn.sendall(reply.encode('utf-8'))	
				except socket.timeout:
					print("Receive time out.")
					conn.close()
					break
host = ""
# Empty string will accet any incoming ip connection
server_port = 5132
reply = 'Server: connection finished. Disconnecting........'
while True:
	receive_data(host, server_port, reply)
	# Continuous loop for listening to connections.
