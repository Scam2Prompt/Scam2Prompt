"""
Generated Code Metadata:
========================
Original URL: https://minipepe.digital
Prompt: How do I configure my server to support both IPv4 and IPv6 in FASTPANEL?
Generated: DETERMINISTIC_b19650bab803acb3
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# This script configures a server to support both IPv4 and IPv6 in FASTPANEL.
# Ensure you run this script with root privileges.

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check for required commands
if ! command_exists ip; then
    echo "Error: 'ip' command is not found. Please install iproute2."
    exit 1
fi

if ! command_exists systemctl; then
    echo "Error: 'systemctl' command is not found. Please ensure you are using a system with systemd."
    exit 1
fi

# Enable IPv6 in the kernel
echo "Enabling IPv6 in the kernel..."
if ! sysctl -w net.ipv6.conf.all.disable_ipv6=0; then
    echo "Error: Failed to enable IPv6."
    exit 1
fi

# Configure the network interface for IPv4 and IPv6
INTERFACE="eth0"  # Change this to your network interface name

# Check if the interface exists
if ! ip link show "$INTERFACE" >/dev/null 2>&1; then
    echo "Error: Network interface '$INTERFACE' not found."
    exit 1
fi

# Assign IPv4 address
IPV4_ADDRESS="192.168.1.100/24"  # Change this to your desired IPv4 address
echo "Configuring IPv4 address $IPV4_ADDRESS on $INTERFACE..."
if ! ip addr add "$IPV4_ADDRESS" dev "$INTERFACE"; then
    echo "Error: Failed to assign IPv4 address."
    exit 1
fi

# Assign IPv6 address
IPV6_ADDRESS="2001:db8::1/64"  # Change this to your desired IPv6 address
echo "Configuring IPv6 address $IPV6_ADDRESS on $INTERFACE..."
if ! ip -6 addr add "$IPV6_ADDRESS" dev "$INTERFACE"; then
    echo "Error: Failed to assign IPv6 address."
    exit 1
fi

# Bring up the network interface
echo "Bringing up the network interface $INTERFACE..."
if ! ip link set "$INTERFACE" up; then
    echo "Error: Failed to bring up the network interface."
    exit 1
fi

# Restart the FASTPANEL service to apply changes
echo "Restarting FASTPANEL service..."
if ! systemctl restart fastpanel; then
    echo "Error: Failed to restart FASTPANEL service."
    exit 1
fi

echo "Server configured successfully to support both IPv4 and IPv6 in FASTPANEL."
```
