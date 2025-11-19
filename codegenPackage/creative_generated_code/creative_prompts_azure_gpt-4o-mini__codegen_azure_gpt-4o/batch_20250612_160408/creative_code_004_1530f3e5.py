"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meteora.expcofmini.com
Prompt: Create a sample configuration file for a web application running on LiteSpeed.
Generated: DETERMINISTIC_1530f3e5b44588d4
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```conf
# LiteSpeed Web Server Configuration File
# This is a sample configuration file for a web application running on LiteSpeed.
# Ensure you review and customize this file to meet your application's specific needs.

# General Settings
serverName                     my-web-app
enableCoreDump                 0                # Disable core dumps for better security
autoRestart                    1                # Automatically restart server on crash
enableGzip                     1                # Enable Gzip compression for better performance
gzipStatic                     1                # Serve pre-compressed static files

# Listeners
listener HTTP {
    address                    *                # Listen on all IP addresses
    port                       80               # HTTP port
    secure                     0                # Non-secure connection
}

listener HTTPS {
    address                    *                # Listen on all IP addresses
    port                       443              # HTTPS port
    secure                     1                # Secure connection
    keyFile                    /path/to/ssl/key.pem    # Path to SSL Key file
    certFile                   /path/to/ssl/cert.pem   # Path to SSL Certificate file
}

# Virtual Host Configuration
virtualHost my-app {
    vhRoot                     /var/www/my-app  # Root directory of your application
    configFile                 /path/to/vhost/config/my-app.conf  # Path to virtual host config file
    allowSymbolLink            1                # Allow symbolic links for flexibility
    enableGzip                 1                # Enable Gzip compression for this virtual host
    rewriteEnable              1                # Enable URL rewriting
    maxConnections             1000             # Max simultaneous connections for this host
}

# Logging
errorLog /var/log/litespeed/error.log {
    logLevel                   WARN             # Log level (DEBUG, INFO, WARN, ERROR)
    rollingSize                10M              # Max size of each log file before rolling
    keepDays                   10               # Retain logs for 10 days
}

accessLog /var/log/litespeed/access.log {
    rollingSize                10M              # Max size of each access log file
    keepDays                   7                # Retain logs for 7 days
    logHeaders                 1                # Log request headers
}

# Security Settings
secRuleEngine                ON                 # Enable ModSecurity engine
secAuditLog                  /var/log/litespeed/modsec_audit.log  # Path for audit logs
secRequestBodyAccess         ON                 # Enable inspection of request body
secResponseBodyAccess        ON                 # Enable inspection of response body
secDataDir                   /tmp               # Directory for temporary files

# Static Content Settings
static {
    compressibleTypes         text/html text/plain text/css application/javascript  # Compress these content types
    cacheControl              max-age=3600      # Set cache control header for static files
}

# PHP Settings
extProcessor php {
    type                      lsphp             # Use LiteSpeed PHP processor
    address                   uds://tmp/lshttpd/lsphp.sock  # Unix domain socket for PHP communication
    maxConns                  200               # Maximum connections to the PHP processor
    initTimeout               60                # Timeout for initializing PHP processor
}

# Error Pages
errorPage 404 /custom_404.html                # Custom 404 error page
errorPage 500 /custom_500.html                # Custom 500 error page

# Index File Defaults
indexFiles index.php index.html index.htm     # Default index files to look for

# End of configuration
```
