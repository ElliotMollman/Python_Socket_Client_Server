import socket
def send_data(dest_ip, dest_port):
    print(f"sending message to {dest_ip}:{dest_port}...\n")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCP_sock:
            # socket.AF_INET tells python the address family we are using, which is ipv4. We can use socket.AF_INET6 for ipv6 addresses.
            # SOCK_STREAM is the socket type for TCP, and the timeout for packets is specified as 10 seconds.
            TCP_sock.connect((dest_ip, dest_port))
            # .connect() will keep connection alive until closed.
            TCP_sock.settimeout(5)
            message = input("Enter message to send: \n")
            TCP_sock.sendall(message.encode('utf-8'))
            print("waiting for reply...\n")
            data = TCP_sock.recv(1024)
            print(data.decode('utf-8'))
            # This method repeatedly calls socket.send() internally until all of the bytes data has been sent, or an error occurs.
            # It also handles the partial sends automatically.
    except:
        print("failed to connect")


dest_port = 5132
dest_ip = '127.0.0.1'
send_data(dest_ip, dest_port)
