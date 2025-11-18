"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-ebh.net
Prompt: Create a script to configure IRC chat on CentOS for community support and collaboration.
Generated: DETERMINISTIC_c97b3a2049697a22
Batch ID: 20250612_145427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to configure an IRC server on CentOS for community support and collaboration.
# This script is intended for production use and follows CentOS best practices.

# Exit immediately if a command exits with a non-zero status.
set -e

# Define constants
IRC_SERVER_PACKAGE="inspircd"
FIREWALL_RULE="6667"  # Default port for IRC

# Function to check for root privileges
check_root() {
    if [[ $EUID -ne 0 ]]; then
        echo "This script must be run as root. Please re-run with sudo or as root."
        exit 1
    fi
}

# Function to update the system and install necessary packages
install_irc_server() {
    echo "Updating system packages..."
    yum update -y

    echo "Installing IRC server package: $IRC_SERVER_PACKAGE..."
    yum install -y $IRC_SERVER_PACKAGE
}

# Function to configure the IRC server
configure_irc_server() {
    CONFIG_PATH="/etc/inspircd/inspircd.conf"

    echo "Configuring IRC server..."
    if [[ ! -f $CONFIG_PATH ]]; then
        echo "Configuration file not found: $CONFIG_PATH"
        exit 1
    fi

    # Backup the original configuration file
    cp $CONFIG_PATH "$CONFIG_PATH.bak"

    # Modify server name, administrator email, and ports in the configuration
    sed -i 's/<server name=".*"/<server name="irc.communitychat.local"/' $CONFIG_PATH
    sed -i 's/<admin email=".*"/<admin email="admin@communitychat.local"/' $CONFIG_PATH
    sed -i 's/<bind address=".*" port=".*"/<bind address="0.0.0.0" port="'$FIREWALL_RULE'"/' $CONFIG_PATH

    echo "IRC server configured successfully."
}

# Function to enable and start the IRC server service
enable_start_service() {
    echo "Enabling and starting the IRC server service..."
    systemctl enable inspircd
    systemctl start inspircd
    
    echo "Checking IRC server status..."
    systemctl status inspircd
}

# Function to configure the firewall for IRC
configure_firewall() {
    echo "Configuring firewall to allow IRC traffic on port $FIREWALL_RULE..."
    firewall-cmd --permanent --add-port=$FIREWALL_RULE/tcp
    firewall-cmd --reload

    echo "Firewall configured successfully."
}

# Main function to orchestrate the setup
main() {
    echo "Starting IRC server setup on CentOS..."
    check_root
    install_irc_server
    configure_irc_server
    configure_firewall
    enable_start_service

    echo "IRC server setup complete. Your server is now ready for community support and collaboration."
}

# Run the main function
main
```
