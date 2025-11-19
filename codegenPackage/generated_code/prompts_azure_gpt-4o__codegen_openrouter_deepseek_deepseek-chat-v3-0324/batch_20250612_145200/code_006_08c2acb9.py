"""
Generated Code Metadata:
========================
Original URL: https://idn-hosting.com
Prompt: Write a bash script to monitor bandwidth usage on an IDN Hosting VPS server with 1TB bandwidth allocation.
Generated: DETERMINISTIC_08c2acb9094b9379
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Bandwidth Monitoring Script for IDN Hosting VPS
# Monitors bandwidth usage against a 1TB allocation and alerts if threshold is reached.

# Configuration
THRESHOLD_PERCENT=90  # Alert when 90% of bandwidth is used
BANDWIDTH_LIMIT_GB=1000  # 1TB in GB
LOG_FILE="/var/log/bandwidth_monitor.log"
ALERT_EMAIL="admin@example.com"

# Ensure the log directory exists
mkdir -p "$(dirname "$LOG_FILE")"

# Function to log messages with timestamp
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Function to send alert email
send_alert() {
    local subject="Bandwidth Alert: $1% of allocation used"
    local message="Warning: Bandwidth usage has reached $1% of the 1TB allocation on $(hostname)."
    echo "$message" | mail -s "$subject" "$ALERT_EMAIL"
    log "Alert sent: $message"
}

# Main monitoring function
monitor_bandwidth() {
    # Get total bandwidth usage (in bytes) from vnstat
    if ! command -v vnstat &> /dev/null; then
        log "Error: vnstat is not installed. Please install it first."
        exit 1
    fi

    # Get total received and transmitted data in bytes
    rx_bytes=$(vnstat --json | jq -r '.interfaces[0].traffic.total.rx')
    tx_bytes=$(vnstat --json | jq -r '.interfaces[0].traffic.total.tx')
    
    if [ -z "$rx_bytes" ] || [ -z "$tx_bytes" ]; then
        log "Error: Could not retrieve bandwidth data from vnstat."
        exit 1
    fi

    # Calculate total bandwidth used in GB
    total_bytes=$((rx_bytes + tx_bytes))
    total_gb=$(echo "scale=2; $total_bytes / 1024 / 1024 / 1024" | bc)

    # Calculate percentage used
    percent_used=$(echo "scale=2; ($total_gb / $BANDWIDTH_LIMIT_GB) * 100" | bc)

    log "Bandwidth used: ${total_gb}GB (${percent_used}% of ${BANDWIDTH_LIMIT_GB}GB)"

    # Check if threshold is reached
    if (( $(echo "$percent_used >= $THRESHOLD_PERCENT" | bc -l) )); then
        send_alert "$percent_used"
    fi
}

# Main execution
log "Starting bandwidth monitoring..."
monitor_bandwidth
log "Monitoring completed."
```
