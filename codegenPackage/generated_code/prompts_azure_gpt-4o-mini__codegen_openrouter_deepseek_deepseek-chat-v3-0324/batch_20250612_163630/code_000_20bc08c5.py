"""
Generated Code Metadata:
========================
Original URL: https://xn--strkfysioterapi-ylb.no
Prompt: Generate a code snippet for a web server configuration using LiteSpeed that optimizes performance for a physiotherapy website.
Generated: DETERMINISTIC_20bc08c51d213c07
Batch ID: 20250612_163630
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://*.googleapis.com;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://*.gstatic.com;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://*.googleapis.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://*.google-analytics.com;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://*.google-analytics.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://*.googletagmanager.com;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```apache
# LiteSpeed Web Server Configuration for Physiotherapy Website
# Optimized for performance, security, and SEO

server {
    # Basic Server Configuration
    listen 80
    listen 443 ssl http2
    serverName physiotherapy.example.com
    serverAdmin webmaster@example.com

    # SSL Configuration
    sslCertificateFile /etc/letsencrypt/live/physiotherapy.example.com/fullchain.pem
    sslCertificateKeyFile /etc/letsencrypt/live/physiotherapy.example.com/privkey.pem
    sslProtocol TLSv1.2 TLSv1.3
    sslCiphers ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384
    sslPreferServerCiphers on
    sslSessionCache shared:SSL:10m
    sslSessionTimeout 1d

    # Performance Optimizations
    enableGzip 1
    gzipCompLevel 6
    gzipTypes text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript
    brotliCompression 1
    brotliTypes text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript

    # Cache Control Headers
    expires $expires_var {
        default 1d
        css 1w
        js 1w
        ~image/ 1M
    }

    # Security Headers
    header {
        Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
        X-Frame-Options SAMEORIGIN
        X-Content-Type-Options nosniff
        Referrer-Policy strict-origin-when-cross-origin
        Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' https://*.googleapis.com https://*.googletagmanager.com; style-src 'self' 'unsafe-inline' https://*.googleapis.com; img-src 'self' data: https://*.google-analytics.com; font-src 'self' https://*.gstatic.com; connect-src 'self' https://*.google-analytics.com"
    }

    # Rewrite Rules
    rewrite {
        enable 1
        autoLoadHtaccess 1
        logLevel 0
    }

    # Static File Handling
    staticFile {
        expireTime 300
        sendCacheControl 1
        enableSendfile 1
        enableAIO 1
    }

    # PHP Handling
    extProcessor lsphp {
        type lsapi
        address uds://tmp/lshttpd/lsphp.sock
        maxConns 100
        env PHP_LSAPI_MAX_REQUESTS=5000
        env PHP_LSAPI_CHILDREN=35
        initTimeout 60
        retryTimeout 0
        persistConn 1
        respBuffer 0
        autoStart 1
        path /usr/local/lsws/lsphp81/bin/lsphp
        backlog 100
        instances 1
        priority 0
        memSoftLimit 2047M
        memHardLimit 2047M
        procSoftLimit 400
        procHardLimit 500
    }

    # Context for PHP files
    context / {
        type NULL
        location /var/www/physiotherapy/
        allowBrowse 1
        rewrite {
        }
        addDefaultCharset off
        phpIniOverride {
            max_execution_time = 30
            memory_limit = 256M
            upload_max_filesize = 32M
            post_max_size = 36M
            opcache.enable = 1
            opcache.memory_consumption = 256
            opcache.interned_strings_buffer = 16
            opcache.max_accelerated_files = 10000
            opcache.validate_timestamps = 0
            opcache.revalidate_freq = 2
        }
    }

    # Error Handling
    errorPage 404 /404.html
    errorPage 403 /403.html
    errorPage 500 /500.html

    # Logging Configuration
    accessLog {
        useServer 0
        fileName /var/log/litespeed/physiotherapy_access.log
        logLevel INFO
        rollingSize 100M
        keepDays 30
        enableStderrLog 1
    }

    errorLog {
        useServer 0
        fileName /var/log/litespeed/physiotherapy_error.log
        logLevel ERROR
        rollingSize 100M
        keepDays 30
        debugLevel 0
    }
}
```
