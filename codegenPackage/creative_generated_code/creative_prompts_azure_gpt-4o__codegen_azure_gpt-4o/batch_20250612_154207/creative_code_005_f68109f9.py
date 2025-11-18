"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0x000000000000000.icu
Prompt: Provide a code example to configure an IPv4-only server to handle domains with AAAA records using FASTPANEL.
Generated: DETERMINISTIC_f68109f92f48f0d4
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script configures FASTPANEL to handle AAAA records on an IPv4-only server.
# It ensures that the server can resolve domains with AAAA records by forcing IPv4 in the DNS resolution process.

set -e  # Exit immediately if a command exits with a non-zero status.
set -u  # Treat unset variables as an error.

# Function to update the DNS resolver configuration
update_resolver_configuration() {
    # Backup the existing resolver configuration file
    local resolver_conf="/etc/resolv.conf"
    local backup_resolver_conf="/etc/resolv.conf.bak"

    echo "Creating a backup of $resolver_conf..."
    cp "$resolver_conf" "$backup_resolver_conf"

    # Force the resolver to use IPv4 by appending options
    echo "Configuring $resolver_conf to prefer IPv4..."
    {
        echo "options inet6-disable"  # Disable IPv6 resolution
        echo "options single-request-reopen"  # Workaround for handling AAAA records
    } >> "$resolver_conf"

    echo "$resolver_conf updated successfully."
}

# Function to restart necessary services
restart_fastpanel_services() {
    echo "Restarting FASTPANEL services to apply changes..."
    # Restart the FASTPANEL service
    if systemctl is-active --quiet fastpanel; then
        systemctl restart fastpanel
        echo "FASTPANEL service restarted successfully."
    else
        echo "FASTPANEL service is not active. Skipping restart."
    fi
}

# Main script execution
main() {
    echo "Starting IPv4-only server configuration for handling AAAA records..."
    
    # Step 1: Update resolver configuration
    update_resolver_configuration

    # Step 2: Restart services
    restart_fastpanel_services

    echo "Configuration completed successfully."
}

# Call the main function
main
```
