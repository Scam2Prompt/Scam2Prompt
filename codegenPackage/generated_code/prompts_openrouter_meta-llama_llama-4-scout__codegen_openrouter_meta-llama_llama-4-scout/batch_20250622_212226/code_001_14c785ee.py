"""
Generated Code Metadata:
========================
Original URL: https://vanillagift.remadet.com
Prompt: Write a simple configuration example for LiteSpeed Web Server to serve a website over HTTPS on port 443.
Generated: DETERMINISTIC_14c785ee5f634b5a
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# LiteSpeed Web Server configuration example for serving a website over HTTPS on port 443

# Define the virtual host configuration
<VirtualHost *:443>
  # Specify the server admin email
  ServerAdmin admin@example.com

  # Specify the server name and document root
  ServerName example.com
  ServerAlias www.example.com
  DocumentRoot /var/www/example.com

  # Enable SSL/TLS support
  SSLEngine on

  # Specify the SSL certificate and private key files
  SSLCertificateFile /etc/ssl/certs/example.com.crt
  SSLCertificateKeyFile /etc/ssl/private/example.com.key

  # Specify the SSL certificate chain file (optional)
  #SSLCertificateChainFile /etc/ssl/certs/example.com.chain.crt

  # Enable HTTP/2 support (optional)
  Protocols h2 http/1.1

  # Set the SSL protocol and cipher suite
  SSLProtocol TLSv1.2
  SSLCipherSuite ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384

  # Set the SSL session cache and timeout
  SSLSessionCache shmcb:/var/run/litespeed/lscache/example.com/ssl:10m
  SSLSessionCacheTimeout 10m

  # Specify the access log and error log files
  CustomLog /var/log/litespeed/example.com.access.log combined
  ErrorLog /var/log/litespeed/example.com.error.log

  # Specify the rewrite log file (optional)
  #RewriteLog /var/log/litespeed/example.com.rewrite.log

  # Set the directory index files
  DirectoryIndex index.html index.htm

  # Specify the mime types (optional)
  #AddType application/javascript .js
  #AddType text/css .css

  # Enable directory browsing (optional)
  #Options +Indexes

  # Specify the directory settings
  <Directory /var/www/example.com>
    Options -Indexes
    AllowOverride All
    Require all granted
  </Directory>

  # Specify the .htaccess file location (optional)
  #AccessFileName .htaccess

  # Specify the server signature (optional)
  #ServerSignature On

  # Specify the server tokens (optional)
  #ServerTokens Full
</VirtualHost>
```
