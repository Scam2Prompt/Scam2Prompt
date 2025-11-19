"""
Generated Code Metadata:
========================
Original URL: https://thekygrand.com
Prompt: Provide an example of how to set up a LiteSpeed web server to serve static files from a specific path.
Generated: DETERMINISTIC_8aac095c2a9070e4
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready configuration for LiteSpeed to serve static files from a specific directory, using an `.htaccess` file:

```apache
# LiteSpeed Configuration for Serving Static Files

# Turn off directory listing
Options -Indexes

# Enable static file serving with proper caching
<IfModule LiteSpeed>
  # Disable LiteSpeed cache for dynamic content (only needed if mixing static/dynamic)
  CacheDisable public /

  # Cache static files for 1 year (production recommended)
  <FilesMatch "\.(css|js|jpg|jpeg|png|gif|svg|woff|woff2|ico|pdf|txt)$">
    Header set Cache-Control "public, max-age=31536000, immutable"
  </FilesMatch>
</IfModule>

# Set proper MIME types for static files
<IfModule mod_mime.c>
  AddType text/css .css
  AddType application/javascript .js
  AddType image/jpeg .jpg .jpeg
  AddType image/png .png
  AddType image/svg+xml .svg
  AddType image/x-icon .ico
  AddType application/font-woff .woff
  AddType application/font-woff2 .woff2
  AddType application/pdf .pdf
  AddType text/plain .txt
</IfModule>

# Gzip compression for static files
<IfModule mod_deflate.c>
  <IfModule mod_filter.c>
    AddOutputFilterByType DEFLATE text/html text/plain text/xml
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/json
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE application/rss+xml
    AddOutputFilterByType DEFLATE image/svg+xml
  </IfModule>
</IfModule>

# Serve pre-compressed files if available
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteCond %{HTTP:Accept-Encoding} gzip
  RewriteCond %{REQUEST_FILENAME}\.gz -s
  RewriteRule ^(.*)$ $1\.gz [QSA]
</IfModule>

# Security headers for static content
<IfModule mod_headers.c>
  Header always set X-Content-Type-Options "nosniff"
  Header always set X-Frame-Options "SAMEORIGIN"
  Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains" env=HTTPS
</IfModule>

# Error documents (customize paths as needed)
ErrorDocument 400 /error/400.html
ErrorDocument 403 /error/403.html
ErrorDocument 404 /error/404.html
ErrorDocument 500 /error/500.html
```
