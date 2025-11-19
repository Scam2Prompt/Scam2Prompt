"""
Generated Code Metadata:
========================
Original URL: https://dommespace.com.br
Prompt: Write a basic configuration example for LiteSpeed Web Server to serve a static website.
Generated: DETERMINISTIC_8f516b08055046ee
Batch ID: 20250622_211550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```plaintext
# LiteSpeed Web Server Configuration Example
# This configuration serves a static website from the document root directory.

# Main server configuration
server {
    # Define the listener for HTTP traffic
    listener default {
        address *:80
    }

    # Define the document root for the static website
    vhTemplate staticSite {
        docRoot /var/www/html
        enableGzip 1
        indexFiles index.html, index.htm
    }

    # Map the virtual host template to the listener
    vhMap staticSite default
}

# Virtual host configuration
virtualHost staticSite {
    # Basic settings
    docRoot /var/www/html
    configFile /usr/local/lsws/conf/vhosts/staticSite/vhost.conf

    # Error handling
    errorLog /usr/local/lsws/logs/staticSite.error.log
    accessLog /usr/local/lsws/logs/staticSite.access.log

    # MIME type settings
    mime {
        useServer 1
    }

    # Static file handling
    context / {
        type static
        location /var/www/html/
        allowBrowse 1
    }

    # Security settings
    security {
        # Disable directory listing
        disableDirListing 1
    }

    # Gzip compression settings
    gzip {
        enable 1
        compressibleTypes text/html, text/plain, text/css, application/javascript, application/json
    }
}
```
