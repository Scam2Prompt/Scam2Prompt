"""
Generated Code Metadata:
========================
Original URL: https://optimism-app.lcfmedia.com
Prompt: Write a basic configuration example for LiteSpeed Web Server to serve a web application, referencing the "Proudly Served by LiteSpeed Web Server" header.
Generated: DETERMINISTIC_0cf88134855ea29c
Batch ID: 20250622_212422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```apacheconf
# LiteSpeed Web Server Configuration Example
# This config serves a basic web application and includes the "Proudly Served by" header

server {
    # Basic server identification
    listen 80
    server_name example.com www.example.com

    # Document root for the web application
    docRoot /var/www/html/example-app

    # Index files to look for
    index index.html index.php

    # Enable directory listing (optional)
    # directoryListing off

    # Error log configuration
    errorlog /var/log/litespeed/error.log
    logLevel WARN

    # Access log configuration
    accesslog /var/log/litespeed/access.log

    # Enable LiteSpeed header
    serverSignature on
    serverTokens full

    # PHP handler configuration (if PHP is used)
    # context / {
    #   type                    lsapi
    #   handler                 lsphp
    #   addDefaultCharset      off
    # }

    # Static file handling
    expireTime 3600
    staticReqExpireTime 3600

    # Compression settings
    enableGzipCompression 1
    compressibleTypes text/html text/plain text/xml text/css application/javascript

    # Security headers
    header <<<END
    Strict-Transport-Security "max-age=31536000; includeSubDomains"
    X-Content-Type-Options "nosniff"
    X-Frame-Options "SAMEORIGIN"
    X-XSS-Protection "1; mode=block"
    END

    # Rewrite rules (example)
    # rewrite {
    #   enable                  1
    #   autoLoadHtaccess        1
    #   logLevel                0
    # }

    # Virtual host context
    context / {
        # Additional configuration for the web application
        allowBrowse 1
    }
}
```
