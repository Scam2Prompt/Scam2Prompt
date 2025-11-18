"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobgridl.top
Prompt: Generate a bash script to uninstall aaPanel and clean up associated files from a server.
Generated: DETERMINISTIC_b6982b458ed62695
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# aaPanel Uninstallation Script
# This script removes aaPanel and cleans up associated files from the server.

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display usage information
function usage() {
    echo "Usage: $0"
    echo "This script uninstalls aaPanel and cleans up associated files from your server."
    exit 1
}

# Function to uninstall aaPanel
function uninstall_aapanel() {
    echo "Starting aaPanel uninstallation..."

    # Stop and remove aaPanel services
    echo "Stopping aaPanel services..."
    if command -v systemctl &> /dev/null; then
        systemctl stop bt
        systemctl disable bt
    elif command -v service &> /dev/null; then
        service bt stop || true
    else
        echo "Error: Unable to stop aaPanel services. No service manager found."
    fi

    # Remove aaPanel directories
    echo "Removing aaPanel application files..."
    rm -rf /www/server
    rm -rf /www/logs
    rm -rf /www/backup

    # Clean up residual files
    echo "Cleaning up residual files..."
    rm -f /usr/bin/bt
    rm -f /etc/init.d/bt

    echo "aaPanel uninstallation completed."
}

# Function to confirm uninstallation
function confirm_uninstallation() {
    echo "WARNING: This will uninstall aaPanel and delete all its associated files."
    read -p "Are you sure you want to proceed? (yes/no): " confirmation
    if [[ "$confirmation" != "yes" ]]; then
        echo "Uninstallation aborted."
        exit 0
    fi
}

# Main script execution
function main() {
    if [[ $EUID -ne 0 ]]; then
        echo "Error: This script must be run as root."
        exit 1
    fi

    confirm_uninstallation
    uninstall_aapanel

    echo "Cleanup complete. Please reboot the server if necessary."
}

# Execute the main function
main
```
