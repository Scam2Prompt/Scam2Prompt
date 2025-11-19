"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soniclabes.org
Prompt: Can you provide code examples for serving static files using Apache on a Debian server like the one at soniclabes.org?
Generated: DETERMINISTIC_627ea8190569ac4d
Batch ID: 20250612_155801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Update package index
sudo apt update

# Install Apache web server if not already installed
sudo apt install -y apache2

# Enable the mod_alias module for serving static files
sudo a2enmod alias

# Create a directory for your static files
sudo mkdir -p /var/www/soniclabes.org/static

# Set proper permissions for the static directory
sudo chown -R www-data:www-data /var/www/soniclabes.org/static
sudo chmod -R 755 /var/www/soniclabes.org/static

# Create a sample HTML file in the static directory
echo "<html><body><h1>Welcome to Sonic Labes Static Files</h1></body></html>" | sudo tee /var/www/soniclabes.org/static/index.html

# Define a virtual host configuration for soniclabes.org
sudo tee /etc/apache2/sites-available/soniclabes.org.conf > /dev/null <<EOL
<VirtualHost *:80>
    ServerName soniclabes.org
    DocumentRoot /var/www/soniclabes.org/static

    <Directory /var/www/soniclabes.org/static>
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/soniclabes_error.log
    CustomLog ${APACHE_LOG_DIR}/soniclabes_access.log combined
</VirtualHost>
EOL

# Enable the new site configuration
sudo a2ensite soniclabes.org.conf

# Disable the default Apache site if necessary
sudo a2dissite 000-default.conf

# Test the Apache configuration for syntax errors
sudo apache2ctl configtest

# If the configuration test is successful, reload Apache to apply changes
if [ $? -eq 0 ]; then
    sudo systemctl reload apache2
else
    echo "Apache configuration error. Please check the configuration."
fi

# Print the final message to indicate setup completion
echo "Apache is set up to serve static files for soniclabes.org"
```
