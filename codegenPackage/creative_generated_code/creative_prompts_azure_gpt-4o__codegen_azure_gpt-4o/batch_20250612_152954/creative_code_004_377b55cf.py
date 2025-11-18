"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-mining.com
Prompt: Explain how to use LiteSpeed Web Server to host a static website and enable directory browsing, referencing the structure seen at phantom-mining.com.
Generated: DETERMINISTIC_377b55cfdb78b50d
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

To set up a static website with LiteSpeed Web Server and enable directory browsing, you typically configure the LiteSpeed Web Server using its web admin interface or by directly modifying the configuration files. Below is a sample configuration file snippet for LiteSpeed Web Server that achieves the requested functionality.

```xml
# Configuration for LiteSpeed Web Server
# This example demonstrates hosting a static website and enabling directory browsing.

<virtualHost>
    # Specify the domain name for the virtual host
    name             phantom-mining.com
    ip               ANY
    port             80

    # Set the root directory where the static files are located
    documentRoot     /var/www/phantom-mining

    # Enable directory browsing
    # This allows users to see a list of files and directories when no index file is present
    enableAutoIndex  1

    # Define default index files (e.g., index.html)
    indexFiles       index.html

    # Error page configuration
    # Redirect to custom pages for common HTTP error codes
    errorPage        404 /errors/404.html
    errorPage        403 /errors/403.html

    # Logging
    accessLog        /var/log/litespeed/phantom-mining-access.log
    errorLog         /var/log/litespeed/phantom-mining-error.log
    logLevel         DEBUG

    # MIME type definition for serving static files
    <mime>
        map         text/html              html
        map         text/plain             txt
        map         image/jpeg             jpg jpeg
        map         image/png              png
        map         application/javascript js
        map         text/css               css
    </mime>

    # Cache settings for better performance with static files
    <cache>
        enableCache 1
        staticCacheControl public, max-age=3600
    </cache>
</virtualHost>

# Global server settings
<server>
    # Enable SSL if desired (update paths to certificate and key files)
    <ssl>
        keyFile      /etc/litespeed/ssl/phantom-mining.key
        certFile     /etc/litespeed/ssl/phantom-mining.crt
        enable       1
    </ssl>

    # Error logging level (adjust as needed for production)
    logLevel        NOTICE
</server>
```

### Notes:
- The `documentRoot` is the path to your static website files (`/var/www/phantom-mining` in this example). Update it to match the location of your web files.
- Directory browsing is enabled using `enableAutoIndex 1`.
- SSL is optional. If you want to enable HTTPS, you need to provide the paths to your SSL certificate and key files.
- Logging paths should be updated to match your server's preferred locations or naming conventions.
- Place this configuration in the LiteSpeed Web Admin console or an appropriate configuration file, following LiteSpeed's documentation.
