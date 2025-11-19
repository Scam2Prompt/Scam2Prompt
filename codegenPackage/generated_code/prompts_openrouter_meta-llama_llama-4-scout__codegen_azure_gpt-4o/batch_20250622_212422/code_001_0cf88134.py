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

```plaintext
# LiteSpeed Web Server Configuration Example
# This configuration serves a basic web application and includes a custom header.

# Virtual Host Configuration
virtualhost {
    # Set the virtual host name
    vhName              example.com

    # Document root for the web application
    docRoot             /var/www/example.com

    # Enable access logging
    accessLog           /var/log/litespeed/example.com.access.log

    # Enable error logging
    errorLog            /var/log/litespeed/example.com.error.log

    # Set the log level (INFO, WARN, ERROR, DEBUG)
    logLevel            INFO

    # Custom header to indicate LiteSpeed server
    header {
        add             "X-Powered-By: Proudly Served by LiteSpeed Web Server"
    }

    # Index files to look for when serving a directory
    indexFiles          index.html, index.php

    # MIME type settings
    mime {
        useDefault      true
    }

    # PHP settings (if using PHP)
    scriptHandler {
        add             "application/x-httpd-php" php
    }

    # Error page settings
    errorPage           404 /404.html
    errorPage           500 /500.html

    # Security settings
    security {
        # Disable directory listing
        disableDirListing 1

        # Limit request body size (in bytes)
        requestBodyLimit  10485760
    }

    # Static file cache settings
    cache {
        enable          1
        maxAge          3600
    }

    # SSL settings (if using HTTPS)
    ssl {
        enable          1
        certFile        /etc/ssl/certs/example.com.crt
        keyFile         /etc/ssl/private/example.com.key
    }
}

# Listener Configuration
listener {
    # Bind to port 80 for HTTP
    address             *:80
    secure              0
    vhDomainMap         example.com example.com

    # Bind to port 443 for HTTPS
    address             *:443
    secure              1
    vhDomainMap         example.com example.com
}

# Global Settings
server {
    # Set the server name
    serverName          LiteSpeedServer

    # Enable gzip compression
    gzipCompress        1

    # Set the maximum number of concurrent connections
    maxConnections      1000

    # Error log settings
    errorLog            /var/log/litespeed/error.log
    logLevel            WARN
}
```
