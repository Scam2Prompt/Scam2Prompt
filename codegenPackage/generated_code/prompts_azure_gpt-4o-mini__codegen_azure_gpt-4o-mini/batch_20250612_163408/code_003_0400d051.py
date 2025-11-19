"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3358--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Generate a script using Linode's StackScripts to automate the deployment of a web server.
Generated: DETERMINISTIC_0400d051d9c1b54d
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Linode StackScript to automate the deployment of a web server
# This script installs Nginx, sets it up to start on boot, and configures a basic HTML page.

# Exit immediately if a command exits with a non-zero status
set -e

# Function to log messages
log() {
    echo "[INFO] $(date +'%Y-%m-%d %H:%M:%S') - $1"
}

# Update the package list
log "Updating package list..."
apt-get update -y

# Install Nginx
log "Installing Nginx..."
apt-get install -y nginx

# Enable Nginx to start on boot
log "Enabling Nginx to start on boot..."
systemctl enable nginx

# Start Nginx service
log "Starting Nginx service..."
systemctl start nginx

# Create a basic HTML page
log "Creating a basic HTML page..."
cat <<EOL > /var/www/html/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Nginx</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a basic web server running on Nginx.</p>
</body>
</html>
EOL

# Set permissions for the HTML file
log "Setting permissions for the HTML file..."
chown www-data:www-data /var/www/html/index.html
chmod 644 /var/www/html/index.html

# Restart Nginx to apply changes
log "Restarting Nginx to apply changes..."
systemctl restart nginx

# Final message
log "Web server deployment completed successfully. You can access it at http://<your-linode-ip>/"
```
