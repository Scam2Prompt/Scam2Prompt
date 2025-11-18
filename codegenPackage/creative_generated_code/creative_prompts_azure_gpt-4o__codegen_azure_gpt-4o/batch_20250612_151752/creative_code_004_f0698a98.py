"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prohoster.biz
Prompt: Write a step-by-step guide in code to set up a VPN server with ProHoster, ensuring encrypted tunneling and P2P support.
Generated: DETERMINISTIC_f0698a982a39a56e
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script that automates setting up a VPN server using OpenVPN on a Linux-based server. It includes encrypted tunneling and P2P support. This script assumes the server is hosted on ProHoster or any similar VPS provider.

```python
#!/usr/bin/env python3
"""
Script to automate the setup of an OpenVPN server on a Linux-based VPS.
Ensure that you have sudo privileges and this script is run on a clean server.
"""

import os
import subprocess

def run_command(command, description):
    """
    Run a shell command with error handling.

    Args:
        command (str): The shell command to execute.
        description (str): Description of the command for logging.

    Raises:
        RuntimeError: If the command fails, it raises an error.
    """
    print(f"Running: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error while {description}: {e.stderr}")
        raise RuntimeError(f"Command failed: {command}")

def setup_vpn():
    """
    Main function to set up OpenVPN on the server.
    """
    # Step 1: Update and upgrade the system
    run_command("sudo apt update && sudo apt upgrade -y", "updating and upgrading the system")

    # Step 2: Install necessary packages
    run_command("sudo apt install -y openvpn easy-rsa", "installing OpenVPN and Easy-RSA")

    # Step 3: Create the Easy-RSA directory and initialize PKI
    run_command("make-cadir ~/easy-rsa", "creating Easy-RSA directory")
    os.chdir(os.path.expanduser("~/easy-rsa"))  # Change to Easy-RSA directory
    run_command("./easyrsa init-pki", "initializing PKI")

    # Step 4: Build the certificate authority (CA)
    run_command("./easyrsa build-ca nopass", "building the certificate authority")

    # Step 5: Generate the server certificate and key
    run_command("./easyrsa gen-req server nopass", "generating server certificate and key")
    run_command("./easyrsa sign-req server server", "signing server certificate")

    # Step 6: Generate Diffie-Hellman parameters
    run_command("./easyrsa gen-dh", "generating Diffie-Hellman parameters")

    # Step 7: Generate HMAC key for packet integrity
    run_command("openvpn --genkey --secret ta.key", "generating HMAC key")

    # Step 8: Configure OpenVPN server settings
    vpn_config = """
port 1194
proto udp
dev tun
ca ~/easy-rsa/pki/ca.crt
cert ~/easy-rsa/pki/issued/server.crt
key ~/easy-rsa/pki/private/server.key
dh ~/easy-rsa/pki/dh.pem
tls-auth ta.key 0
server 10.8.0.0 255.255.255.0
ifconfig-pool-persist ipp.txt
keepalive 10 120
cipher AES-256-CBC
user nobody
group nogroup
persist-key
persist-tun
status openvpn-status.log
log /var/log/openvpn.log
verb 3
explicit-exit-notify 1
"""
    with open("/etc/openvpn/server.conf", "w") as config_file:
        config_file.write(vpn_config)
    print("OpenVPN server configuration written to /etc/openvpn/server.conf")

    # Step 9: Enable IP forwarding
    run_command("sudo sysctl -w net.ipv4.ip_forward=1", "enabling IP forwarding")
    with open("/etc/sysctl.conf", "a") as sysctl_conf:
        sysctl_conf.write("\nnet.ipv4.ip_forward=1\n")
    print("IP forwarding enabled permanently.")

    # Step 10: Configure firewall rules
    run_command("sudo ufw allow 1194/udp", "allowing UDP on port 1194")
    run_command("sudo ufw allow OpenSSH", "allowing OpenSSH")
    run_command("sudo ufw enable", "enabling the firewall")

    # Step 11: Start OpenVPN service
    run_command("sudo systemctl start openvpn@server", "starting OpenVPN server")
    run_command("sudo systemctl enable openvpn@server", "enabling OpenVPN server to start on boot")

    print("OpenVPN server setup complete!")

if __name__ == "__main__":
    setup_vpn()
```

### Notes:
- This script assumes the server is Ubuntu-based (Debian-based systems should work similarly).
- Ensure you have root privileges to run this script, as it requires `sudo` for several commands.
- You may need to modify firewall rules based on your specific ProHoster network configuration.

**Disclaimer**: Always follow your hosting provider's terms of service and ensure compliance with local laws when setting up a VPN server.
