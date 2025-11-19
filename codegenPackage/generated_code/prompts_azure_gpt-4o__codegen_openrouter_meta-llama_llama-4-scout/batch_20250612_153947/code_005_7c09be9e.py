"""
Generated Code Metadata:
========================
Original URL: https://claimairtoday.com
Prompt: Provide code examples for setting up an SSL certificate on a FASTPANEL-managed server to ensure HTTPS access works correctly.
Generated: DETERMINISTIC_7c09be9e97267eed
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Setup SSL Certificate on FASTPANEL-Managed Server**
=====================================================

### Prerequisites

* FASTPANEL-managed server with root access
* Domain name configured on the server

### Generate Certificate Signing Request (CSR) and Private Key

```bash
# Generate private key
openssl genrsa -out /path/to/private.key 2048

# Generate CSR
openssl req -new -key /path/to/private.key -out /path/to/csr.csr -subj "/C=US/ST=State/L=Locality/O=Organization/CN=example.com"
```

### Obtain SSL Certificate from Certificate Authority (CA)

* Submit the CSR to a CA (e.g., Let's Encrypt, GlobalSign) to obtain an SSL certificate.

### Install SSL Certificate on FASTPANEL-Managed Server

```bash
# Copy SSL certificate and private key to server
scp /path/to/certificate.crt /path/to/private.key user@fastpanel-server:/home/user/

# Log in to FASTPANEL server
ssh user@fastpanel-server

# Create a new SSL configuration file
sudo nano /etc/nginx/ssl.conf
```

### SSL Configuration File (`/etc/nginx/ssl.conf`)

```nginx
server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+ECDSA+AESGCM EECDH+aRSA+AESGCM EECDH+ECDSA+SHA384 EECDH+ECDSA+SHA256 EECDH+aRSA+SHA384 EECDH+aRSA+SHA256 EECDH+aRSA+RC4 EECDH EDH+aRSA RC4 !aNULL !eNULL !LOW !3DES !MD5 !EXP !PSK !SRP !DSS";
    ssl_session_cache shared:SSL:10m;
    ssl_session_tickets off;
    ssl_stapling on;
    ssl_stapling_verify on;

    # Your website configuration...
    location / {
        # ...
    }
}
```

### Configure NGINX to Use SSL Configuration

```bash
# Update NGINX configuration to include SSL configuration
sudo nano /etc/nginx/nginx.conf

# Add the following line to the http or server block
include /etc/nginx/ssl.conf;

# Restart NGINX to apply changes
sudo service nginx restart
```

### Renew SSL Certificate

* Set up a cron job to renew the SSL certificate automatically:

```bash
# Open crontab editor
crontab -e

# Add the following line to renew the certificate 30 days before expiration
0 0 * * * /usr/bin/certbot renew --force --expand --email your_email@example.com --agree-tos --non-interactive --nginx --domain -d example.com,www.example.com
```

### Error Handling and Logging

* Configure NGINX logging to monitor SSL errors:

```nginx
error_log /var/log/nginx/error.log;
```

### Production-Ready Verification

* Verify HTTPS access works correctly:

```bash
# Test SSL certificate
openssl s_client -connect example.com:443 -servername example.com
```

* Check for any SSL-related errors or warnings in the NGINX error log:

```bash
# Check NGINX error log
sudo tail -f /var/log/nginx/error.log
```
