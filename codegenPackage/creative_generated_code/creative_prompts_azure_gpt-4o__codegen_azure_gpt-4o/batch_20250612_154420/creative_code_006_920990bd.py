"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linkbonus.net
Prompt: Explain how to use Nginx Proxy Manager to redirect HTTP traffic to HTTPS with code examples.
Generated: DETERMINISTIC_920990bd93dd4e28
Batch ID: 20250612_154420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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

Below is an example of an Nginx configuration file to redirect HTTP traffic to HTTPS using Nginx Proxy Manager:

```nginx
# HTTP server configuration
server {
    # Listen on port 80 for incoming HTTP requests
    listen 80;

    # Define the server name (domain or subdomain)
    server_name example.com www.example.com;

    # Redirect all HTTP traffic to HTTPS
    return 301 https://$host$request_uri;
}

# HTTPS server configuration
server {
    # Listen on port 443 for incoming HTTPS requests
    listen 443 ssl;

    # Define the server name (domain or subdomain)
    server_name example.com www.example.com;

    # SSL certificate and key files (replace with actual file paths)
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    # SSL settings for security (best practices)
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    # Root directory for serving static files (optional, modify as needed)
    root /var/www/html;

    # Index file to be served
    index index.html;

    # Location block for handling requests
    location / {
        try_files $uri $uri/ =404;
    }
}
```

### Key Notes in Comments:
- Replace `example.com` and `www.example.com` with your actual domain names.
- Update the paths to `ssl_certificate` and `ssl_certificate_key` with the correct file paths for your SSL certificates.
- This configuration redirects all HTTP traffic (`port 80`) to HTTPS (`port 443`) using a `301` status code, which is a permanent redirect.
- The `ssl_protocols` and `ssl_ciphers` settings follow modern security best practices.

To use this configuration:
1. Save the code above in an Nginx configuration file, for example, `/etc/nginx/sites-available/example`.
2. Create a symbolic link to this file in `/etc/nginx/sites-enabled/`.
3. Test the configuration for errors using `sudo nginx -t`.
4. Reload Nginx with `sudo systemctl reload nginx`.

This is production-ready Nginx configuration adhering to best practices!
