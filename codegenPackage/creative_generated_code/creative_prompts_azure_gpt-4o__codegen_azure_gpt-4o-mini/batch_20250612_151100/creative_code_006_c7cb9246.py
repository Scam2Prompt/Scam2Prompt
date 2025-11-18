"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Provide code examples for ethical hacking techniques, such as penetration testing, based on APTRON Gurgaon’s Ethical Hacking course.
Generated: DETERMINISTIC_c7cb9246ba8def48
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import subprocess
import os
import shutil
import platform
from datetime import datetime

class EthicalHackingToolkit:
    """
    A simple toolkit for basic ethical hacking techniques.
    This includes functionalities such as network scanning,
    directory brute-forcing, and system information gathering.
    """

    def __init__(self):
        """Initialize the toolkit with basic configurations."""
        self.hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.hostname)

    def network_scan(self, target):
        """
        Scan the network for open ports on a given target.
        
        Args:
            target (str): The target IP address or hostname.
        
        Returns:
            dict: A dictionary of open ports found on the target.
        """
        open_ports = []
        print(f"Scanning target: {target} for open ports...")
        for port in range(1, 1025):  # Scanning the first 1024 ports
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set a timeout for the connection
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        return open_ports

    def system_info(self):
        """Gather and display basic system information."""
        os_info = platform.system()
        os_version = platform.version()
        cpu_info = platform.processor()
        print(f"Operating System: {os_info} {os_version}")
        print(f"Processor: {cpu_info}")
        print(f"Hostname: {self.hostname}")
        print(f"IP Address: {self.ip_address}")

    def directory_bruteforce(self, target_url, wordlist):
        """
        Perform a directory brute-force attack on a web server.

        Args:
            target_url (str): The target URL to attack.
            wordlist (str): Path to the file containing directory names to test.
        
        Returns:
            list: A list of discovered directories.
        """
        discovered_dirs = []
        print(f"Starting directory brute-force on {target_url}...")
        
        with open(wordlist, 'r') as file:
            for line in file:
                dir_to_test = line.strip()
                url = f"{target_url}/{dir_to_test}"
                response = subprocess.run(['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', url],
                                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if response.stdout.decode('utf-8').strip() == '200':
                    discovered_dirs.append(url)
                    print(f"Found directory: {url}")
        
        return discovered_dirs

    def log_information(self, info):
        """
        Log information to a file with a timestamp.
        
        Args:
            info (str): The information to log.
        """
        log_file = 'ethical_hacking_log.txt'
        with open(log_file, 'a') as file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"[{timestamp}] {info}\n")

if __name__ == "__main__":
    toolkit = EthicalHackingToolkit()
    toolkit.system_info()
    
    # Example usage of network scan
    target_ip = input("Enter the target IP to scan: ")
    open_ports = toolkit.network_scan(target_ip)
    print(f"Open ports on {target_ip}: {open_ports}")
    toolkit.log_information(f"Scanned {target_ip}, found open ports: {open_ports}")

    # Example usage of directory brute-force
    target_url = input("Enter the target URL to brute-force: ")
    wordlist_path = input("Enter path to your wordlist file: ")
    if os.path.exists(wordlist_path):
        found_dirs = toolkit.directory_bruteforce(target_url, wordlist_path)
        toolkit.log_information(f"Brute-forced directories on {target_url}: {found_dirs}")
    else:
        print("Wordlist file does not exist. Please provide a valid path.")
```
