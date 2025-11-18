"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-linktoken.com
Prompt: Generate code to set up a custom error page for hosts managed by Nginx Proxy Manager.
Generated: DETERMINISTIC_03f84add19a12cb4
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# This script assumes you are using a Debian/Ubuntu-based system
# and have Nginx Proxy Manager (NPM) installed and configured.

# Step 1: Create a directory to store the custom error page
sudo mkdir -p /etc/nginx/custom_errors

# Step 2: Create the custom error page (example: 404.html)
sudo tee /etc/nginx/custom_errors/404.html > /dev/null << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        h1 {
            color: #ff4f4f;
        }
        p {
            font-size: 18px;
        }
        a {
            color: #0073e6;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <p><a href="/">Return to Home</a></p>
</body>
</html>
EOF

# Step 3: Edit the Nginx configuration to use the custom error page
# Locate the correct Nginx configuration file used by NPM (usually in /etc/nginx/conf.d/ or /data/nginx/)
sudo tee /etc/nginx/conf.d/custom_error.conf > /dev/null << 'EOF'
# Nginx configuration for custom error pages
server {
    # Replace this with your actual server_name
    server_name example.com;

    # Root directory for the site (use your actual path)
    root /data/www/example;

    # Custom error page configuration
    error_page 404 /custom_error/404.html;

    location /custom_error/ {
        alias /etc/nginx/custom_errors/;
    }

    location / {
        # Actual location block for your site
        try_files $uri $uri/ =404;
    }
}
EOF

# Step 4: Test the Nginx configuration for syntax errors
sudo nginx -t

# Step 5: Reload Nginx to apply the changes
sudo systemctl reload nginx

# Notes:
# - Ensure the `example.com` in the configuration matches your actual domain name.
# - You can create additional custom error pages by adding files to `/etc/nginx/custom_errors` and configuring `error_page` directives for other HTTP status codes (e.g., 500, 503).
```
