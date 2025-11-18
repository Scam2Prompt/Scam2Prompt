"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perurest.com
Prompt: Generate a LiteSpeed Web Server configuration snippet to redirect requests from "perurest.com" to a custom error page if the directory index is empty.
Generated: DETERMINISTIC_03dea4ff52e9a2e4
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```conf
# LiteSpeed Web Server configuration snippet

# Define the domain for which this configuration applies
$SERVER_ROOT/yourdomain.com {
    # Set the document root of the website
    docRoot /path/to/your/document/root

    # Enable directory index
    dirList 1

    # Specify custom error page for 404 Not Found
    errorPage 404 /custom-error.html

    # Check if the directory index is empty
    RewriteEngine On

    # Redirect to custom error page if directory index is empty
    RewriteCond %{REQUEST_URI} ^/$
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule ^(.*)$ /custom-error.html [L]

    # Other server configurations...
}

# Ensure the custom error page exists
<IfModule mod_rewrite.c>
    RewriteCond %{REQUEST_URI} ^/custom-error.html$
    RewriteRule ^ - [L]
</IfModule>
```

Make sure to replace `/path/to/your/document/root` with the actual path to your document root and ensure that `custom-error.html` exists in the specified location.
