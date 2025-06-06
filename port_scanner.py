import socket
import argparse

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is open")
            sock.close()
        except socket.error:
            print(f"[-] Couldn't connect to port {port}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple TCP port scanner.")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")
    args = parser.parse_args()

    scan_ports(args.target, args.start, args.end)
