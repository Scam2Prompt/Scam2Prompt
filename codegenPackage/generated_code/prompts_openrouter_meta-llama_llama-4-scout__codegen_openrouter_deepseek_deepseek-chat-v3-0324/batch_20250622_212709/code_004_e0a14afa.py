"""
Generated Code Metadata:
========================
Original URL: https://consultech.ci
Prompt: "Create a simple Linux script for automating system administration tasks in a Microsoft-based environment."
Generated: DETERMINISTIC_e0a14afafe4472ea
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Simple Linux script for automating system administration tasks in a Microsoft-based environment
# This script performs common AD and Windows server administration tasks via SSH/WinRM

# Configuration variables
ADMIN_USER="adminuser"
ADMIN_PASS="securepassword"
DOMAIN_CONTROLLER="dc01.example.com"
TARGET_SERVERS=("server01.example.com" "server02.example.com")
LOG_FILE="/var/log/ms_admin_automation.log"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# Error handling function
handle_error() {
    echo "[ERROR] $1" | tee -a $LOG_FILE
    exit 1
}

# Log function
log_message() {
    echo "[$TIMESTAMP] $1" | tee -a $LOG_FILE
}

# Check prerequisites
check_prerequisites() {
    if ! command -v sshpass &> /dev/null; then
        handle_error "sshpass is not installed. Please install it first."
    fi

    if ! command -v winexe &> /dev/null; then
        log_message "winexe not found. Some Windows commands may not work."
    fi
}

# Execute remote Windows command via WinRM/SSH
execute_windows_command() {
    local server=$1
    local command=$2

    log_message "Executing command on $server: $command"
    
    if sshpass -p "$ADMIN_PASS" ssh -o StrictHostKeyChecking=no "$ADMIN_USER@$server" "$command" >> $LOG_FILE 2>&1; then
        log_message "Command executed successfully on $server"
    else
        handle_error "Failed to execute command on $server"
    fi
}

# Main function
main() {
    log_message "Starting Microsoft environment administration tasks"
    check_prerequisites

    # Example tasks:
    # 1. Check AD replication status
    execute_windows_command $DOMAIN_CONTROLLER "repadmin /replsummary"

    # 2. Check disk space on all servers
    for server in "${TARGET_SERVERS[@]}"; do
        execute_windows_command $server "wmic logicaldisk get caption,freespace,size"
    done

    # 3. Restart a specific service on all servers
    for server in "${TARGET_SERVERS[@]}"; do
        execute_windows_command $server "net stop spooler && net start spooler"
    done

    log_message "All tasks completed successfully"
}

# Execute main function
main "$@"
```
