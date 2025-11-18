"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abelltodoit.com.au
Prompt: Write a tutorial on setting up LiteSpeed Web Server to serve directories like those shown on https://abelltodoit.com.au, including `css`, `img`, and `js`.
Generated: DETERMINISTIC_2f1d1a1ca87b0961
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a sample configuration script written in bash, along with a LiteSpeed Web Server configuration file, to set up a LiteSpeed Web Server that serves directories (`css`, `img`, `js`) similar to the website you mentioned.

```bash
#!/bin/bash

# Script to set up LiteSpeed Web Server and configure it for serving static directories

# Exit immediately if a command exits with a non-zero status
set -e

# Update package lists and install LiteSpeed Web Server
echo "Updating package lists..."
sudo apt update

echo "Installing LiteSpeed Web Server..."
sudo apt install -y openlitespeed

# Start and enable LiteSpeed service
echo "Starting LiteSpeed Web Server..."
sudo systemctl start lsws

echo "Enabling LiteSpeed Web Server to start on boot..."
sudo systemctl enable lsws

# Create the directory structure for the static files
echo "Creating directory structure..."
sudo mkdir -p /usr/local/lsws/ExampleSite/{css,img,js}

# Set permissions for the directories
echo "Setting permissions..."
sudo chown -R nobody:nogroup /usr/local/lsws/ExampleSite
sudo chmod -R 755 /usr/local/lsws/ExampleSite

# Sample static files for demonstration purposes
echo "Creating sample static files..."
echo "body { background-color: #f0f0f0; }" | sudo tee /usr/local/lsws/ExampleSite/css/style.css > /dev/null
echo "<script>alert('Hello World!');</script>" | sudo tee /usr/local/lsws/ExampleSite/js/script.js > /dev/null
echo "<img src='/img/example.png' alt='Example Image'>" | sudo tee /usr/local/lsws/ExampleSite/index.html > /dev/null

# Configuration for LiteSpeed Web Server to serve the example site
echo "Configuring LiteSpeed Web Server..."
CONFIG_FILE="/usr/local/lsws/conf/httpd_config.conf"

sudo bash -c "cat > $CONFIG_FILE" <<EOF
# LiteSpeed Web Server main configuration file

# Listener for HTTP traffic
listener Default {
    address                 *:80
    secure                  0
}

# Virtual Host configuration
virtualhost ExampleSite {
    vhRoot                  /usr/local/lsws/ExampleSite
    configFile              /usr/local/lsws/ExampleSite/conf/vhost.conf
    allowSymbolLink         1
    enableScript            1
    restrainPolicy          0
}

# Map the listener to the virtual host
listener Default {
    # The ExampleSite virtual host is mapped to this listener
    map                     ExampleSite *
}
EOF

# Create the virtual host configuration file
echo "Creating virtual host configuration file..."
sudo mkdir -p /usr/local/lsws/ExampleSite/conf
VHOST_CONFIG="/usr/local/lsws/ExampleSite/conf/vhost.conf"

sudo bash -c "cat > $VHOST_CONFIG" <<EOF
# Virtual Host configuration

docRoot                   /usr/local/lsws/ExampleSite
indexFiles                index.html, index.php

# Logging configuration
errorlog                  /usr/local/lsws/ExampleSite/logs/error.log
accesslog                 /usr/local/lsws/ExampleSite/logs/access.log

# Static content handling
expires                   1d
EOF

# Restart LiteSpeed Web Server to apply changes
echo "Restarting LiteSpeed Web Server..."
sudo systemctl restart lsws

echo "LiteSpeed Web Server configuration is complete!"
echo "Your static files should now be accessible at http://<your-server-ip>/"
```

This script assumes you're using a Linux-based system and have the requisite permissions to install and configure LiteSpeed Web Server.
