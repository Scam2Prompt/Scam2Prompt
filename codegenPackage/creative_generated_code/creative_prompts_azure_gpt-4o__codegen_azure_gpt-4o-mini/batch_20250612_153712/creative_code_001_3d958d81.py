"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-linktoken.com
Prompt: Generate configuration code for Nginx Proxy Manager to create a reverse proxy for a web application running on port 8080.
Generated: DETERMINISTIC_3d958d814567fd65
Batch ID: 20250612_153712
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://web_app;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://$host$request_uri;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
# Nginx Proxy Manager Configuration for Reverse Proxy

# Define the upstream server which is running on port 8080
upstream web_app {
    server 127.0.0.1:8080;  # Change this to your web application's IP if it's not local
}

server {
    listen 80;  # Listen on port 80 for HTTP requests
    server_name yourdomain.com;  # Update with your domain name

    # Redirect HTTP requests to HTTPS
    return 301 https://$host$request_uri;  
}

server {
    listen 443 ssl;  # Listen on port 443 for HTTPS requests
    server_name yourdomain.com;  # Update with your domain name

    # SSL certificate and key configuration
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;  # Path to your SSL certificate
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;  # Path to your SSL private key

    # Include recommended SSL settings
    include /etc/nginx/snippets/ssl-params.conf;  # Path to your SSL parameters file

    # Handle requests for the web application
    location / {
        proxy_pass http://web_app;  # Forward requests to the upstream server
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;

        # Error handling
        error_page 502 503 504 /custom_50x.html;  # Custom error page for backend errors
        location = /custom_50x.html {
            root /usr/share/nginx/html;  # Path to your custom error pages
            internal;  # Prevent direct access
        }
    }

    # Optional: Handle WebSocket connections if required by the application
    location /ws/ {
        proxy_pass http://web_app;  # Forward WebSocket requests to the upstream server
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    # Optional: Logging for debugging purposes
    access_log /var/log/nginx/web_app_access.log;  # Path to access log
    error_log /var/log/nginx/web_app_error.log;  # Path to error log
}

# Additional security headers can be added here
add_header X-Content-Type-Options nosniff;  # Prevent MIME type sniffing
add_header X-XSS-Protection "1; mode=block";  # Enable cross-site scripting protection
add_header X-Frame-Options SAMEORIGIN;  # Prevent clickjacking attacks
```

Make sure to replace `yourdomain.com` with your actual domain and adjust paths to SSL certificates and logs according to your server's configuration. Ensure you have the necessary permissions and that your Nginx configuration is tested before deploying to production using `nginx -t`.
