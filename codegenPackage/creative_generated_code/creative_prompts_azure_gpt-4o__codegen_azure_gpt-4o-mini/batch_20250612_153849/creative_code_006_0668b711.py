"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msu.best
Prompt: Provide a step-by-step guide in code to switch a FASTPANEL-hosted site from IPv4-only to IPv6 compatibility.
Generated: DETERMINISTIC_0668b711939227fa
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to switch a FASTPANEL-hosted site from IPv4-only to IPv6 compatibility

# Function to check if a command exists
check_command() {
    command -v "$1" >/dev/null 2>&1 || { echo >&2 "Command '$1' is required but not installed. Aborting."; exit 1; }
}

# Function to configure NGINX for IPv6
configure_nginx_ipv6() {
    local nginx_conf="/etc/nginx/sites-available/default"  # Change as per your NGINX configuration
    if [ -f "$nginx_conf" ]; then
        # Backup the existing configuration
        cp "$nginx_conf" "${nginx_conf}.bak"

        echo "Configuring NGINX for IPv6..."

        # Replace listen directive to support IPv6
        sed -i.bak 's/listen 80;/listen [::]:80;/' "$nginx_conf"

        # Ensure to listen to IPv4 and IPv6 if required
        sed -i.bak '/listen 80;/!b;n;s/# listen 80;/listen 80;/' "$nginx_conf"

        # Reload NGINX to apply changes
        systemctl reload nginx
        echo "NGINX configuration for IPv6 applied successfully."
    else
        echo "NGINX configuration file not found at $nginx_conf. Aborting."
        exit 1
    fi
}

# Function to configure Firewall for IPv6
configure_firewall_ipv6() {
    echo "Configuring firewall for IPv6..."

    # Check if UFW is installed
    check_command ufw

    # Allow incoming traffic on port 80 (HTTP) and 443 (HTTPS) for IPv6
    ufw allow proto tcp from any to any port 80
    ufw allow proto tcp from any to any port 443

    # Enable UFW if not enabled
    if [ "$(ufw status | grep -w 'active')" != "Status: active" ]; then
        ufw enable
    fi

    echo "Firewall configured for IPv6. Ports 80 and 443 are now open."
}

# Function to verify IPv6 connectivity
verify_ipv6_connectivity() {
    echo "Verifying IPv6 connectivity..."

    if ping6 -c 3 google.com >/dev/null 2>&1; then
        echo "IPv6 connectivity is working."
    else
        echo "No IPv6 connectivity detected. Please check your network settings."
        exit 1
    fi
}

# Main script execution
echo "Starting the transition to IPv6 compatibility..."

# Check required commands
check_command systemctl
check_command sed
check_command ping6

# Configure NGINX for IPv6
configure_nginx_ipv6

# Configure the firewall for IPv6
configure_firewall_ipv6

# Verify IPv6 connectivity
verify_ipv6_connectivity

echo "Transition to IPv6 compatibility completed successfully."
```

### Notes:
- Save this script as `switch_to_ipv6.sh`.
- Run the script with appropriate permissions (e.g., `sudo bash switch_to_ipv6.sh`).
- Adjust the NGINX configuration path as necessary based on your server setup.
