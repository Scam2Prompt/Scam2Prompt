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

```bash
# LiteSpeed Web Server Configuration Example

# Define the virtual host settings
vhost {
    # Specify the domain name and port
    listen      443 ssl
    serverName  example.com
    serverAlias www.example.com

    # Specify the document root
    documentRoot /var/www/example.com

    # SSL/TLS certificate and key files
    sslCertificate      /path/to/example.com.crt
    sslCertificateKey   /path/to/example.com.key

    # Enable directory indexing
    enableDirectoryListing  off

    # Directory indexing settings
    dirIndex  index.html index.htm

    # Specify the directory settings
    location / {
        # Enable SSL/TLS
        ssl  on

        # Set the index file
        index  index.html index.htm

        # Set the character set
        charset  utf-8

        # Enable rewrite engine
        rewrite  on

        # Set the rewrite log
        rewriteLog  /var/log/litespeed/example.com-rewrite.log
    }

    # Error handling
    errorLog  /var/log/litespeed/example.com-error.log
    errorPage  404  /404.html

    # Security settings
    secure  on
    tls  on
    http2  on

    # Set the LiteSpeed security features
    setSecurity  {
        # Enable the web application firewall (WAF)
        waf  on

        # Set the WAF rules
        wafRules  /path/to/waf/rules.conf
    }
}
```
