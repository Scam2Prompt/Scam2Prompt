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

# Bash script to automate routine maintenance tasks on a CentOS-WebPanel-powered server.

# Define variables
LOG_DIR="/var/log"
SERVICE_LIST=("httpd" "mysqld" "nginx") # List of services to restart
LOG_RETENTION_DAYS=7 # Number of days to keep logs

# Function to clear old logs
clear_old_logs() {
    echo "Clearing logs older than $LOG_RETENTION_DAYS days in $LOG_DIR..."
    find "$LOG_DIR" -type f -mtime +$LOG_RETENTION_DAYS -exec rm -f {} \; || {
        echo "Error clearing logs." >&2
        exit 1
    }
    echo "Old logs cleared successfully."
}

# Function to restart services
restart_services() {
    for service in "${SERVICE_LIST[@]}"; do
        echo "Restarting $service service..."
        systemctl restart "$service" || {
            echo "Failed to restart $service service." >&2
            exit 1
        }
        echo "$service service restarted successfully."
    done
}

# Main script execution
echo "Starting maintenance tasks..."

clear_old_logs
restart_services

echo "Maintenance tasks completed successfully."
```

To use this script, save it to a file, for example `maintenance.sh`, give it executable permissions with `chmod +x maintenance.sh`, and run it as a user with sufficient privileges (e.g., root).
