"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.magpiexyz.click
Prompt: Can you provide code examples for setting up a web server to avoid default pages, specifically for Apache or Nginx?
Generated: DETERMINISTIC_f1686969d772e45d
Batch ID: 20250612_162409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### Apache Configuration Example

```apache
# Apache Configuration to Avoid Default Pages

# Load required modules
LoadModule deflate_module modules/mod_deflate.so
LoadModule headers_module modules/mod_headers.so

# Define the server configuration
<VirtualHost *:80>
    # Set the server name
    ServerName example.com
    ServerAlias www.example.com

    # Document root for the website
    DocumentRoot "/var/www/example"

    # Disable directory listing
    Options -Indexes

    # Custom error document for 404 Not Found
    ErrorDocument 404 /custom_404.html

    # Redirect default pages to a custom page
    RewriteEngine On
    RewriteCond %{THE_REQUEST} ^[A-Z]{3,}\s/+(index\.html|index\.php|default\.html)\s [NC]
    RewriteRule ^(.*)$ /custom_page.html [R=301,L]

    # Add security headers
    Header always set X-Content-Type-Options "nosniff"
    Header always set X-XSS-Protection "1; mode=block"
    Header always set X-Frame-Options "DENY"

    # Ensure logs are written for requests and errors
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

### Nginx Configuration Example

```nginx
# Nginx Configuration to Avoid Default Pages

server {
    # Listen on port 80
    listen 80;
    server_name example.com www.example.com;

    # Root directory for the server
    root /var/www/example;

    # Disable directory listing
    autoindex off;

    # Custom error page for 404 Not Found
    error_page 404 /custom_404.html;

    # Redirect default pages to a custom page
    location = / {
        rewrite ^/(index\.html|index\.php|default\.html)$ /custom_page.html permanent;
    }

    # Add security headers
    add_header X-Content-Type-Options "nosniff";
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Frame-Options "DENY";

    # Logging configuration
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;
}
```
