"""
Generated Code Metadata:
========================
Original URL: https://mylovelyplanet.cfd
Prompt: Provide an example of a cron job setup in CentOS-WebPanel to periodically check and log HTTP server uptime.
Generated: DETERMINISTIC_baa1ba08dc8aeb85
Batch ID: 20250612_151027
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your-server-url.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to check HTTP server uptime and log the result

# Configuration
URL="http://your-server-url.com"  # Replace with your server URL
LOG_FILE="/var/log/http_uptime.log"  # Log file path
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")  # Current timestamp

# Function to check HTTP server status
check_http_status() {
    # Send a request to the server and capture the HTTP response code
    HTTP_RESPONSE=$(curl -o /dev/null -s -w "%{http_code}\n" "$URL")

    # Check if the response code is 200 (OK)
    if [ "$HTTP_RESPONSE" -eq 200 ]; then
        echo "$TIMESTAMP - Server is UP" >> "$LOG_FILE"
    else
        echo "$TIMESTAMP - Server is DOWN (HTTP Code: $HTTP_RESPONSE)" >> "$LOG_FILE"
    fi
}

# Error handling
{
    check_http_status
} || {
    echo "$TIMESTAMP - Error occurred while checking server status" >> "$LOG_FILE"
}

# End of script
```

### Cron Job Setup
To set up a cron job to run this script periodically, follow these steps:

1. Save the script above to a file, e.g., `/usr/local/bin/check_http_uptime.sh`.
2. Make the script executable:
   ```bash
   chmod +x /usr/local/bin/check_http_uptime.sh
   ```
3. Open the crontab for editing:
   ```bash
   crontab -e
   ```
4. Add a line to schedule the script (e.g., every 5 minutes):
   ```bash
   */5 * * * * /usr/local/bin/check_http_uptime.sh
   ```
5. Save and exit the crontab editor.

This setup will log the HTTP server uptime status every 5 minutes to the specified log file.
