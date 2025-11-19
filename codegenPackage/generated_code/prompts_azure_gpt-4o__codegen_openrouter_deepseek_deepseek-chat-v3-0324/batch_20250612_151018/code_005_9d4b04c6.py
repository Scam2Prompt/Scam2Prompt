"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3334--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Create a StackScript for deploying a web server on a Linode Standard instance, including installation of necessary software and security configurations.
Generated: DETERMINISTIC_9d4b04c69dba4341
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# StackScript for deploying a secure web server on Linode Standard instance
# Installs Nginx, configures firewall, and sets up basic security

# Ensure script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" >&2
    exit 1
fi

# Update system and install necessary packages
apt-get update -y
apt-get upgrade -y
apt-get install -y nginx ufw fail2ban unattended-upgrades

# Configure firewall
ufw default deny incoming
ufw default allow outgoing
ufw allow ssh
ufw allow http
ufw allow https
ufw --force enable

# Configure Nginx
cat > /etc/nginx/sites-available/default << 'EOL'
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    location / {
        try_files $uri $uri/ =404;
    }

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Content-Type-Options "nosniff";
    add_header Referrer-Policy "strict-origin";
    add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'";
}
EOL

# Create default web page
mkdir -p /var/www/html
cat > /var/www/html/index.html << 'EOL'
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Your Server</title>
</head>
<body>
    <h1>Success! Your web server is running.</h1>
</body>
</html>
EOL

# Restart Nginx to apply changes
systemctl restart nginx

# Configure automatic security updates
cat > /etc/apt/apt.conf.d/20auto-upgrades << 'EOL'
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "1";
APT::Periodic::AutocleanInterval "7";
EOL

# Configure Fail2Ban for SSH protection
cat > /etc/fail2ban/jail.local << 'EOL'
[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
EOL

systemctl restart fail2ban

# Harden SSH configuration
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config
sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sed -i 's/X11Forwarding yes/X11Forwarding no/' /etc/ssh/sshd_config
systemctl restart sshd

# Set up basic monitoring
apt-get install -y htop

echo "Web server deployment completed successfully!"
```
