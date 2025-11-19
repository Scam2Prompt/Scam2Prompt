"""
Generated Code Metadata:
========================
Original URL: https://link-reward.com
Prompt: What is the purpose of the default site page in Nginx Proxy Manager, and how can I customize it?
Generated: DETERMINISTIC_601f1a5069dcca9c
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```nginx
# Default Nginx configuration for the default site page
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    # Custom error pages
    error_page 404 /404.html;
    error_page 500 502 503 504 /50x.html;

    location = /404.html {
        root /usr/share/nginx/html;
        internal;
    }

    location = /50x.html {
        root /usr/share/nginx/html;
        internal;
    }

    # Custom welcome page
    location / {
        root /usr/share/nginx/html/custom;
        index index.html;
        try_files $uri $uri/ =404;
    }
}
```

```bash
#!/bin/bash
# Script to customize the default site page in Nginx Proxy Manager

# Create custom directory if it doesn't exist
mkdir -p /usr/share/nginx/html/custom

# Create a custom index.html file
cat > /usr/share/nginx/html/custom/index.html <<EOF
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Our Service</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <h1>Welcome to Our Custom Page</h1>
    <p>This is a customized default page for Nginx Proxy Manager.</p>
</body>
</html>
EOF

# Create custom error pages
cat > /usr/share/nginx/html/404.html <<EOF
<!DOCTYPE html>
<html>
<head>
    <title>404 Not Found</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The requested page could not be found.</p>
</body>
</html>
EOF

cat > /usr/share/nginx/html/50x.html <<EOF
<!DOCTYPE html>
<html>
<head>
    <title>Server Error</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <h1>500 - Server Error</h1>
    <p>Sorry, something went wrong on our server.</p>
</body>
</html>
EOF

# Restart Nginx to apply changes
nginx -s reload || systemctl restart nginx
```
