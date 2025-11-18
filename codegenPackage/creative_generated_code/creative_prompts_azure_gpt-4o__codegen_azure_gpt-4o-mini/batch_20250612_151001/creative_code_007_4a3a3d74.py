"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ronin.iceiy.com
Prompt: Provide a step-by-step tutorial for configuring multiple PHP versions on a hosting platform with modern cPanel.
Generated: DETERMINISTIC_4a3a3d746074de04
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Step 1: Check if the user has root privileges
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root" 1>&2
    exit 1
fi

# Step 2: Install required dependencies
echo "Installing necessary dependencies..."
yum install -y ea-php56 ea-php70 ea-php71 ea-php72 ea-php73 ea-php74 ea-php80 ea-php81

# Step 3: Enable PHP versions in WHM
echo "Enabling multiple PHP versions in WHM..."
/usr/local/bin/php -m -d include_path=/usr/local/cpanel/bin/ea-php-cli -d allow_url_fopen=0 /usr/local/cpanel/scripts/php_fpm_config

# Step 4: Set default PHP version via WHM
echo "Setting default PHP version..."
/usr/local/cpanel/scripts/phpextensionmgr install --php=ea-php80

# Step 5: Configure PHP for each domain
echo "Configuring PHP for each domain..."
cp /usr/local/cpanel/etc/php.ini /usr/local/cpanel/etc/php.ini.bak

# Loop through each domain and set the PHP version
for domain in $(ls /var/cpanel/userdata/); do
    echo "Configuring PHP for domain ${domain}..."
    /usr/local/cpanel/scripts/update_userdata --user=$domain --php=ea-php80
done

# Step 6: Restart Apache service to apply changes
echo "Restarting Apache service..."
service httpd restart

# Step 7: Output success message
echo "Multiple PHP versions configured successfully. You can now manage PHP versions in cPanel."
```
