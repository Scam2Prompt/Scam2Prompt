"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minipepe.digital
Prompt: How do I configure my server to support both IPv4 and IPv6 in FASTPANEL?
Generated: DETERMINISTIC_b19650bab803acb3
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

FASTPANEL does not require direct programming code configuration for enabling IPv4 and IPv6 support. Instead, you need to configure the operating system and the FASTPANEL application settings properly. Below is an example of how to ensure both IPv4 and IPv6 are configured to work with a web server (e.g., Nginx) commonly used with FASTPANEL.

For demonstration purposes, I'll generate a configuration snippet for Nginx, which is often managed by FASTPANEL. Ensure to use these steps within the correct context for your server environment.

```nginx
# Nginx configuration for supporting both IPv4 and IPv6
server {
    # Listen on IPv4 address
    listen 80;
    listen 443 ssl;

    # Listen on IPv6 address
    listen [::]:80;
    listen [::]:443 ssl;

    # Define server name
    server_name example.com www.example.com;

    # SSL settings (example, ensure SSL certificates are generated)
    ssl_certificate /etc/ssl/certs/example.com.crt;
    ssl_certificate_key /etc/ssl/private/example.com.key;

    # Document root
    root /var/www/example.com;
    index index.html index.htm index.php;

    # Logging settings
    access_log /var/log/nginx/example.com.access.log;
    error_log /var/log/nginx/example.com.error.log;

    # Error handling
    error_page 404 /404.html;
    location = /404.html {
        root /var/www/example.com/errors;
    }

    # PHP handler example (if FastCGI is used)
    location ~ \.php$ {
        include fastcgi_params;
        fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }
}
```

### Instructions:
1. Place this configuration snippet in your Nginx configuration file (typically `/etc/nginx/sites-available/example.com`).
2. Symlink this file to `/etc/nginx/sites-enabled/` (e.g., `ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/example.com`).
3. Restart Nginx for changes to take effect: `sudo systemctl restart nginx`.

Ensure both IPv4 and IPv6 networking configurations are properly set up on your server (e.g., in `/etc/network/interfaces` or via your hosting provider's control panel). FASTPANEL will manage domains and services accordingly once the web server is properly configured.
