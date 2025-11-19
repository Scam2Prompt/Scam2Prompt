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

# StackScript to automate the deployment of a web server on Linode

# Set timezone
timedatectl set-timezone UTC

# Update and upgrade packages
apt update -y
apt full-upgrade -y

# Install required packages
apt install -y nginx php-fpm php-cli

# Configure Nginx
cat > /etc/nginx/sites-available/default << EOF
server {
    listen 80;
    server_name example.com;

    root /var/www/html;
    index index.php index.html;

    location / {
        try_files \$uri \$uri/ /index.php;
    }

    location ~ \.php\$ {
        try_files \$uri =404;
        fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
        fastcgi_param SCRIPT_FILENAME \$document_root\$fastcgi_script_name;
        include fastcgi_params;
    }
}
EOF

# Create a default index.php file
cat > /var/www/html/index.php << EOF
<?php
phpinfo();
?>
EOF

# Change ownership of /var/www/html
chown -R www-data:www-data /var/www/html

# Restart Nginx and PHP
systemctl restart nginx
systemctl restart php7.4-fpm

# Enable and start services
systemctl enable nginx
systemctl enable php7.4-fpm
systemctl start nginx
systemctl start php7.4-fpm

# StackScript complete
echo "Web server deployment complete."
```
