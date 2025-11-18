"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enhancekko.com
Prompt: Provide an example of how to use OpenResty to rewrite URLs based on specific patterns.
Generated: DETERMINISTIC_a06b646b54cf7fc6
Batch ID: 20250612_154111
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://backend_server;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```nginx
# OpenResty URL Rewrite Example

# Define the server block for your application
server {
    listen 80;  # Listen on port 80
    server_name example.com;  # Replace with your domain

    # Specify the location for the requests
    location / {
        # First, try to serve files directly
        try_files $uri $uri/ =404;  
    }

    # Rewrite URLs based on specific patterns
    # Example: Redirect /old-path to /new-path
    location /old-path {
        rewrite ^/old-path(.*)$ /new-path$1 permanent;  # Permanent redirect
    }

    # Example: Redirect /products/123 to /shop/item/123
    location /products {
        rewrite ^/products/(.*)$ /shop/item/$1 last;  # Last rule, continue processing
    }

    # Example: Remove .html extension from URLs
    location / {
        rewrite ^/(.*).html$ /$1 last;  # Rewrite URLs without .html
    }

    # Handle 404 errors with a custom page
    error_page 404 /404.html;  
    location = /404.html {
        internal;  # Prevent direct access to the 404 page
    }

    # Additional configurations can go here
    # For example, proxy_pass to an upstream server
    # location /api {
    #     proxy_pass http://backend_server;  # Forward requests to a backend server
    # }

    # Logging for debugging purposes
    access_log /var/log/nginx/access.log;  # Log access requests
    error_log /var/log/nginx/error.log;  # Log error requests
}

# End of the server block
```
