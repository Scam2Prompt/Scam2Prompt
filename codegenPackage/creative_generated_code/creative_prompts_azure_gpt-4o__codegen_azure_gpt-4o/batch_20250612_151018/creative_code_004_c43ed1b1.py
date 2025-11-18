"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3338--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Create a StackScript to deploy a web server on a Linode Standard instance, including installation of Nginx and SSL configuration.
Generated: DETERMINISTIC_c43ed1b15b99eb0c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# StackScript Metadata
# <UDF name="domain_name" label="Domain Name" example="example.com" />
# <UDF name="email" label="Email for SSL Certificate" example="user@example.com" />

DOMAIN_NAME={{domain_name}}
EMAIL={{email}}

set -e

# Helper function to display messages
log() {
    echo "[$(date +"%Y-%m-%d %H:%M:%S")] $@"
}

# Update system packages
log "Updating system packages..."
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Nginx
log "Installing Nginx..."
sudo apt-get install -y nginx

# Start and enable Nginx service
log "Starting and enabling Nginx..."
sudo systemctl start nginx
sudo systemctl enable nginx

# Install Certbot for Let's Encrypt SSL
log "Installing Certbot..."
sudo apt-get install -y certbot python3-certbot-nginx

# Configure firewall (allow HTTP/HTTPS traffic)
log "Configuring firewall..."
sudo ufw allow 'Nginx Full'
sudo ufw --force enable

# SSL Certificate setup with Certbot
log "Setting up SSL with Certbot for domain: $DOMAIN_NAME..."
sudo certbot --nginx -d $DOMAIN_NAME --email $EMAIL --agree-tos --non-interactive

# Schedule automatic SSL certificate renewal
log "Setting up automatic SSL certificate renewal..."
sudo systemctl enable certbot.timer

# Verify Nginx is running
log "Verifying Nginx is running..."
if sudo systemctl is-active --quiet nginx; then
    log "Nginx is running successfully!"
else
    log "Error: Nginx failed to start."
    exit 1
fi

# Final message
log "Web server setup completed successfully! Nginx is running with SSL configured for $DOMAIN_NAME."
```
