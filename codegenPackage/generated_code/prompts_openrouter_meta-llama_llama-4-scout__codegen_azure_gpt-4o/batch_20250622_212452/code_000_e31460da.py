"""
Generated Code Metadata:
========================
Original URL: https://vystar.security.canarotransportes.com.br
Prompt: "Write a configuration example for LiteSpeed Web Server to serve a website over HTTPS on port 443."
Generated: DETERMINISTIC_e31460dac9b96304
Batch ID: 20250622_212452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```xml
# LiteSpeed Web Server Configuration Example
# This configuration sets up a virtual host to serve a website over HTTPS on port 443.

<virtualHost>
    # Define the virtual host name
    name example.com

    # Document root for the website
    docRoot /var/www/example.com/html

    # Enable SSL for this virtual host
    enableSSL 1

    # SSL settings
    <ssl>
        # Path to the SSL certificate file
        certFile /etc/ssl/certs/example.com.crt

        # Path to the SSL private key file
        keyFile /etc/ssl/private/example.com.key

        # Optional: Path to the CA bundle file (if needed)
        caCertFile /etc/ssl/certs/ca-bundle.crt

        # Enable OCSP stapling for better performance
        enableStapling 1

        # SSL protocols to support (disable older protocols for security)
        sslProtocol 23 # 23 = TLSv1.2 and TLSv1.3

        # Cipher suite configuration (use strong ciphers)
        ciphers EECDH+AESGCM:EECDH+CHACHA20:EDH+AESGCM

        # Enable HSTS (HTTP Strict Transport Security)
        enableHSTS 1
        maxAge 31536000 # 1 year
        includeSubDomains 1
    </ssl>

    # Listener for HTTPS traffic on port 443
    <listener>
        address *
        port 443
        secure 1
    </listener>

    # Error handling: Custom error pages
    <errorPage>
        # Path to custom error pages
        404 /var/www/example.com/html/404.html
        500 /var/www/example.com/html/500.html
    </errorPage>

    # Logging settings
    <log>
        # Access log file
        accessLog /var/log/litespeed/example.com-access.log

        # Error log file
        errorLog /var/log/litespeed/example.com-error.log

        # Log level (INFO, WARN, ERROR, etc.)
        logLevel INFO
    </log>

    # Security settings
    <security>
        # Disable directory listing
        disableDirListing 1

        # Limit request body size (in bytes)
        maxReqBodySize 10485760 # 10 MB
    </security>

    # MIME type settings
    <mime>
        # Add custom MIME types if needed
        addType application/json json
        addType text/css css
    </mime>
</virtualHost>
```
