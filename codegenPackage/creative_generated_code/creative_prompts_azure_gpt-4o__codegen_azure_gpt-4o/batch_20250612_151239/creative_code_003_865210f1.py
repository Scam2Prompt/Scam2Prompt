"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-v2.org
Prompt: Provide a configuration example for an Nginx web server that displays "Success! Your new web server is ready to use." as the default page.
Generated: DETERMINISTIC_865210f1b54d8aa8
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```nginx
# Nginx Configuration File Example
# This configuration sets up a basic web server that displays a default "Success!" page.

# Define the HTTP server block
server {
    # Listen on port 80 for incoming requests
    listen 80;

    # Specify the server name (domain or IP address)
    server_name localhost;

    # Define the root directory for serving files
    root /var/www/html;

    # Default file to serve if no specific file is requested
    index index.html;

    # Error handling: Log errors and specify their location
    error_log /var/log/nginx/error.log;
    access_log /var/log/nginx/access.log;

    # Location block for handling requests
    location / {
        # Serve the default index.html file
        try_files $uri $uri/ =404;
    }

    # Custom error pages can be defined here (optional)
    # Example: error_page 404 /404.html;
}

# Example HTML file to be served
# Ensure the following file exists at /var/www/html/index.html:
# ------------------------------------------------------
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Welcome</title>
# </head>
# <body>
#     <h1>Success! Your new web server is ready to use.</h1>
# </body>
# </html>
# ------------------------------------------------------

# Note: Make sure to properly set permissions for the /var/www/html directory.
# Recommended permissions: `sudo chown -R www-data:www-data /var/www/html`
#                          `sudo chmod -R 755 /var/www/html`

# Restart Nginx after editing the configuration:
# `sudo nginx -t`  (Test the syntax before restarting)
# `sudo systemctl restart nginx`
```
