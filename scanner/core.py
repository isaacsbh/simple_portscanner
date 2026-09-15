import socket

def scan_ports(address, min_port, max_port):
    open_ports= []
    for port in range(min_port, max_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        connection_status = s.connect_ex((address, port))

        if connection_status== 0:
            try:
                banner= s.recv(1024).decode(errors="ignore").strip()
            except socket.timeout:
                banner = None

            open_ports.append((port,banner))

        s.close()
    return open_ports





