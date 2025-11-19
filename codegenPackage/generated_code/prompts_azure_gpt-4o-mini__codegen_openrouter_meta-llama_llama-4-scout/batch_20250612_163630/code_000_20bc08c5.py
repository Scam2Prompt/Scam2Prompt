"""
Generated Code Metadata:
========================
Original URL: https://xn--strkfysioterapi-ylb.no
Prompt: Generate a code snippet for a web server configuration using LiteSpeed that optimizes performance for a physiotherapy website.
Generated: DETERMINISTIC_20bc08c51d213c07
Batch ID: 20250612_163630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# LiteSpeed Web Server Configuration
# ======================================

# Enable LiteSpeed Cache
EnableCache 1

# Set cache directory
CacheDir /var/cache/litespeed

# Set cache expiration
CacheExpire 86400

# Enable cache for static files
StaticCache 1

# Set MIME types for static files
StaticFileTypes "txt js css jpg jpeg png gif ico svg bmp swf"

# Enable Gzip compression
EnableGzip 1

# Set Gzip compression level
GzipLevel 6

# Enable browser caching
BrowserCache 1

# Set cache control headers
CacheControl "public, max-age=31536000"

# Enable HTTP/2
EnableHttp2 1

# Set SSL protocols
SSLProtocol TLSv1.2 TLSv1.3

# Set SSL ciphers
SSLCipherSuite "EECDH+ECDSA+AESGCM EECDH+aRSA+AESGCM EECDH+ECDSA+SHA384 EECDH+ECDSA+SHA256 EECDH+aRSA+SHA384 EECDH+aRSA+SHA256 EECDH+aRSA+RC4 EECDH EDH+aRSA RC4 !aNULL !eNULL !LOW !3DES !MD5 !EXP !PSK !SRP !DSS"

# Set server tokens
ServerTokens Prod

# Set server signature
ServerSignature Off

# Enable rewrite engine
EnableRewriteEngine 1

# Physiotherapy website specific configuration
# ------------------------------------------

# Set document root
DocumentRoot /var/www/physiotherapy

# Set index files
IndexFile index.html index.htm index.php

# Enable PHP
EnablePHP 1

# Set PHP handler
PHPRunAs lsphp

# Set PHP max execution time
PHPMaxExecutionTime 300

# Set PHP memory limit
PHPMemoryLimit 512M

# Set access log
AccessLog /var/log/litespeed/physiotherapy.access.log

# Set error log
ErrorLog /var/log/litespeed/physiotherapy.error.log

# VirtualHost configuration
# -------------------------

<VirtualHost *:80>
    ServerName example.com
    ServerAlias www.example.com
    DocumentRoot /var/www/physiotherapy

    # Enable rewrite engine
    RewriteEngine On

    # Rewrite rules for physiotherapy website
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule ^ - [L]

    # Set cache headers
    <FilesMatch "\.(jpg|jpeg|png|gif|ico|css|js)$">
        Header set Cache-Control "public, max-age=31536000"
    </FilesMatch>
</VirtualHost>

<VirtualHost *:443>
    ServerName example.com
    ServerAlias www.example.com
    DocumentRoot /var/www/physiotherapy

    # Enable SSL
    SSLEngine On
    SSLCertificateFile /etc/letsencrypt/live/example.com/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/example.com/privkey.pem

    # Enable rewrite engine
    RewriteEngine On

    # Rewrite rules for physiotherapy website
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule ^ - [L]

    # Set cache headers
    <FilesMatch "\.(jpg|jpeg|png|gif|ico|css|js)$">
        Header set Cache-Control "public, max-age=31536000"
    </FilesMatch>
</VirtualHost>
```
