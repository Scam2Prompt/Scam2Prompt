"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://destiro.com
Prompt: Provide a step-by-step guide for setting up an Apache/2.4.62 server on Debian and configuring it to serve static files securely.
Generated: DETERMINISTIC_164fba2cc2f75cec
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Step-by-step guide for setting up Apache/2.4.62 on Debian and configuring it to serve static files securely.
# Designed to be a production-ready script.
# Test and modify as needed for your specific use case.

set -e  # Exit immediately if a command exits with a non-zero status.

# Step 1: Update the system's package index
echo "Updating package index..."
sudo apt update

# Step 2: Install Apache
echo "Installing Apache/2.4.62..."
sudo apt install -y apache2

# Step 3: Verify Apache is installed and running
echo "Verifying Apache installation..."
sudo systemctl status apache2

# Step 4: Enable Apache to start on boot
echo "Enabling Apache to start on boot..."
sudo systemctl enable apache2

# Step 5: Configure the firewall (if UFW is enabled)
echo "Configuring the firewall to allow HTTP and HTTPS traffic..."
sudo ufw allow 'Apache Full'
sudo ufw reload  # Apply the new rules

# Step 6: Secure the server with HTTPS using Let's Encrypt SSL certificates
echo "Installing Certbot for SSL setup..."
sudo apt install -y certbot python3-certbot-apache

echo "Obtaining and installing SSL certificates using Certbot..."
sudo certbot --apache -n --agree-tos --redirect -d yourdomain.com -d www.yourdomain.com

# Note: Replace 'yourdomain.com' with your actual domain.

# Step 7: Create a directory for static files
echo "Creating directory for static files..."
STATIC_DIR="/var/www/static"
sudo mkdir -p "$STATIC_DIR"
sudo chown -R www-data:www-data "$STATIC_DIR"
sudo chmod -R 755 "$STATIC_DIR"

# Step 8: Configure Apache to serve static files securely
echo "Creating Apache configuration for serving static files..."
STATIC_CONF="/etc/apache2/sites-available/static.conf"
sudo cat <<EOF | sudo tee "$STATIC_CONF"
<VirtualHost *:80>
    ServerName yourdomain.com
    ServerAlias www.yourdomain.com

    DocumentRoot $STATIC_DIR

    <Directory $STATIC_DIR>
        Options -Indexes +FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>

    ErrorLog \${APACHE_LOG_DIR}/static_error.log
    CustomLog \${APACHE_LOG_DIR}/static_access.log combined
</VirtualHost>
EOF

# Note: Update 'yourdomain.com' and 'www.yourdomain.com' with your actual domain.

# Step 9: Enable the new configuration and restart Apache
echo "Enabling the static site configuration..."
sudo a2ensite static.conf

echo "Restarting Apache to apply changes..."
sudo systemctl restart apache2

# Step 10: Verify the setup
echo "Setup complete! Test your domain in a browser to ensure the static files are served securely."

# Cleanup: Output a message indicating the script ran successfully.
echo "Apache server setup and static file configuration complete!"
```

This script sets up Apache/2.4.62 on Debian, configures it to serve static files securely using HTTPS, and applies best practices for production environments.
