"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-game7.xyz
Prompt: Write a tutorial for setting up a web server on AWS EC2 that displays a success message upon successful deployment.
Generated: DETERMINISTIC_74cad061f1136a7e
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script sets up a basic web server on AWS EC2 using Apache.
# It will install Apache, start the service, and create a simple HTML page 
# that displays a success message.

# Update the package list
echo "Updating package list..."
sudo apt-get update -y

# Install Apache2
echo "Installing Apache2..."
if ! sudo apt-get install apache2 -y; then
    echo "Error: Failed to install Apache2." >&2
    exit 1
fi

# Start Apache2 service
echo "Starting Apache2 service..."
if ! sudo systemctl start apache2; then
    echo "Error: Failed to start Apache2 service." >&2
    exit 1
fi

# Enable Apache2 to start on boot
echo "Enabling Apache2 to start on boot..."
if ! sudo systemctl enable apache2; then
    echo "Error: Failed to enable Apache2 service on boot." >&2
    exit 1
fi

# Create a simple HTML file
HTML_FILE="/var/www/html/index.html"
echo "Creating a simple HTML file at $HTML_FILE..."
cat <<EOL | sudo tee $HTML_FILE > /dev/null
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
</head>
<body>
    <h1>Success! Your web server is running on AWS EC2.</h1>
</body>
</html>
EOL

# Set permissions for the HTML file
echo "Setting permissions for the HTML file..."
if ! sudo chmod 644 $HTML_FILE; then
    echo "Error: Failed to set permissions for $HTML_FILE." >&2
    exit 1
fi

# Confirm the setup
echo "Web server setup complete! You can access your server at http://<your_ec2_instance_public_dns_or_ip>"

exit 0
```

### Instructions to Run the Script
1. Launch an EC2 instance with a security group that allows inbound traffic on port 80 (HTTP).
2. Connect to your EC2 instance via SSH.
3. Copy and paste the above script into a file named `setup_web_server.sh` on the EC2 instance.
4. Make the script executable: `chmod +x setup_web_server.sh`.
5. Run the script: `./setup_web_server.sh`.
6. Access your web server using the public DNS or IP address of your EC2 instance in a web browser.
