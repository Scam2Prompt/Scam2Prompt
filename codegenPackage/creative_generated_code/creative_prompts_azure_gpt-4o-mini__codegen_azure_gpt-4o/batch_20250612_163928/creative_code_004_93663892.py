"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nabberx.com
Prompt: Illustrate how to implement network security measures and firewalls in a business environment, using the guidelines from NabberX’s offerings.
Generated: DETERMINISTIC_936638924d006ef0
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Network Security Implementation Script

This script demonstrates how to implement basic network security measures 
and firewalls in a business environment using NabberX's offerings.

The code utilizes Python's `socket` and `ipaddress` libraries for 
network operations and includes features such as IP whitelist/blacklist,
port filtering, and logging of blocked access attempts.

Prerequisites:
- Install `pyiptables` library for managing iptables (Linux firewall rules).
- Python 3.x is required.
"""

import socket
import ipaddress
import logging
import os

# Configure logging
LOG_FILE = "firewall_activity.log"
logging.basicConfig(
    filename=LOG_FILE,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# NabberX's offerings: IP whitelist and blacklist
IP_WHITELIST = {"192.168.1.10", "192.168.1.20"}  # Trusted IPs within the business network
IP_BLACKLIST = {"192.168.1.99"}  # Suspicious or malicious IPs

# Define allowed ports (business-critical services)
ALLOWED_PORTS = {80, 443, 22}  # HTTP, HTTPS, and SSH

# Utility function: Check if an IP is valid
def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


# Firewall rule: Block IPs in blacklist
def configure_blacklist():
    for ip in IP_BLACKLIST:
        if is_valid_ip(ip):
            os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
            logging.info(f"Blocked IP: {ip}")
        else:
            logging.error(f"Invalid IP in blacklist: {ip}")


# Firewall rule: Allow only whitelisted IPs
def configure_whitelist():
    for ip in IP_WHITELIST:
        if is_valid_ip(ip):
            os.system(f"sudo iptables -A INPUT -s {ip} -j ACCEPT")
            logging.info(f"Allowed IP: {ip}")
        else:
            logging.error(f"Invalid IP in whitelist: {ip}")


# Firewall rule: Block non-approved ports
def configure_port_filtering():
    os.system("sudo iptables -A INPUT -j DROP")  # Default to block all traffic
    for port in ALLOWED_PORTS:
        os.system(f"sudo iptables -A INPUT -p tcp --dport {port} -j ACCEPT")
        logging.info(f"Allowed port: {port}")


# Monitor incoming connections and log blocked attempts
def monitor_connections():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 8080))  # Bind to an arbitrary monitoring port
    server_socket.listen(5)

    logging.info("Monitoring incoming connections...")
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            ip, port = client_address
            logging.info(f"Connection attempt from {ip}:{port}")

            if ip in IP_BLACKLIST or port not in ALLOWED_PORTS:
                logging.warning(f"Blocked connection from {ip}:{port}")
                client_socket.close()
            else:
                logging.info(f"Allowed connection from {ip}:{port}")
                client_socket.close()
        except Exception as e:
            logging.error(f"Error during connection monitoring: {e}")


# Main function: Setup firewall rules and monitor network
def main():
    logging.info("Starting firewall configuration...")
    try:
        configure_blacklist()
        configure_whitelist()
        configure_port_filtering()
        monitor_connections()  # Continuous monitoring
    except Exception as e:
        logging.error(f"Error during firewall setup: {e}")
    finally:
        logging.info("Firewall configuration complete.")


if __name__ == "__main__":
    main()
```
