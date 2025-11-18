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

```bash
#!/bin/bash

# Step 1: Update the system packages
echo "Updating system packages..."
sudo apt-get update && sudo apt-get upgrade -y

# Step 2: Install necessary packages for VPN setup
echo "Installing necessary packages..."
sudo apt-get install -y openvpn easy-rsa iptables-persistent

# Step 3: Set up the Public Key Infrastructure (PKI)
echo "Setting up the Public Key Infrastructure (PKI)..."
make-cadir ~/openvpn-ca
cd ~/openvpn-ca

# Step 4: Configure the OpenVPN server
echo "Configuring OpenVPN server..."
source vars
./clean-all
./build-ca
./build-key-server server
./build-dh
openvpn --genkey --secret keys/ta.key

# Step 5: Generate server configuration file
echo "Generating server configuration file..."
cat <<EOL > ~/openvpn-ca/keys/server.conf
port 1194
proto udp
dev tun
ca ca.crt
cert server.crt
key server.key
dh dh2048.pem
tls-auth ta.key 0
cipher AES-256-CBC
comp-lzo
persist-key
persist-tun
status openvpn-status.log
verb 3
keepalive 10 120
user nobody
group nogroup
EOL

# Step 6: Set up IP forwarding
echo "Enabling IP forwarding..."
echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

# Step 7: Configure UFW (Uncomplicated Firewall)
echo "Configuring UFW to allow OpenVPN traffic..."
sudo ufw allow 1194/udp
sudo ufw allow OpenSSH
echo "y" | sudo ufw enable

# Step 8: Add NAT rules to iptables
echo "Adding NAT rules to iptables..."
sudo iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -s 10.8.0.0/24 -j ACCEPT

# Step 9: Save iptables rules
echo "Saving iptables rules..."
sudo iptables-save | sudo tee /etc/iptables/rules.v4

# Step 10: Start the OpenVPN server
echo "Starting OpenVPN server..."
sudo systemctl start openvpn@server
sudo systemctl enable openvpn@server

# Step 11: Verify OpenVPN service status
echo "Verifying OpenVPN service status..."
sudo systemctl status openvpn@server

# Step 12: Configuration for P2P support
echo "Configuring P2P support..."
# Assuming peers will connect to the server using the "client.conf"
cat <<EOL > ~/client.ovpn
client
dev tun
proto udp
remote YOUR_SERVER_IP 1194
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
auth SHA256
cipher AES-256-CBC
tls-auth ta.key 1
comp-lzo
verb 3
EOL

# Step 13: Completion message
echo "VPN server setup is complete. Make sure to replace 'YOUR_SERVER_IP' in client.ovpn with your server's public IP."
``` 

**Note:** 
- Replace `YOUR_SERVER_IP` in the `client.ovpn` file with the actual public IP address of your server.
- Make sure to run this script with appropriate privileges, and perform actions in a secure environment.
- This script presumes a basic familiarity with Linux command-line operations. Please adapt paths and configurations based on your specific requirements and environment.
