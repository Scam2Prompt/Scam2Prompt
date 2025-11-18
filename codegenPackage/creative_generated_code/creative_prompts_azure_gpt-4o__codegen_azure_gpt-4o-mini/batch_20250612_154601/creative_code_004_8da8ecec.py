"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solutechsystem.com.ng
Prompt: Provide a step-by-step guide to implement SSL certificates and WHOIS protection on a website, as described in Solutech System's web design services.
Generated: DETERMINISTIC_8da8ecec248adfc8
Batch ID: 20250612_154601
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://\\$host\\$request_uri;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:3000;": {
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

# Step 1: Install OpenSSL
echo "Installing OpenSSL..."
sudo apt-get update
sudo apt-get install -y openssl

# Step 2: Generate an SSL Certificate
DOMAIN="yourdomain.com"  # Replace with your domain
EMAIL="youremail@example.com"  # Replace with your email for Let's Encrypt notifications

echo "Generating SSL Certificate for $DOMAIN..."
sudo openssl req -new -newkey rsa:2048 -days 365 -nodes \
  -x509 -keyout /etc/ssl/private/$DOMAIN.key \
  -out /etc/ssl/certs/$DOMAIN.crt \
  -subj "/C=US/ST=State/L=City/O=Company Name/CN=$DOMAIN/emailAddress=$EMAIL"

# Step 3: Install Certbot for Let's Encrypt (optional for automatic renewal)
echo "Installing Certbot for Let's Encrypt SSL Certificate..."
sudo apt-get install -y certbot python3-certbot-nginx

# Step 4: Obtain a FREE SSL Certificate from Let's Encrypt
echo "Obtaining SSL Certificate from Let's Encrypt for $DOMAIN..."
sudo certbot certonly --nginx -d $DOMAIN --email $EMAIL --agree-tos --non-interactive

# Step 5: Configure Nginx to use the SSL Certificate
NGINX_CONF="/etc/nginx/sites-available/$DOMAIN"
echo "Configuring Nginx for SSL..."
sudo tee $NGINX_CONF > /dev/null <<EOL
server {
    listen 80;
    server_name $DOMAIN;
    return 301 https://\$host\$request_uri;  # Redirect HTTP to HTTPS
}

server {
    listen 443 ssl;
    server_name $DOMAIN;

    ssl_certificate /etc/letsencrypt/live/$DOMAIN/fullchain.pem;  # Path to SSL Cert
    ssl_certificate_key /etc/letsencrypt/live/$DOMAIN/privkey.pem;  # Path to SSL Key

    location / {
        proxy_pass http://localhost:3000;  # Update with your backend service
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
    }
}
EOL

# Step 6: Test Nginx Configuration
echo "Testing Nginx configuration..."
sudo nginx -t
if [ $? -ne 0 ]; then
    echo "Nginx configuration test failed. Please check the configuration."
    exit 1
fi

# Step 7: Restart Nginx to apply changes
echo "Restarting Nginx..."
sudo systemctl restart nginx

# Step 8: Set up WHOIS Protection (depends on the domain registrar)
echo "Setting up WHOIS protection..."
echo "Please visit your domain registrar's website and enable WHOIS privacy protection for $DOMAIN."

# Step 9: Schedule automatic renewal for Let's Encrypt certificates
echo "Setting up automatic renewal for Let's Encrypt certificates..."
sudo crontab -l | { cat; echo "0 3 * * * /usr/bin/certbot renew --quiet"; } | sudo crontab -

echo "SSL Certificate and WHOIS protection setup complete!"
```
