"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webautomigrate.hstn.me
Prompt: Write a sample configuration for enabling SSL on a website hosted with iFastNet, including the steps for obtaining a free SSL certificate.
Generated: DETERMINISTIC_fd378c067212bbbc
Batch ID: 20250612_155401
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://$host$request_uri;": {
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
# Sample configuration for enabling SSL on a website hosted with iFastNet

# Step 1: Obtain a Free SSL Certificate
# You can obtain a free SSL certificate from Let's Encrypt or other providers.
# Below are the steps for using Certbot to get an SSL certificate from Let's Encrypt.

# 1. Install Certbot
# For Debian/Ubuntu systems, run:
sudo apt-get update
sudo apt-get install certbot

# 2. Generate SSL Certificate
# Replace 'example.com' with your domain name.
sudo certbot certonly --standalone -d example.com -d www.example.com

# Step 2: Configure Apache/Nginx to Use SSL
# Below are sample configurations for Apache and Nginx.

# Apache Configuration
# Create a new configuration file for your site
# Replace 'example.com' with your domain name
sudo nano /etc/apache2/sites-available/example.com.conf

# Add the following configuration:
<VirtualHost *:80>
    ServerName example.com
    ServerAlias www.example.com
    Redirect permanent / https://example.com/
</VirtualHost>

<VirtualHost *:443>
    ServerName example.com
    ServerAlias www.example.com

    DocumentRoot /var/www/example.com

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/example.com/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/example.com/privkey.pem

    <Directory /var/www/example.com>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/example.com-error.log
    CustomLog ${APACHE_LOG_DIR}/example.com-access.log combined
</VirtualHost>

# Enable the SSL module and the site configuration
sudo a2enmod ssl
sudo a2ensite example.com.conf
sudo systemctl restart apache2

# Nginx Configuration
# Create a new configuration file for your site
# Replace 'example.com' with your domain name
sudo nano /etc/nginx/sites-available/example.com

# Add the following configuration:
server {
    listen 80;
    server_name example.com www.example.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name example.com www.example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    location / {
        root /var/www/example.com;
        index index.html index.htm;
        try_files $uri $uri/ =404;
    }

    error_log /var/log/nginx/example.com-error.log;
    access_log /var/log/nginx/example.com-access.log;
}

# Enable the site configuration and restart Nginx
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
sudo systemctl restart nginx

# Step 3: Set Up Automatic Renewal of SSL Certificate
# Let's Encrypt certificates expire every 90 days. To automate the renewal process, add a cron job.

# Open the crontab configuration
crontab -e

# Add the following line to renew certificates automatically
0 0 * * * /usr/bin/certbot renew --quiet

# This cron job runs the renewal command daily at midnight and suppresses output unless there is an error.
```
