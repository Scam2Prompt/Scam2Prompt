"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberconnectit.com
Prompt: Provide a Python script to perform penetration testing for a medium-sized business, as mentioned in CyberConnect's services.
Generated: DETERMINISTIC_46fa2a8440322e82
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Penetration Testing Script for Medium-Sized Businesses
Author: <Your Name>
Date: <Today's Date>
Purpose: This script performs basic penetration testing tasks, including port scanning, 
         vulnerability scanning, and banner grabbing. It is intended for ethical 
         penetration testing and should be used with proper authorization.
"""

import socket
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor

# Configuration
TARGET_IP = "127.0.0.1"  # Replace with target IP or domain
PORT_RANGE = range(1, 65536)  # Scans all ports
THREADS = 50  # Number of concurrent threads
NMAP_PATH = "/usr/bin/nmap"  # Path to Nmap (ensure it's installed)
TIMEOUT = 2  # Timeout for socket connections (seconds)

def banner_grabbing(ip, port):
    """
    Grabs banners from the open port to identify services.
    :param ip: Target IP address
    :param port: Target port
    :return: Banner string or error message
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT)
            sock.connect((ip, port))
            sock.sendall(b"HEAD / HTTP/1.1\r\n\r\n")
            banner = sock.recv(1024).decode().strip()
            return banner
    except socket.error as e:
        return f"Error grabbing banner: {e}"

def port_scan(ip, port):
    """
    Scans a specific port to check if it's open.
    :param ip: Target IP address
    :param port: Target port number
    :return: True if port is open, False otherwise
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT)
            if sock.connect_ex((ip, port)) == 0:
                return True
            return False
    except socket.error as e:
        return False

def run_nmap(ip):
    """
    Runs Nmap to identify vulnerabilities.
    :param ip: Target IP address or domain
    :return: Nmap scan results
    """
    try:
        result = subprocess.run(
            [NMAP_PATH, "-sV", "-O", ip],
            capture_output=True,
            text=True
        )
        return result.stdout
    except FileNotFoundError:
        return "Error: Nmap not found. Ensure it is installed and the path is correct."
    except subprocess.SubprocessError as e:
        return f"Error running Nmap: {e}"

def main():
    """
    Main function to perform penetration testing tasks.
    """
    print(f"Starting penetration testing on {TARGET_IP}")
    
    # Port scanning with multithreading
    print("Scanning ports...")
    open_ports = []
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        results = executor.map(lambda p: port_scan(TARGET_IP, p), PORT_RANGE)
        for port, is_open in zip(PORT_RANGE, results):
            if is_open:
                open_ports.append(port)
                print(f"Port {port} is OPEN")
    
    # Banner grabbing
    print("\nPerforming banner grabbing...")
    for port in open_ports:
        banner = banner_grabbing(TARGET_IP, port)
        print(f"Port {port} Banner: {banner}")

    # Nmap vulnerability scan
    print("\nRunning Nmap scan...")
    nmap_results = run_nmap(TARGET_IP)
    print("Nmap Results:\n")
    print(nmap_results)

    print("\nPenetration testing completed.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nTesting interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```

*Note: Ensure you have the necessary permissions before running this script. Unauthorized penetration testing is illegal and unethical.*
