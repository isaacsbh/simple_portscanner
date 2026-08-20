import sys
from scanner.core import get_available_ports

def main (argv): 
    address = sys.argv[1]
    min_port = int(sys.argv[2])
    max_port = int(sys.argv[3])
    ports = get_available_ports(address, min_port, max_port)
    for p in ports: 
        print(p)



if __name__ == "__main__":
    main(sys.argv)


