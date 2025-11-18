"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://workgridp.top
Prompt: Suggest methods to secure an aaPanel installation against unauthorized access, including firewall rules and SSH configurations.
Generated: DETERMINISTIC_f8807ea3f3bfa22d
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script configures security settings for aaPanel to secure against unauthorized access.

# Function to install and configure UFW (Uncomplicated Firewall)
configure_firewall() {
    echo "Configuring firewall rules..."
    
    # Allow SSH connections on port 22
    sudo ufw allow 22/tcp
    
    # Allow aaPanel's default port (e.g., 8888)
    sudo ufw allow 8888/tcp
    
    # Deny all other incoming connections
    sudo ufw default deny incoming
    
    # Allow outgoing connections (default)
    sudo ufw default allow outgoing
    
    # Enable the firewall
    sudo ufw enable
    
    echo "Firewall configured successfully."
}

# Function to secure SSH configuration
secure_ssh() {
    echo "Securing SSH configuration..."
    
    # Backup the original sshd_config file
    sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
    
    # Disable root login via SSH
    sudo sed -i 's/^PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
    
    # Change the default SSH port to enhance security (e.g., to 2222)
    sudo sed -i 's/^#Port 22/Port 2222/' /etc/ssh/sshd_config
    
    # Restart SSH service to apply changes
    sudo systemctl restart sshd
    
    echo "SSH configuration secured successfully."
}

# Function to set up fail2ban to protect against brute force attacks
configure_fail2ban() {
    echo "Installing and configuring fail2ban..."
    
    # Install fail2ban if not already installed
    if ! command -v fail2ban-client &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y fail2ban
    fi
    
    # Create a configuration file for jail.local
    sudo bash -c 'cat << EOF > /etc/fail2ban/jail.local
[sshd]
enabled = true
port = 2222
filter = sshd
logpath = /var/log/auth.log
maxretry = 5
bantime = 3600
EOF'
    
    # Start and enable fail2ban service
    sudo systemctl start fail2ban
    sudo systemctl enable fail2ban
    
    echo "fail2ban configured successfully."
}

# Function to secure aaPanel
secure_aapanel() {
    echo "Securing aaPanel..."
    
    # Example of restricting access to aaPanel based on IP (replace with your IP)
    echo "Allowing access to aaPanel only from specific IP..."
    ALLOWED_IP="YOUR_IP_ADDRESS_HERE"  # Replace with your actual IP
    sudo iptables -A INPUT -p tcp -s $ALLOWED_IP --dport 8888 -j ACCEPT
    sudo iptables -A INPUT -p tcp --dport 8888 -j DROP
    
    echo "aaPanel secured successfully."
}

# Execute the functions
configure_firewall
secure_ssh
configure_fail2ban
secure_aapanel

echo "Security configuration completed successfully."
``` 

**Note:** Make sure to replace `YOUR_IP_ADDRESS_HERE` with the actual IP address from which you want to allow access to aaPanel. Additionally, test this script in a safe environment before executing it on a production server.
