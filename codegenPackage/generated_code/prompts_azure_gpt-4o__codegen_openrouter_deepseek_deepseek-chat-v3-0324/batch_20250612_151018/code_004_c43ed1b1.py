"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3338--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Create a StackScript to deploy a web server on a Linode Standard instance, including installation of Nginx and SSL configuration.
Generated: DETERMINISTIC_c43ed1b15b99eb0c
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

# StackScript to deploy a web server on a Linode Standard instance
# Includes Nginx installation and SSL configuration with Let's Encrypt

# <UDF name="hostname" label="Server Hostname" example="example.com" default="">
# <UDF name="email" label="Admin Email" example="admin@example.com" default="">
# <UDF name="username" label="Limited User Account" example="webadmin" default="">
# <UDF name="password" label="Password for Limited User" example="securePassword123" default="">
# <UDF name="ssh_key" label="SSH Public Key for Limited User" example="ssh-rsa AAAAB3Nza..." default="">

# Update system and install dependencies
apt-get update -y
apt-get upgrade -y
apt-get install -y nginx certbot python3-certbot-nginx ufw

# Configure firewall
ufw allow 'Nginx Full'
ufw allow 'OpenSSH'
ufw --force enable

# Create limited user account
if [ -n "$USERNAME" ]; then
    useradd -m -s /bin/bash "$USERNAME"
    echo "$USERNAME:$PASSWORD" | chpasswd
    usermod -aG sudo "$USERNAME"
    
    if [ -n "$SSH_KEY" ]; then
        mkdir -p /home/"$USERNAME"/.ssh
        echo "$SSH_KEY" >> /home/"$USERNAME"/.ssh/authorized_keys
        chown -R "$USERNAME":"$USERNAME" /home/"$USERNAME"/.ssh
        chmod 700 /home/"$USERNAME"/.ssh
        chmod 600 /home/"$USERNAME"/.ssh/authorized_keys
    fi
    
    # Disable root SSH login
    sed -i 's/^PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
    systemctl restart sshd
fi

# Configure Nginx
if [ -n "$HOSTNAME" ]; then
    cat > /etc/nginx/sites-available/"$HOSTNAME" <<EOF
server {
    listen 80;
    server_name $HOSTNAME www.$HOSTNAME;
    root /var/www/$HOSTNAME/html;
    index index.html index.htm index.nginx-debian.html;

    location / {
        try_files \$uri \$uri/ =404;
    }
}
EOF

    mkdir -p /var/www/"$HOSTNAME"/html
    chown -R www-data:www-data /var/www/"$HOSTNAME"/html
    chmod -R 755 /var/www/"$HOSTNAME"
    
    echo "<html><head><title>Welcome to $HOSTNAME</title></head><body><h1>Success! The $HOSTNAME server is working!</h1></body></html>" > /var/www/"$HOSTNAME"/html/index.html
    
    ln -s /etc/nginx/sites-available/"$HOSTNAME" /etc/nginx/sites-enabled/
    rm /etc/nginx/sites-enabled/default
    nginx -t && systemctl restart nginx
    
    # Obtain SSL certificate
    if [ -n "$EMAIL" ]; then
        certbot --nginx -d "$HOSTNAME" -d "www.$HOSTNAME" --non-interactive --agree-tos -m "$EMAIL"
        systemctl restart nginx
        
        # Set up automatic renewal
        (crontab -l 2>/dev/null; echo "0 12 * * * /usr/bin/certbot renew --quiet") | crontab -
    fi
fi

echo "Web server setup complete!"
echo "Nginx is running with SSL configured for $HOSTNAME"
echo "Limited user account $USERNAME has been created"
```
