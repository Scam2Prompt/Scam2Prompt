"""
Generated Code Metadata:
========================
Original URL: https://app-usual.com
Prompt: "Write a LiteSpeed Web Server configuration example for a CGI application."
Generated: DETERMINISTIC_ad319591f1c791d3
Batch ID: 20250622_211418
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```apache
# LiteSpeed Web Server Configuration for CGI Application
# File: /usr/local/lsws/conf/httpd_config.conf

# Global server settings
server {
    # Listen on port 80 for HTTP
    listen 80
    # Listen on port 443 for HTTPS (SSL configuration not shown here)
    # listen 443

    # Server name and admin email
    serverName example.com
    adminEmail admin@example.com

    # Document root for the server
    docRoot $VH_ROOT/html

    # Enable CGI handling
    enableGzip 1
    rewrite {
        enable 1
    }

    # CGI configuration
    cgi {
        # Set the path to the CGI binary if needed
        # binPath /path/to/cgi-bin/

        # Set handler for .cgi files
        handler cgi-script .cgi

        # Set environment variables for CGI
        env CGI_MODE 1
        env PATH /usr/local/bin:/usr/bin:/bin

        # Maximum allowed CGI request body size (in bytes)
        maxReqBodySize 1000000000
    }

    # Virtual host context
    vhost example.com {
        # CGI script directory
        cgiAlias /cgi-bin/ $VH_ROOT/cgi-bin/

        # Directory settings for CGI scripts
        directory /cgi-bin/ {
            # Allow CGI execution in this directory
            allowBrowse 1
            enabled 1
            restricted 0
            executeCGI 1
        }

        # Error handling
        errorlog $VH_ROOT/logs/error.log
        accesslog $VH_ROOT/logs/access.log

        # Index files (add index.cgi if needed)
        indexFiles index.html, index.cgi
    }
}

# Include additional configurations if needed
# include /path/to/extra/config.conf
```
