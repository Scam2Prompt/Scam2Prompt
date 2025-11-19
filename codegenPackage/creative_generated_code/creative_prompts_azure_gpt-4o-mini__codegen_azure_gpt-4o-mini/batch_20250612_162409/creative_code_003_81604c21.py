"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.magpiexyz.click
Prompt: What steps should I take to deploy a website correctly to prevent the default web server page from appearing?
Generated: DETERMINISTIC_81604c215a499446
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

# This script deploys a website to prevent the default web server page from appearing.
# It assumes that the web server is either Apache or Nginx and that the website files
# are located in a specified directory.

# Configuration variables
WEBSITE_DIR="/var/www/mywebsite"   # Path to your website files
SERVER_TYPE="nginx"                 # Change to "apache" if using Apache
SERVER_CONFIG="/etc/nginx/sites-available/mywebsite" # Update for Apache as needed

# Function to check if the web server is running
check_server() {
    if ! systemctl is-active --quiet $1; then
        echo "Error: $1 is not running. Starting $1..."
        sudo systemctl start $1
    else
        echo "$1 is running."
    fi
}

# Function to deploy website files
deploy_website() {
    # Check if the website directory exists
    if [ ! -d "$WEBSITE_DIR" ]; then
        echo "Error: Website directory $WEBSITE_DIR does not exist."
        exit 1
    fi

    # Copy website files to the default web directory
    sudo cp -r "$WEBSITE_DIR/" /var/www/html/

    # Set permissions for the web server to access the files
    sudo chown -R www-data:www-data /var/www/html/*
    sudo chmod -R 755 /var/www/html/*
}

# Function to configure the web server
configure_server() {
    if [ "$SERVER_TYPE" == "nginx" ]; then
        # Create a new server block for Nginx
        sudo tee $SERVER_CONFIG > /dev/null <<EOL
server {
    listen 80;
    server_name example.com; # Replace with your domain name

    location / {
        root /var/www/html;
        index index.html index.htm;
    }

    error_page 404 /404.html; # Custom 404 error page
}
EOL
        # Enable the new site and restart Nginx
        sudo ln -s $SERVER_CONFIG /etc/nginx/sites-enabled/
        sudo systemctl restart nginx
    elif [ "$SERVER_TYPE" == "apache" ]; then
        # Create and enable a new Apache configuration file
        sudo tee /etc/apache2/sites-available/mywebsite.conf > /dev/null <<EOL
<VirtualHost *:80>
    ServerName example.com # Replace with your domain name
    DocumentRoot /var/www/html

    <Directory /var/www/html>
        AllowOverride All
    </Directory>

    ErrorDocument 404 /404.html # Custom 404 error page
</VirtualHost>
EOL
        # Enable the new site and restart Apache
        sudo a2ensite mywebsite.conf
        sudo systemctl restart apache2
    else
        echo "Error: Unsupported server type. Please use 'nginx' or 'apache'."
        exit 1
    fi
}

# Main script execution
check_server $SERVER_TYPE
deploy_website
configure_server

echo "Website deployed successfully. Please visit your domain to verify."
```
