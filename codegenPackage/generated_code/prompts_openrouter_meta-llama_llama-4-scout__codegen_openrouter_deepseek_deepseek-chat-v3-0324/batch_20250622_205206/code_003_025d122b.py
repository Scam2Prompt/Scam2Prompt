"""
Generated Code Metadata:
========================
Original URL: https://abelltodoit.com.au
Prompt: "How would you configure a LiteSpeed Web Server to serve a website with multiple subdirectories and file types?"
Generated: DETERMINISTIC_025d122b2016c293
Batch ID: 20250622_205206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```apacheconf
# LiteSpeed Web Server Configuration Example
# For serving a website with multiple subdirectories and file types

server {
    # Basic server settings
    listen 80
    serverName example.com
    serverAdmin webmaster@example.com
    documentRoot /var/www/html

    # Enable directory indexing for specific paths
    directoryIndex index.html index.php

    # Logging configuration
    errorLog /var/log/litespeed/error.log
    accessLog /var/log/litespeed/access.log {
        logReferer 1
        logUserAgent 1
    }

    # Compression settings
    enableGzip 1
    gzipCompLevel 6
    gzipStatic 1
    gzipTypes text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript

    # Expires headers for caching
    expires {
        image/* A604800
        text/css A604800
        application/javascript A604800
        font/* A2419200
    }

    # Rewrite rules for clean URLs
    rewrite {
        enable 1
        autoLoadHtaccess 1
    }

    # PHP handler configuration
    extProcessor lsphp {
        type lsapi
        address uds://tmp/lshttpd/lsphp.sock
        maxConns 10
        env PHP_LSAPI_CHILDREN=10
        initTimeout 60
        retryTimeout 0
        persistConn 1
        pcKeepAliveTimeout 60
        respBuffer 0
        autoStart 1
    }

    # Virtual host context for PHP files
    context / {
        type NULL
        handler lsphp
    }

    # Static file handling
    context /static/ {
        location /var/www/html/static/
        allowBrowse 1
        extraHeaders <<<END_extraHeaders
            Access-Control-Allow-Origin: *
        END_extraHeaders
    }

    # Media file handling
    context /media/ {
        location /var/www/html/media/
        allowBrowse 1
        expires 1d
    }

    # Security headers
    header {
        Strict-Transport-Security "max-age=31536000; includeSubDomains"
        X-Content-Type-Options nosniff
        X-Frame-Options SAMEORIGIN
        X-XSS-Protection "1; mode=block"
        Content-Security-Policy "default-src 'self'"
    }

    # Error pages
    errorPage 400 /error/400.html
    errorPage 403 /error/403.html
    errorPage 404 /error/404.html
    errorPage 500 /error/500.html

    # Rate limiting
    throttling {
        staticReqPerSec 200
        dynReqPerSec 50
        outBandwidth 100M
        inBandwidth 50M
    }
}
```
