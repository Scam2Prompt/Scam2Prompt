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

Here is the configuration code for both Apache and Nginx web servers to avoid serving default pages:

---

### Apache Configuration
```apache
# Apache Virtual Host Configuration
# This configuration prevents serving default pages by returning a "403 Forbidden" error
# if no specific index file is available.

<VirtualHost *:80>
    ServerName example.com
    ServerAlias www.example.com

    # Define the document root directory
    DocumentRoot /var/www/example.com/public_html

    # Prevent serving default pages by restricting DirectoryIndex
    DirectoryIndex disabled
    <Directory /var/www/example.com/public_html>
        # Ensure proper permissions and security
        Options -Indexes
        AllowOverride All
        Require all granted
    </Directory>

    # Log files for debugging and monitoring
    ErrorLog ${APACHE_LOG_DIR}/example.com-error.log
    CustomLog ${APACHE_LOG_DIR}/example.com-access.log combined
</VirtualHost>
```

---

### Nginx Configuration
```nginx
# Nginx Server Block Configuration
# This configuration prevents serving default pages by denying directory listing.

server {
    listen 80;
    server_name example.com www.example.com;

    # Define the root directory for the website
    root /var/www/example.com/public_html;

    # Specify that no default index file is to be served
    index none;

    # Prevent directory listing
    autoindex off;

    # Error page configuration
    error_page 403 /403.html;

    # Enable custom error handling
    location = /403.html {
        root /var/www/example.com/public_html;
    }

    # Default server behavior
    location / {
        try_files $uri $uri/ =404;
    }

    # Access and error log files for monitoring
    access_log /var/log/nginx/example.com-access.log;
    error_log /var/log/nginx/example.com-error.log;
}
```

--- 

Ensure to reload the server configurations after updating these files:
- For Apache: `sudo systemctl reload apache2`
- For Nginx: `sudo systemctl reload nginx`
