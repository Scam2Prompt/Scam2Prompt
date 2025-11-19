"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptogive.rf.gd
Prompt: What are the steps to enable a free SSL certificate for a website hosted on iFastNet?
Generated: DETERMINISTIC_0f6a2c5942242631
Batch ID: 20250612_162409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to enable a free SSL certificate for a website hosted on iFastNet using Certbot
# Ensure Certbot is installed before running this script

# Usage: ./enable_ssl.sh yourdomain.com

# Function to display usage information
usage() {
    echo "Usage: $0 domain"
    exit 1
}

# Check if the domain is provided as an argument
if [ $# -ne 1 ]; then
    usage
fi

DOMAIN=$1

# Check for Certbot installation
if ! command -v certbot &> /dev/null; then
    echo "Certbot could not be found. Please install Certbot first."
    exit 1
fi

# Requesting SSL certificate
echo "Requesting SSL certificate for $DOMAIN..."

# Run Certbot to obtain the SSL certificate
if certbot certonly --webroot -w /path/to/your/webroot -d "$DOMAIN"; then
    echo "SSL certificate successfully obtained for $DOMAIN."
else
    echo "Error: Failed to obtain SSL certificate for $DOMAIN."
    exit 1
fi

# Reload web server to apply the new SSL certificate
echo "Reloading web server to apply the new SSL certificate..."

# Command to reload the web server (nginx example)
if sudo systemctl reload nginx; then
    echo "Web server reloaded successfully."
else
    echo "Error: Failed to reload web server."
    exit 1
fi

echo "SSL setup complete for $DOMAIN."
```

**Note**: Make sure to replace `/path/to/your/webroot` with the actual path to your webroot directory where your website files are hosted. Additionally, ensure that you run this script with the proper permissions to execute Certbot and reload the web server.
