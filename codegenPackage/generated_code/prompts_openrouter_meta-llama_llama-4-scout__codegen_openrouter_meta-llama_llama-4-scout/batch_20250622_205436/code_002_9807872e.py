"""
Generated Code Metadata:
========================
Original URL: https://prohoster.biz
Prompt: "Generate a bash script to install and configure a Drupal site on a ProHoster VPS server with a specific PHP version and modules."
Generated: DETERMINISTIC_9807872ee8d62550
Batch ID: 20250622_205436
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.drupal.org/download/$DRUPAL_VERSION/drupal-$DRUPAL_VERSION.tar.gz": {
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

# Define variables
DRUPAL_VERSION="9.5.5"
PHP_VERSION="8.1"
DB_NAME="drupal_db"
DB_USER="drupal_user"
DB_PASSWORD="drupal_password"
DB_HOST="localhost"
DOMAIN="example.com"

# Update and upgrade system
echo "Updating and upgrading system..."
sudo apt update -y
sudo apt upgrade -y

# Install required packages
echo "Installing required packages..."
sudo apt install -y git curl unzip

# Install PHP and required modules
echo "Installing PHP $PHP_VERSION and required modules..."
sudo apt install -y php$PHP_VERSION php$PHP_VERSION-fpm php$PHP_VERSION-cli php$PHP_VERSION-mysql php$PHP_VERSION-gd php$PHP_VERSION-dom php$PHP_VERSION-simplexml

# Configure PHP
echo "Configuring PHP..."
sudo tee /etc/php/$PHP_VERSION/fpm/php.ini <<EOF
memory_limit = 512M
max_execution_time = 300
upload_max_filesize = 100M
post_max_size = 100M
EOF

# Restart PHP service
echo "Restarting PHP service..."
sudo systemctl restart php$PHP_VERSION-fpm

# Install and configure database
echo "Installing and configuring database..."
sudo apt install -y mariadb-server
sudo mysql_secure_installation <<EOF
y
$DB_PASSWORD
$DB_PASSWORD
y
y
y
y
EOF

# Create database and user
echo "Creating database and user..."
sudo mysql -e "CREATE DATABASE $DB_NAME;"
sudo mysql -e "CREATE USER '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASSWORD';"
sudo mysql -e "GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_USER'@'localhost';"
sudo mysql -e "FLUSH PRIVILEGES;"

# Download and extract Drupal
echo "Downloading and extracting Drupal..."
wget https://www.drupal.org/download/$DRUPAL_VERSION/drupal-$DRUPAL_VERSION.tar.gz
tar -xvf drupal-$DRUPAL_VERSION.tar.gz
sudo mv drupal-$DRUPAL_VERSION /var/www/html/$DOMAIN

# Change ownership and permissions
echo "Changing ownership and permissions..."
sudo chown -R www-data:www-data /var/www/html/$DOMAIN
sudo chmod -R 755 /var/www/html/$DOMAIN

# Configure Drupal
echo "Configuring Drupal..."
sudo tee /var/www/html/$DOMAIN/sites/default/settings.php <<EOF
<?php
\$databases = array (
  'default' => array (
    'default' => array (
      'driver' => 'mysql',
      'database' => '$DB_NAME',
      'username' => '$DB_USER',
      'password' => '$DB_PASSWORD',
      'host' => '$DB_HOST',
      'port' => '',
      'prefix' => '',
    ),
  ),
);
?>
EOF

# Enable required modules
echo "Enabling required modules..."
sudo chdir /var/www/html/$DOMAIN
sudo drush en -y admin_toolbar admin_toolbar_tools views views_ui

# Set domain and restart services
echo "Setting domain and restarting services..."
sudo tee /etc/nginx/sites-available/$DOMAIN <<EOF
server {
    listen 80;
    server_name $DOMAIN;
    root /var/www/html/$DOMAIN;
    index index.php index.html index.htm;

    location / {
        try_files \$uri \$uri/ /index.php;
    }

    location ~ \.php\$ {
        try_files \$uri =404;
        fastcgi_pass unix:/var/run/php/php$PHP_VERSION-fpm.sock;
        fastcgi_param SCRIPT_FILENAME \$document_root\$fastcgi_script_name;
        include fastcgi_params;
    }
}
EOF
sudo ln -s /etc/nginx/sites-available/$DOMAIN /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

To use this script, save it to a file (e.g., `drupal_setup.sh`), give it execute permissions with `chmod +x drupal_setup.sh`, and then run it with `./drupal_setup.sh`. Make sure to replace the variables at the top of the script with your own values.
