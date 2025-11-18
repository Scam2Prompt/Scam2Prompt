"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chillguy.lol
Prompt: Provide recommendations for configuring a server to support both IPv4 and IPv6, referencing FASTPANEL's domain setup guidelines.
Generated: DETERMINISTIC_400525ea6aeb04c1
Batch ID: 20250612_145506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script configures a server to support both IPv4 and IPv6.
# It includes basic firewall rules and network configuration adjustments.
# Ensure you run this script with root privileges.

# Function to check if a command succeeded
check_command() {
    if [ $? -ne 0 ]; then
        echo "Error: $1 failed."
        exit 1
    fi
}

# Update package list
echo "Updating package list..."
apt update
check_command "Package list update"

# Install necessary packages (if not already installed)
echo "Installing necessary packages..."
apt install -y net-tools iptables-persistent
check_command "Package installation"

# Configure the network interfaces
echo "Configuring network interfaces..."
cat <<EOL > /etc/network/interfaces
# /etc/network/interfaces

# Loopback interface
auto lo
iface lo inet loopback

# IPv4 configuration
auto eth0
iface eth0 inet dhcp

# IPv6 configuration
iface eth0 inet6 auto
EOL

# Restart networking service to apply changes
echo "Restarting networking service..."
systemctl restart networking
check_command "Restart networking service"

# Configure firewall for IPv4 and IPv6 support
echo "Configuring firewall..."

# Allow essential services
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT # SSH
iptables -A INPUT -p tcp --dport 80 -j ACCEPT # HTTP
iptables -A INPUT -p tcp --dport 443 -j ACCEPT # HTTPS
iptables -A INPUT -j DROP # Drop all other traffic

# Save IPv4 rules
iptables-save > /etc/iptables/rules.v4

# IPv6 configuration
ip6tables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
ip6tables -A INPUT -p tcp --dport 22 -j ACCEPT # SSH
ip6tables -A INPUT -p tcp --dport 80 -j ACCEPT # HTTP
ip6tables -A INPUT -p tcp --dport 443 -j ACCEPT # HTTPS
ip6tables -A INPUT -j DROP # Drop all other traffic

# Save IPv6 rules
ip6tables-save > /etc/iptables/rules.v6

# Notify the user of successful configuration
echo "Server successfully configured to support both IPv4 and IPv6."
echo "Please review the configuration in /etc/network/interfaces and the firewall rules."
```

### Note:
- This script is designed for Debian-based systems (like Ubuntu). Adjust package installation and commands according to the specific distribution if necessary.
- Ensure your server's firewall settings do not block other necessary ports according to your application needs.
