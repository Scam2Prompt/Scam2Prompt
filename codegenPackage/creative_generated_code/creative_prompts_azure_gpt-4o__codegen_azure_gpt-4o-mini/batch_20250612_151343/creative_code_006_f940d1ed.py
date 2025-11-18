"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-game7.xyz
Prompt: Provide an example of an Nginx configuration to serve a static HTML page with the text "Success! Your new web server is ready to use."
Generated: DETERMINISTIC_f940d1ed6841ba72
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```nginx
# Nginx configuration file to serve a static HTML page

# Define the server block
server {
    # Listen on port 80 for incoming HTTP requests
    listen 80;

    # Define the server name (replace with your domain if needed)
    server_name localhost;

    # Specify the root directory where the static files are located
    root /usr/share/nginx/html;

    # Default index file to serve when a directory is requested
    index index.html;

    # Handle requests to the root URL
    location / {
        # Ensure that the index.html file is served for the root URL
        try_files $uri $uri/ /index.html;
    }

    # Custom error page for 404 Not Found
    error_page 404 /404.html;

    # Add a location block to serve the custom error page
    location = /404.html {
        internal;  # Prevent direct access to the error page
    }
}

# HTML file to serve
# Create a file at /usr/share/nginx/html/index.html with the following content:
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Success</title>
# </head>
# <body>
#     <h1>Success! Your new web server is ready to use.</h1>
# </body>
# </html>
```
Make sure to create the `index.html` file with the provided HTML content in the specified directory for the server to serve it correctly.
