"""
Generated Code Metadata:
========================
Original URL: https://saniva.com.sg
Prompt: Write a basic configuration example for a LiteSpeed Web Server to serve a website securely over HTTPS (Port 443) with specific directory indexing settings.
Generated: DETERMINISTIC_d08ecf2e5e45ce3f
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```apache
# LiteSpeed Web Server Configuration Example
# Secure HTTPS (Port 443) with directory indexing settings

server {
    # Basic server identification
    listen                443 ssl http2
    serverName            example.com www.example.com

    # SSL/TLS Configuration
    ssl {
        # Certificate files
        certFile             /path/to/certificate.crt
        keyFile              /path/to/private.key
        # Intermediate certificate (if applicable)
        caPath               /path/to/ca_bundle.crt

        # Enable modern protocols and ciphers
        enableECDHE         1
        sslProtocol         TLSv1.2 TLSv1.3
        cipherSuite         EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH
    }

    # Document root and basic settings
    documentRoot          /var/www/example.com/public_html/
    accessLog             /var/log/litespeed/example.com/access.log
    errorLog              /var/log/litespeed/example.com/error.log

    # Directory indexing settings
    directory {
        # Enable directory listing
        indexFiles         index.html, index.php
        autoIndex          1
        # Customize directory listing appearance
        indexStyle         "/icons/example.css"
        # Show file sizes in directory listing
        showFileSize       1
        # Show file last modified time
        showLastMod        1
    }

    # Security headers
    header {
        # HSTS (HTTP Strict Transport Security)
        Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
        # XSS Protection
        X-XSS-Protection "1; mode=block"
        # Content Security Policy
        Content-Security-Policy "default-src 'self';"
    }

    # Error pages
    errorpage 404 /404.html
    errorpage 403 /403.html
    errorpage 500 /500.html

    # PHP handler (if needed)
    extProcessor lsphp {
        type                lsapi
        address             uds://tmp/lshttpd/lsphp.sock
        maxConns            35
        env                 PHP_LSAPI_CHILDREN=35
        initTimeout         60
        retryTimeout        0
        persistConn         1
        respBuffer          0
        autoStart           1
        path                /usr/local/lsws/lsphp73/bin/lsphp
    }

    # Context for PHP files
    context / {
        type                NULL
        location            $DOC_ROOT/
        allowBrowse         1
        extraHeaders        <<<END_extraHeaders
        Cache-Control "no-cache, must-revalidate"
        END_extraHeaders
        rewrite {
            enable          1
            inherit         1
        }
        addDefaultCharset   off
        phpIniOverride {
            max_execution_time = 30
            memory_limit = 128M
        }
    }
}
```
