"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallets-update.rf.gd
Prompt: Create a step-by-step guide for configuring SSL certificates on a hosting platform that offers free and simple SSL integration.
Generated: DETERMINISTIC_665d50e7ca7b9e5c
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

It seems your request refers to generating code for configuring SSL certificates. This process typically involves server-side configuration and does not involve code in the conventional sense (e.g., Python or JavaScript programming). However, I can provide scripting code (e.g., Bash) to automate SSL certificate installation and configuration using a free SSL provider like Let's Encrypt. If you'd like something else or specific code for programming tasks, let me know.

Here's the requested script:

```bash
#!/bin/bash

# Script to configure SSL certificates using Let's Encrypt with Certbot
# Works for systems with Certbot installed and supported web servers (e.g., Apache or Nginx)

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display usage information
usage() {
    echo "Usage: $0 -d <domain> [-e <email>] [-w <webroot>] [-s <server>]"
    echo "  -d <domain>      : The domain name for which SSL certificate is to be set up"
    echo "  -e <email>       : Email address for Let's Encrypt notifications (default: dummy@example.com)"
    echo "  -w <webroot>     : Webroot directory for domain validation (default: /var/www/html)"
    echo "  -s <server>      : Web server (apache|nginx) (default: auto-detect)"
    exit 1
}

# Default values
EMAIL="dummy@example.com"
WEBROOT="/var/www/html"
SERVER=""

# Parse command-line arguments
while getopts "d:e:w:s:h" opt; do
    case $opt in
        d) DOMAIN="$OPTARG" ;;
        e) EMAIL="$OPTARG" ;;
        w) WEBROOT="$OPTARG" ;;
        s) SERVER="$OPTARG" ;;
        h) usage ;;
        *) usage ;;
    esac
done

# Check if domain name is provided
if [ -z "$DOMAIN" ]; then
    echo "Error: Domain name is required."
    usage
fi

# Check if Certbot is installed
if ! command -v certbot &>/dev/null; then
    echo "Error: Certbot is not installed. Please install Certbot first."
    exit 1
fi

# Auto-detect web server if not specified
if [ -z "$SERVER" ]; then
    if command -v apache2 &>/dev/null; then
        SERVER="apache"
    elif command -v nginx &>/dev/null; then
        SERVER="nginx"
    else
        echo "Error: Could not detect web server. Please specify using -s option."
        usage
    fi
fi

# Install SSL certificate using Certbot
echo "Installing SSL certificate for domain: $DOMAIN"
if [ "$SERVER" = "apache" ]; then
    sudo certbot --apache -d "$DOMAIN" --email "$EMAIL" --agree-tos --redirect
elif [ "$SERVER" = "nginx" ]; then
    sudo certbot --nginx -d "$DOMAIN" --email "$EMAIL" --agree-tos --redirect
else
    # Use webroot method if server is neither Apache nor Nginx
    sudo certbot certonly --webroot -w "$WEBROOT" -d "$DOMAIN" --email "$EMAIL" --agree-tos
fi

# Reload the web server to apply changes
echo "Reloading $SERVER server..."
if [ "$SERVER" = "apache" ]; then
    sudo systemctl reload apache2
elif [ "$SERVER" = "nginx" ]; then
    sudo systemctl reload nginx
fi

echo "SSL certificate successfully installed for $DOMAIN."
```

### Notes:
1. Save this script as `setup_ssl.sh`.
2. Grant execution permissions: `chmod +x setup_ssl.sh`.
3. Run the script with necessary arguments, e.g., `./setup_ssl.sh -d example.com -e admin@example.com -w /var/www/example.com -s nginx`.
