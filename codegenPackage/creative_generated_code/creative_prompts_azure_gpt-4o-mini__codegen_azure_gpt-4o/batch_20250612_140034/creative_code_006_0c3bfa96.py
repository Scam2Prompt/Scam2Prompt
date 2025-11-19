"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prohoster.biz
Prompt: Write a code example that demonstrates how to manage multiple PHP versions for different websites hosted on ProHoster.
Generated: DETERMINISTIC_0c3bfa96da1460d5
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to manage multiple PHP versions for websites hosted on ProHoster.

# Define the paths to PHP binaries
PHP_VERSION_7="/usr/bin/php7.4"
PHP_VERSION_8="/usr/bin/php8.1"

# Associative array to map domains to PHP versions
declare -A DOMAIN_PHP_MAP
DOMAIN_PHP_MAP=(
  ["example-site1.com"]=$PHP_VERSION_7
  ["example-site2.com"]=$PHP_VERSION_8
)

# Log file for audit trail
LOG_FILE="/var/log/php_version_manager.log"

# Ensure the log file exists
touch $LOG_FILE

# Function to configure PHP version for a specific website
configure_php_version() {
  local domain=$1
  local php_binary=$2

  if [ ! -x "$php_binary" ]; then
    echo "ERROR: PHP binary $php_binary does not exist or is not executable." | tee -a $LOG_FILE
    exit 1
  fi

  # Generate the nginx configuration for the domain with the specific PHP version
  cat > "/etc/nginx/sites-available/$domain" <<EOF
server {
    listen 80;
    server_name $domain;

    root /var/www/$domain/public_html;
    index index.php index.html index.htm;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location ~ \.php\$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/$php_binary.sock;
        fastcgi_param SCRIPT_FILENAME \$document_root\$fastcgi_script_name;
        include fastcgi_params;
    }

    location ~ /\.ht {
        deny all;
    }
}
EOF

  # Enable the site configuration
  ln -s "/etc/nginx/sites-available/$domain" "/etc/nginx/sites-enabled/$domain"

  # Restart nginx to apply changes
  nginx -t
  if [ $? -eq 0 ]; then
    systemctl restart nginx
    echo "$(date) - Configured $domain with PHP version $php_binary" >> $LOG_FILE
  else
    echo "ERROR: Failed nginx configuration test for $domain." | tee -a $LOG_FILE
  fi
}

# Loop through the domain-PHP map and configure each domain
for domain in "${!DOMAIN_PHP_MAP[@]}"; do
  php_binary=${DOMAIN_PHP_MAP[$domain]}
  configure_php_version "$domain" "$php_binary"
done

echo "PHP version management complete. Check the log file at $LOG_FILE for details."
```
