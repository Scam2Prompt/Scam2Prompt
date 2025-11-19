"""
Generated Code Metadata:
========================
Original URL: https://vanillagift.remadet.com
Prompt: Generate a configuration file for LiteSpeed Web Server to enable HTTPS and redirect all HTTP traffic to HTTPS on port 443.
Generated: DETERMINISTIC_c681a7ae40d5cc01
Batch ID: 20250612_154827
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://%{HTTP_HOST}%{REQUEST_URI": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```apacheconf
# LiteSpeed Web Server Configuration
# Enables HTTPS and redirects all HTTP traffic to HTTPS on port 443

# Listen on port 80 for HTTP
Listen 80
<VirtualHost *:80>
    ServerName example.com
    ServerAlias www.example.com
    
    # Redirect all HTTP traffic to HTTPS
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI} [R=301,L]
</VirtualHost>

# Listen on port 443 for HTTPS
Listen 443
<VirtualHost *:443>
    ServerName example.com
    ServerAlias www.example.com
    
    # SSL Configuration
    SSLEngine on
    SSLProtocol all -SSLv2 -SSLv3
    SSLCipherSuite EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH
    SSLHonorCipherOrder on
    
    # SSL Certificate Files
    SSLCertificateFile /path/to/your/certificate.crt
    SSLCertificateKeyFile /path/to/your/private.key
    SSLCertificateChainFile /path/to/your/ca_bundle.crt
    
    # Enable HTTP/2
    Protocols h2 http/1.1
    
    # Security Headers
    Header always set Strict-Transport-Security "max-age=63072000; includeSubDomains; preload"
    Header always set X-Frame-Options DENY
    Header always set X-Content-Type-Options nosniff
    
    # Document Root
    DocumentRoot /var/www/html
    
    <Directory /var/www/html>
        Options -Indexes +FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
    
    # Logging
    ErrorLog /var/log/litespeed/error.log
    CustomLog /var/log/litespeed/access.log combined
</VirtualHost>

# Enable LiteSpeed cache if needed
<IfModule Litespeed>
    CacheEnable public /
    CacheLookup public on
</IfModule>
```
