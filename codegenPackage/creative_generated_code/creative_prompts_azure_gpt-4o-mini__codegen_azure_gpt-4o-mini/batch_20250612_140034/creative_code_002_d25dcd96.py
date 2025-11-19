"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prohoster.biz
Prompt: Write a script to automate the installation of WordPress on a ProHoster VPS with PHP version selection.
Generated: DETERMINISTIC_d25dcd9681b89b2f
Batch ID: 20250612_140034
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://wordpress.org/latest.zip": {
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

# Script to automate the installation of WordPress on a ProHoster VPS with PHP version selection

# Exit script on any error
set -e

# Function to display usage instructions
usage() {
    echo "Usage: $0 -p <php_version> -d <database_name> -u <db_user> -p <db_password>"
    echo "  -p  PHP version to use (e.g., 7.4, 8.0, etc.)"
    echo "  -d  Database name for WordPress"
    echo "  -u  Database user for WordPress"
    echo "  -p  Database password for WordPress"
    exit 1
}

# Parse command line arguments
while getopts ":p:d:u:p:" opt; do
    case ${opt} in
        p )
            php_version=$OPTARG
            ;;
        d )
            db_name=$OPTARG
            ;;
        u )
            db_user=$OPTARG
            ;;
        p )
            db_password=$OPTARG
            ;;
        \? )
            usage
            ;;
    esac
done

# Check if all required arguments are provided
if [ -z "${php_version}" ] || [ -z "${db_name}" ] || [ -z "${db_user}" ] || [ -z "${db_password}" ]; then
    usage
fi

# Update package repository and install required packages
echo "Updating package repository..."
sudo apt update

echo "Installing necessary packages..."
sudo apt install -y nginx mysql-server php${php_version} php${php_version}-mysql php${php_version}-fpm wget unzip

# Start and enable services
echo "Starting and enabling services..."
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl start mysql
sudo systemctl enable mysql

# Secure MySQL installation
echo "Securing MySQL installation..."
sudo mysql_secure_installation <<EOF

y
${db_password}
${db_password}
y
y
y
y
EOF

# Create WordPress database
echo "Creating WordPress database..."
sudo mysql -u root -p${db_password} -e "CREATE DATABASE ${db_name};"
sudo mysql -u root -p${db_password} -e "CREATE USER '${db_user}'@'localhost' IDENTIFIED BY '${db_password}';"
sudo mysql -u root -p${db_password} -e "GRANT ALL PRIVILEGES ON ${db_name}.* TO '${db_user}'@'localhost';"
sudo mysql -u root -p${db_password} -e "FLUSH PRIVILEGES;"

# Download and install WordPress
echo "Downloading WordPress..."
wget -c https://wordpress.org/latest.zip -O /tmp/wordpress.zip

echo "Unzipping WordPress..."
unzip /tmp/wordpress.zip -d /tmp/

# Configure WordPress
echo "Configuring WordPress..."
cp /tmp/wordpress/wp-config-sample.php /tmp/wordpress/wp-config.php
sed -i "s/database_name_here/${db_name}/" /tmp/wordpress/wp-config.php
sed -i "s/username_here/${db_user}/" /tmp/wordpress/wp-config.php
sed -i "s/password_here/${db_password}/" /tmp/wordpress/wp-config.php

# Move WordPress files to web root
echo "Moving WordPress files to the web root..."
sudo mv /tmp/wordpress/* /var/www/html/

# Set appropriate permissions
echo "Setting permissions..."
sudo chown -R www-data:www-data /var/www/html/
sudo find /var/www/html/ -type d -exec chmod 755 {} \;
sudo find /var/www/html/ -type f -exec chmod 644 {} \;

# Configure Nginx
echo "Configuring Nginx for WordPress..."
cat <<EOL | sudo tee /etc/nginx/sites-available/wordpress
server {
    listen 80;
    server_name your_domain_or_IP;  # Replace with your domain or IP

    root /var/www/html;
    index index.php index.html index.htm;

    location / {
        try_files \$uri \$uri/ /index.php?\$args;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php${php_version}-fpm.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME \$document_root\$fastcgi_script_name;
        include fastcgi_params;
    }

    location ~ /\.ht {
        deny all;
    }
}
EOL

# Enable the Nginx configuration
sudo ln -s /etc/nginx/sites-available/wordpress /etc/nginx/sites-enabled/
sudo nginx -t

# Reload Nginx to apply changes
echo "Reloading Nginx..."
sudo systemctl reload nginx

# Cleanup
echo "Cleaning up..."
rm /tmp/wordpress.zip

# Display completion message
echo "WordPress installation on ProHoster VPS is complete."
echo "Visit your site to finish the WordPress setup."
```
