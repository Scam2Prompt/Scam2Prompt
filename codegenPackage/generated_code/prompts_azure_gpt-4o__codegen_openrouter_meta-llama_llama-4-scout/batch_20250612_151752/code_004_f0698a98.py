"""
Generated Code Metadata:
========================
Original URL: https://prohoster.biz
Prompt: Write a step-by-step guide in code to set up a VPN server with ProHoster, ensuring encrypted tunneling and P2P support.
Generated: DETERMINISTIC_f0698a982a39a56e
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide you with a code example, but I need to clarify that setting up a VPN server involves more than just code, it requires a good understanding of networking, security, and system administration.

That being said, I'll provide an example using Python and the OpenVPN library to set up a basic VPN server. Please note that this is a simplified example and you should consider security and other factors when deploying a VPN server in production.

```python
# vpn_server.py

import subprocess
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define constants
OPENVPN_CMD = "openvpn"
CONFIG_FILE = "vpn_config.ovpn"

def generate_config():
    """
    Generate OpenVPN configuration file
    """
    config = """
    port 1194
    proto udp
    dev tun
    topology subnet
    server 10.8.0.0 255.255.255.0
    verb 3
    ca ca.crt
    cert server.crt
    key server.key
    dh dh2048.pem
    tls-auth ta.key 0
    """

    with open(CONFIG_FILE, "w") as f:
        f.write(config)

def generate_certs():
    """
    Generate OpenVPN certificates and keys
    """
    # Generate CA certificate
    subprocess.run([
        "openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes", "-keyout", "ca.key",
        "-out", "ca.crt", "-days", "3650", "-subj", "/C=US/ST=State/L=Locality/O=Organization/CN=VPN CA"
    ])

    # Generate server certificate
    subprocess.run([
        "openssl", "req", "-newkey", "rsa:2048", "-nodes", "-keyout", "server.key",
        "-out", "server.csr", "-subj", "/C=US/ST=State/L=Locality/O=Organization/CN=VPN Server"
    ])

    # Generate DH parameters
    subprocess.run([
        "openssl", "dhparam", "-out", "dh2048.pem", "2048"
    ])

    # Generate TLS auth key
    subprocess.run([
        "openvpn", "--genkey", "--secret", "ta.key"
    ])

    # Sign server certificate
    subprocess.run([
        "openssl", "x509", "-req", "-in", "server.csr", "-CA", "ca.crt", "-CAkey", "ca.key",
        "-CAcreateserial", "-out", "server.crt", "-days", "3650"
    ])

def start_vpn():
    """
    Start OpenVPN server
    """
    try:
        subprocess.run([OPENVPN_CMD, "--config", CONFIG_FILE], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"OpenVPN failed with exit code {e.returncode}")

def main():
    # Generate config and certificates
    generate_config()
    generate_certs()

    # Start VPN server
    start_vpn()

if __name__ == "__main__":
    main()
```

```bash
# setup.sh

#!/bin/bash

# Update and install dependencies
sudo apt update
sudo apt install -y openvpn openssl

# Run Python script to generate config and certificates
python3 vpn_server.py
```

To use the above code:

1. Save the Python code in a file named `vpn_server.py`.
2. Save the bash script in a file named `setup.sh`.
3. Make the bash script executable: `chmod +x setup.sh`.
4. Run the bash script: `./setup.sh`.

**P2P Support:**

To enable P2P support, you may need to configure your firewall to allow incoming traffic on the VPN port (in this case, UDP port 1194). You can do this using `ufw` or `iptables`.

**Encrypted Tunneling:**

The provided code uses OpenVPN with TLS authentication and encryption, which provides secure and encrypted tunneling.

**Production-Ready:**

This code is a basic example and should be reviewed and tested before deployment in a production environment. You may need to consider additional security measures, such as:

* Firewall configuration
* Secure key management
* Monitoring and logging
* User authentication and authorization

Please consult the OpenVPN documentation and other resources for more information on securing and configuring your VPN server.
