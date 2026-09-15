import sys
from scanner.core import scan_ports

def main (argv): 
    address = sys.argv[1]
    min_port = int(sys.argv[2])
    max_port = int(sys.argv[3])
    ports = scan_ports(address, min_port, max_port)
    for p in ports: 
        print(p)



if __name__ == "__main__":
    main(sys.argv)


