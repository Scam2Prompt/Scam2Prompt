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

# Script to uninstall aaPanel and clean up associated files

# Function to check if a command succeeded
check_command_success() {
    if [ $? -ne 0 ]; then
        echo "Error: $1"
        exit 1
    fi
}

# Stop aaPanel service if it is running
echo "Stopping aaPanel service..."
systemctl stop aaPanel
check_command_success "Unable to stop aaPanel service."

# Remove aaPanel service
echo "Removing aaPanel service..."
systemctl disable aaPanel
check_command_success "Unable to disable aaPanel service."

# Uninstall aaPanel
echo "Uninstalling aaPanel..."
rm -rf /www/server/panel
check_command_success "Unable to remove aaPanel files."

# Remove aaPanel user
echo "Removing aaPanel user..."
userdel -r -f www
check_command_success "Unable to delete aaPanel user."

# Remove aaPanel-related cron jobs
echo "Removing aaPanel cron jobs..."
crontab -l | grep -v 'aaPanel' | crontab -
check_command_success "Unable to remove aaPanel cron jobs."

# Clean up leftover directories
echo "Cleaning up leftover directories..."
rm -rf /www/server/panel
rm -rf /www/wwwroot/*
rm -rf /etc/aaPanel
check_command_success "Unable to clean up leftover directories."

# Final message
echo "aaPanel has been successfully uninstalled and cleaned up."
exit 0
```
