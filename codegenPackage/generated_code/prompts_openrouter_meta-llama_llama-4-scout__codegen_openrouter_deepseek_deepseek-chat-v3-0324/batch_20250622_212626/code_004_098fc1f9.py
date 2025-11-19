"""
Generated Code Metadata:
========================
Original URL: https://hyperliquidfndtn.org
Prompt: "What are the implications of serving files via LiteSpeed Web Server, and how can I optimize server configuration for efficient distribution of large files like big.zip?"
Generated: DETERMINISTIC_098fc1f965e2c767
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```nginx
# LiteSpeed Web Server Configuration for Large File Distribution

# Main server configuration
server {
    listen 80;
    server_name example.com;
    root /var/www/html;

    # Enable gzip compression for text-based files
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
    gzip_min_length 1000;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_vary on;

    # Cache settings for static files
    location ~* \.(jpg|jpeg|png|gif|ico|css|js|zip)$ {
        expires 365d;
        add_header Cache-Control "public, no-transform";
        access_log off;
    }

    # Specific configuration for large files
    location /big.zip {
        # Disable gzip for already compressed files
        gzip off;

        # Optimize sendfile operations
        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;

        # Increase buffer sizes for large files
        output_buffers 4 32k;
        client_max_body_size 0;

        # Set proper MIME type
        types { }
        default_type application/zip;

        # Enable byte-range requests
        slice 1m;
        proxy_cache_valid 200 206 1h;
    }

    # LiteSpeed specific optimizations
    litespeed {
        # Enable static file acceleration
        staticAccel on;

        # Tune buffer sizes
        recvBufferSize 131072;
        sendBufferSize 131072;

        # Optimize for large files
        maxReqHeaderSize 8192;
        maxDynRespHeaderSize 8192;
        gzipCompLevel 6;
    }

    # Error handling
    error_page 404 /404.html;
    error_page 500 502 503 504 /50x.html;
}
```
