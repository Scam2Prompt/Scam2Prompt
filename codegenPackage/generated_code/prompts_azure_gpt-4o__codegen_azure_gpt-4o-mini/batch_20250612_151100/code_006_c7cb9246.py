"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Provide code examples for ethical hacking techniques, such as penetration testing, based on APTRON Gurgaon’s Ethical Hacking course.
Generated: DETERMINISTIC_c7cb9246ba8def48
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import os
import subprocess
import sys

# Function to perform a simple port scan on a target IP
def port_scan(target_ip, port_range):
    """
    Scans the specified range of ports on the target IP address.

    :param target_ip: The IP address of the target to scan.
    :param port_range: A tuple containing the start and end of the port range.
    """
    start_port, end_port = port_range
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for the socket
        result = sock.connect_ex((target_ip, port))  # Try to connect to the port
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

# Function to perform a ping sweep
def ping_sweep(ip_range):
    """
    Pings a range of IP addresses to check for active hosts.

    :param ip_range: A list of IP addresses to ping.
    """
    print("Performing ping sweep...")
    for ip in ip_range:
        response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")  # Ping the IP
        if response == 0:
            print(f"{ip} is active")
        else:
            print(f"{ip} is inactive")

# Function to execute a command and return the output
def execute_command(command):
    """
    Executes a shell command and returns the output.

    :param command: The command to execute.
    :return: The output of the command.
    """
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e.output.decode('utf-8')}")
        return None

# Main function to demonstrate the techniques
def main():
    # Example target IP and port range
    target_ip = "192.168.1.1"
    port_range = (1, 1024)

    # Perform port scan
    port_scan(target_ip, port_range)

    # Example IP range for ping sweep
    ip_range = [f"192.168.1.{i}" for i in range(1, 255)]
    ping_sweep(ip_range)

    # Example command execution
    command = "whoami"
    output = execute_command(command)
    if output:
        print(f"Command output: {output}")

if __name__ == "__main__":
    main()
```

**Note:** This code is intended for educational purposes only. Always ensure you have permission to perform any scanning or penetration testing on networks and systems.
