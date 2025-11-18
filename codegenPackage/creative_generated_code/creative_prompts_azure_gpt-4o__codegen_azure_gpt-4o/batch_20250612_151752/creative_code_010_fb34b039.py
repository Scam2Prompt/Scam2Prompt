"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prohoster.biz
Prompt: Create a configuration file for OpenCart hosting on ProHoster, ensuring compatibility with their FastCGI and CloudLinux optimizations.
Generated: DETERMINISTIC_fb34b0394473886c
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```nginx
# OpenCart Configuration for Hosting on ProHoster with FastCGI and CloudLinux Optimizations

# Ensure the configuration is placed in the hosting directory or added to the server block.

server {
    # Listen on port 80 for HTTP traffic
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    # Root directory where OpenCart is installed
    root /path/to/your/opencart;

    # Define index files
    index index.php index.html index.htm;

    # FastCGI caching settings for CloudLinux optimizations
    fastcgi_cache_path /var/cache/nginx/fastcgi_cache levels=1:2 keys_zone=FASTCGI_CACHE:10m inactive=60m;
    fastcgi_cache_key "$scheme$request_method$host$request_uri";
    fastcgi_cache_use_stale error timeout invalid_header updating;
    fastcgi_cache_valid 200 302 10m;
    fastcgi_cache_valid 404 1m;

    # Error handling
    error_page 404 /index.php?route=error/not_found;

    # Location block for static files
    location / {
        # Try to serve file first, fallback to index.php
        try_files $uri $uri/ /index.php?$query_string;
    }

    # PHP file handling
    location ~ \.php$ {
        # Include FastCGI parameters
        include fastcgi_params;

        # Pass requests to FastCGI server
        fastcgi_pass 127.0.0.1:9000; # Ensure this matches your PHP FastCGI setup
        fastcgi_index index.php;

        # Set root folder
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;

        # Enable FastCGI cache
        fastcgi_cache FASTCGI_CACHE;
        fastcgi_cache_bypass $http_cache_control;

        # Error logging
        fastcgi_intercept_errors on;

        # Use CloudLinux limits for processing
        fastcgi_read_timeout 300;
        fastcgi_connect_timeout 300;
        fastcgi_send_timeout 300;
    }

    # Deny access to sensitive files
    location ~ /\.ht {
        deny all;
    }
    
    # Deny access to "system" directory directly
    location ~ ^/system/ {
        deny all;
    }

    # Enable gzip compression for faster delivery
    gzip on;
    gzip_types text/css text/javascript application/javascript text/xml application/xml application/json image/svg+xml;
    gzip_proxied any;
    gzip_comp_level 5;
    gzip_buffers 16 8k;
    gzip_min_length 256;

    # Log files for monitoring
    access_log /var/log/nginx/opencart_access.log;
    error_log /var/log/nginx/opencart_error.log;
}
```
