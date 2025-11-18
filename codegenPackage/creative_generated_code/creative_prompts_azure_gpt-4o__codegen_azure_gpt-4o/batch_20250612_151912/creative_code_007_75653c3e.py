"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geteasycrypto.com
Prompt: Write a Bash script to automate routine maintenance tasks on a CentOS-WebPanel-powered server, such as clearing logs and restarting services.
Generated: DETERMINISTIC_75653c3e48a63736
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Title: CentOS-WebPanel Maintenance Script
# Description: Automates routine maintenance tasks on a CentOS-WebPanel-powered server.
# Author: [Your Name]
# Version: 1.0
# Date: [Insert Date]

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display usage instructions
function usage() {
    echo "Usage: $0 [OPTIONS]"
    echo "Options:"
    echo "  --help            Show this help message"
    echo "  --clear-logs      Clear system and application logs"
    echo "  --restart-services Restart critical server services"
    echo "  --all             Perform all maintenance tasks"
    exit 0
}

# Function to clear system and application logs
function clear_logs() {
    echo "Clearing logs..."
    # Define log directories
    LOG_DIRS=(
        "/var/log"
        "/usr/local/cwp/logs"
    )

    # Iterate through each directory and clear logs
    for dir in "${LOG_DIRS[@]}"; do
        if [ -d "$dir" ]; then
            echo "Clearing logs in $dir..."
            find "$dir" -type f -name "*.log" -exec truncate -s 0 {} \; || {
                echo "Error: Failed to clear logs in $dir" >&2
                exit 1
            }
        else
            echo "Warning: Directory $dir does not exist." >&2
        fi
    done
    echo "Log clearing completed."
}

# Function to restart critical server services
function restart_services() {
    echo "Restarting critical services..."
    # Define critical services to restart
    SERVICES=(
        "httpd"
        "mysql"
        "cwpsrv"
    )

    # Restart each service and handle errors
    for service in "${SERVICES[@]}"; do
        echo "Restarting $service..."
        systemctl restart "$service" || {
            echo "Error: Failed to restart $service" >&2
            exit 1
        }
        echo "$service restarted successfully."
    done
    echo "Service restart completed."
}

# Main script logic
if [[ $# -eq 0 ]]; then
    usage
fi

case $1 in
    --help)
        usage
        ;;
    --clear-logs)
        clear_logs
        ;;
    --restart-services)
        restart_services
        ;;
    --all)
        clear_logs
        restart_services
        ;;
    *)
        echo "Error: Invalid option '$1'" >&2
        usage
        ;;
esac

echo "Maintenance tasks completed successfully."
exit 0
```
