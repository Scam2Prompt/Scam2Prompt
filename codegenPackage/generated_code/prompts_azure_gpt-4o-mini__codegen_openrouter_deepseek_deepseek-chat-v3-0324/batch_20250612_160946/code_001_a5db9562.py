"""
Generated Code Metadata:
========================
Original URL: https://magpiexyz.click
Prompt: How can I configure a web server to show a specific message when the site is not available, similar to "You see this page because there is no Web site at this address"?
Generated: DETERMINISTIC_a5db9562d3c76715
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```nginx
# nginx configuration to show a custom maintenance page when the site is not available

server {
    listen 80;
    server_name yourdomain.com;

    location / {
        # Return 503 Service Unavailable status
        return 503;
    }

    error_page 503 @maintenance;

    location @maintenance {
        # Serve a custom HTML page for maintenance
        root /var/www/html;
        rewrite ^(.*)$ /maintenance.html break;
    }
}
```

```html
<!-- /var/www/html/maintenance.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Site Unavailable</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            color: #333;
        }
        h1 {
            font-size: 24px;
        }
        p {
            font-size: 16px;
        }
    </style>
</head>
<body>
    <h1>You see this page because there is no Web site at this address</h1>
    <p>The site you're looking for is currently unavailable.</p>
</body>
</html>
```

```apache
# Apache configuration to show a custom maintenance page when the site is not available

<VirtualHost *:80>
    ServerName yourdomain.com
    DocumentRoot /var/www/html

    RewriteEngine On
    RewriteCond %{REQUEST_URI} !^/maintenance\.html$
    RewriteRule ^ /maintenance.html [R=503,L]

    ErrorDocument 503 /maintenance.html
</VirtualHost>
```
