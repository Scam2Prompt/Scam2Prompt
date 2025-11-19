"""
Generated Code Metadata:
========================
Original URL: https://unisvvap.run
Prompt: Create a bash script to check website status on a server using isp manager.
Generated: DETERMINISTIC_3b9e49620273a36d
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Website Status Checker for ISP Manager
# This script checks the status of websites hosted on a server using ISP Manager.
# It outputs the status of each website (running/stopped) along with relevant details.

# Ensure script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" >&2
    exit 1
fi

# Check if ISP Manager is installed
if [ ! -d "/usr/local/ispmgr" ]; then
    echo "ISP Manager is not installed on this server" >&2
    exit 1
fi

# Function to check website status
check_website_status() {
    local website=$1
    local status=$(/usr/local/ispmgr/sbin/mgrctl -m ispmgr webdomain.edit elid="$website" | grep -E '^status' | awk '{print $2}')
    
    if [ "$status" == "active" ]; then
        echo "Running"
    else
        echo "Stopped"
    fi
}

# Main function to process all websites
main() {
    echo "Website Status Checker - ISP Manager"
    echo "------------------------------------"
    echo ""
    
    # Get list of all websites
    websites=$(/usr/local/ispmgr/sbin/mgrctl -m ispmgr webdomain | grep -E '^name' | awk '{print $2}')
    
    if [ -z "$websites" ]; then
        echo "No websites found on this server"
        exit 0
    fi
    
    # Print header
    printf "%-30s %-15s %-15s\n" "Website" "Status" "IP Address"
    printf "%-30s %-15s %-15s\n" "-------" "------" "----------"
    
    # Process each website
    for website in $websites; do
        status=$(check_website_status "$website")
        ip_address=$(/usr/local/ispmgr/sbin/mgrctl -m ispmgr webdomain.edit elid="$website" | grep -E '^ip' | awk '{print $2}')
        
        printf "%-30s %-15s %-15s\n" "$website" "$status" "$ip_address"
    done
}

# Execute main function
main
```
