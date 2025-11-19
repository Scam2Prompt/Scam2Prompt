"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://destiro.com
Prompt: What are the best practices for serving static files like logo.png on an Apache server as seen on destiro.com?
Generated: DETERMINISTIC_db2b2961ab2becfe
Batch ID: 20250612_155805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```apache
# Apache Configuration for Serving Static Files

# Enable mod_headers for caching
<IfModule mod_headers.c>
    Header set Cache-Control "max-age=31536000, public"
</IfModule>

# Set the DocumentRoot to your web directory
DocumentRoot "/var/www/html"

# Define a directory block for static files
<Directory "/var/www/html/static">
    # Allow access to this directory
    Require all granted

    # Enable caching for image files
    <FilesMatch "\.(jpg|jpeg|png|gif|ico)$">
        Header set Cache-Control "max-age=31536000, public"
    </FilesMatch>

    # Optionally set expires headers for images
    ExpiresActive On
    ExpiresDefault "access plus 1 year"
</Directory>

# Error handling for missing files
ErrorDocument 404 /404.html

# Enable compression for better performance
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html text/plain text/xml text/css text/javascript application/javascript application/json
</IfModule>

# Security headers to prevent common attacks
<IfModule mod_headers.c>
    Header set X-Content-Type-Options "nosniff"
    Header set X-XSS-Protection "1; mode=block"
    Header set X-Frame-Options "DENY"
</IfModule>

# Example for serving logo.png from static directory
Alias /logo.png /var/www/html/static/logo.png

# Ensure proper permissions on static files
<Directory "/var/www/html/static">
    Options -Indexes
</Directory>

# End of Apache configuration
```
