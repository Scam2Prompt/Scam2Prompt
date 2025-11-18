"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://8lements.xyz
Prompt: Explain how to secure a LiteSpeed Web Server serving directory listings, including SSL/TLS configuration for port 443.
Generated: DETERMINISTIC_8e38f56638b28eb1
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script configures a LiteSpeed Web Server to secure directory listings
# and sets up SSL/TLS for secure communication over port 443.

# Define variables
LSWS_HOME="/usr/local/lsws"  # Path to LiteSpeed installation
VHOST_CONFIG="$LSWS_HOME/conf/vhosts/your_vhost.conf"  # Path to your virtual host configuration
SSL_CERT="/etc/ssl/certs/your_domain.crt"  # Path to your SSL certificate
SSL_KEY="/etc/ssl/private/your_domain.key"  # Path to your SSL private key

# Function to configure SSL/TLS
configure_ssl() {
    echo "Configuring SSL/TLS for LiteSpeed Web Server..."

    # Check if SSL certificate and key exist
    if [[ ! -f "$SSL_CERT" || ! -f "$SSL_KEY" ]]; then
        echo "Error: SSL certificate or key not found!"
        exit 1
    fi

    # Write SSL configuration to the virtual host config
    cat <<EOL >> "$VHOST_CONFIG"
# SSL Configuration for LiteSpeed
listener SSLListener {
    address                *:443
    secure                 1
    sslProtocol            ALL -SSLv2 -SSLv3
    certFile              $SSL_CERT
    keyFile               $SSL_KEY
}

# Ensure directory listing is enabled
dirListing {
    enable                1
}
EOL

    echo "SSL/TLS configuration complete."
}

# Function to restart LiteSpeed server
restart_litespeed() {
    echo "Restarting LiteSpeed Web Server..."
    # Restart command may vary based on installation
    $LSWS_HOME/bin/lswsctrl restart
    if [ $? -ne 0 ]; then
        echo "Error: Failed to restart LiteSpeed Web Server!"
        exit 1
    fi
    echo "LiteSpeed Web Server restarted successfully."
}

# Main script execution
configure_ssl
restart_litespeed

echo "LiteSpeed Web Server is now secured with SSL/TLS and serving directory listings."
```

### Usage Notes:
- Replace `your_vhost.conf`, `your_domain.crt`, and `your_domain.key` with the appropriate values for your setup.
- Ensure that the script has execute permissions: `chmod +x your_script.sh`.
- Run the script as a user with sufficient privileges to modify the LiteSpeed configuration and restart the server.
