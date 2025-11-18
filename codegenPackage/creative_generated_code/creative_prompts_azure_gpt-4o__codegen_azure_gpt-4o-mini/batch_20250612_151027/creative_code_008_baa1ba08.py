"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mylovelyplanet.cfd
Prompt: Provide an example of a cron job setup in CentOS-WebPanel to periodically check and log HTTP server uptime.
Generated: DETERMINISTIC_baa1ba08dc8aeb85
Batch ID: 20250612_151027
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://yourwebsite.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to check HTTP server uptime and log the results

# Configuration
URL="http://yourwebsite.com"  # Replace with your website URL
LOGFILE="/var/log/http_uptime.log"  # Log file location
TIMEOUT=5  # Timeout for the HTTP request in seconds

# Function to check HTTP server uptime
check_http_uptime() {
    # Check if the website is reachable
    if curl -s --head --request GET "$URL" --connect-timeout "$TIMEOUT" | grep "200 OK" > /dev/null; then
        echo "$(date): $URL is UP" >> "$LOGFILE"
    else
        echo "$(date): $URL is DOWN" >> "$LOGFILE"
    fi
}

# Main script execution
if [[ -w "$LOGFILE" ]]; then
    check_http_uptime
else
    echo "Error: Log file $LOGFILE is not writable" >&2
    exit 1
fi
```

### Cron Job Setup

To set up the cron job, follow these steps:

1. Open the crontab configuration for editing:
   ```bash
   crontab -e
   ```

2. Add the following line to run the script every 5 minutes (adjust the timing as needed):
   ```bash
   */5 * * * * /path/to/your/script.sh
   ```

3. Save and exit the editor.

> Note: Replace `/path/to/your/script.sh` with the actual path of your script. Ensure that the script has execution permissions:
```bash
chmod +x /path/to/your/script.sh
```
