import socket

def get_available_ports(address, min_port, max_port):
    open_ports= []
    for port in range(min_port, max_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        connection_status = s.connect_ex((address, port))
        if connection_status== 0:
            open_ports.append(port)
        s.close()
    return open_ports





