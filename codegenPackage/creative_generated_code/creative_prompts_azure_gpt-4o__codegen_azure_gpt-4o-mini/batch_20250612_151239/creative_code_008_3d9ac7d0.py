"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-v2.org
Prompt: Write a script in Bash to automate the setup of a web server that serves a "Success! Your new web server is ready to use." message.
Generated: DETERMINISTIC_3d9ac7d07052eab2
Batch ID: 20250612_151239
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost/": {
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

# web_server_setup.sh
# This script automates the setup of a simple web server using Nginx.
# It serves a basic HTML message indicating that the server is ready.

# Exit immediately if a command exits with a non-zero status
set -e 

# Function to install Nginx
install_nginx() {
    echo "Installing Nginx..."
    sudo apt update
    sudo apt install -y nginx
}

# Function to configure Nginx to serve a custom HTML page
configure_nginx() {
    echo "Configuring Nginx..."
    
    # Create a directory for the web content
    sudo mkdir -p /var/www/html

    # Create an HTML file with a success message
    echo "<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Web Server Setup</title>
</head>
<body>
    <h1>Success! Your new web server is ready to use.</h1>
</body>
</html>" | sudo tee /var/www/html/index.html > /dev/null

    # Set permissions
    sudo chown -R www-data:www-data /var/www/html
    sudo chmod -R 755 /var/www/html
}

# Function to start Nginx
start_nginx() {
    echo "Starting Nginx..."
    sudo systemctl start nginx
    sudo systemctl enable nginx
}

# Main script execution
main() {
    install_nginx
    configure_nginx
    start_nginx
    echo "Web server setup complete! You can visit it at http://localhost/"
}

# Execute the main function
main
```

### Usage:
1. Save the script as `web_server_setup.sh`.
2. Make it executable: `chmod +x web_server_setup.sh`.
3. Run the script: `./web_server_setup.sh`. 

### Note:
- This script is designed for Ubuntu or Debian-based systems. Adjust package management commands for other distributions as necessary.
