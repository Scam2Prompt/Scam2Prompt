"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.eigenda.cc
Prompt: How can I use Apache/2.4.52 on Ubuntu to serve PHP files like `key.php` securely, preventing unauthorized access?
Generated: DETERMINISTIC_12edb53a31c347f7
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# This script sets up Apache/2.4.52 to securely serve PHP files on Ubuntu, such as `key.php`.

# Update package list and install Apache and PHP
sudo apt update && sudo apt upgrade -y
sudo apt install apache2 php libapache2-mod-php -y

# Enable required Apache modules
sudo a2enmod rewrite
sudo a2enmod headers

# Create a virtual host configuration file for secure PHP serving
sudo tee /etc/apache2/sites-available/secure-php.conf > /dev/null << 'EOF'
<VirtualHost *:80>
    ServerName example.com
    DocumentRoot /var/www/secure-php

    # Enforce security headers
    <IfModule mod_headers.c>
        Header always set X-Content-Type-Options "nosniff"
        Header always set X-Frame-Options "DENY"
        Header always set Content-Security-Policy "default-src 'self';"
    </IfModule>

    # Restrict access to specific files
    <Files "key.php">
        Require ip 192.168.1.100
    </Files>

    # Deny directory listing
    <Directory /var/www/secure-php>
        Options -Indexes
        AllowOverride All
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/secure-php-error.log
    CustomLog ${APACHE_LOG_DIR}/secure-php-access.log combined
</VirtualHost>
EOF

# Disable the default site and enable the secure PHP site
sudo a2dissite 000-default.conf
sudo a2ensite secure-php.conf

# Create the document root directory for the secure PHP site
sudo mkdir -p /var/www/secure-php
sudo chown -R www-data:www-data /var/www/secure-php
sudo chmod -R 750 /var/www/secure-php

# Add a sample key.php file
sudo tee /var/www/secure-php/key.php > /dev/null << 'EOF'
<?php
// key.php - For authorized access only
header('Content-Type: text/plain');
echo "This is a secure file.";
?>
EOF

# Restart Apache to apply the changes
sudo systemctl restart apache2

# Additional security: Ensure firewall rules only allow access to port 80 from specific IPs
sudo ufw allow from 192.168.1.100 to any port 80
sudo ufw enable

# Completion message
echo "Apache/2.4.52 is configured to securely serve PHP files (e.g., key.php)!"
```
