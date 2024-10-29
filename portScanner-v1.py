import socket

def port_scanner(target_ip, port_range=(1, 1024)):
    open_ports = []
    start_port, end_port = port_range

    print(f"Scanning {target_ip} for open ports in range {start_port}-{end_port}...")
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Time Break(0.5)
        
        result = sock.connect_ex((target_ip, port))  # Connection Control
        if result == 0:
            open_ports.append(port)
            print(f"[+] Port {port} is open")
        
        sock.close()
    
    if not open_ports:
        print("No open ports found.")
    else:
        print(f"Open ports: {open_ports}")

# USE
target_ip = "127.0.0.1"  # Target ip Adr.
port_scanner(target_ip, port_range=(1, 1024))  # Target Ports (1-1024)
