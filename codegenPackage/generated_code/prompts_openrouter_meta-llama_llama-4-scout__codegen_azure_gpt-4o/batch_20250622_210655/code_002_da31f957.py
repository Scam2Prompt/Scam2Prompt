"""
Generated Code Metadata:
========================
Original URL: https://www.cenvirmarketingdigital.com
Prompt: "Generate a .htaccess file configuration for securing a WordPress site on LiteSpeed Web Server."
Generated: DETERMINISTIC_da31f957cf7ba61d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```apache
# BEGIN WordPress Security Configuration for LiteSpeed Web Server

# Protect .htaccess file itself
<Files .htaccess>
    Order Allow,Deny
    Deny from all
</Files>

# Disable directory browsing
Options -Indexes

# Protect wp-config.php file
<Files wp-config.php>
    Order Allow,Deny
    Deny from all
</Files>

# Protect readme.html and license.txt files
<FilesMatch "readme\.html|license\.txt">
    Order Allow,Deny
    Deny from all
</FilesMatch>

# Block access to sensitive files
<FilesMatch "\.(log|sh|sql|bak|env|ini|conf|json|lock|dist)$">
    Order Allow,Deny
    Deny from all
</FilesMatch>

# Disable XML-RPC to prevent brute force attacks
<Files xmlrpc.php>
    Order Allow,Deny
    Deny from all
</Files>

# Restrict access to wp-includes directory
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteBase /
    RewriteRule ^wp-includes/[^/]+\.php$ - [F,L]
    RewriteRule ^wp-includes/js/tinymce/langs/.+\.php$ - [F,L]
    RewriteRule ^wp-includes/theme-compat/ - [F,L]
</IfModule>

# Limit file upload size
<IfModule mod_php.c>
    php_value upload_max_filesize 10M
    php_value post_max_size 10M
</IfModule>

# Enable browser caching for static assets
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType image/jpg "access plus 1 year"
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/gif "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType text/javascript "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
    ExpiresByType application/x-javascript "access plus 1 month"
    ExpiresByType image/x-icon "access plus 1 year"
    ExpiresDefault "access plus 1 month"
</IfModule>

# Prevent hotlinking of images
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{HTTP_REFERER} !^$
    RewriteCond %{HTTP_REFERER} !^https://(www\.)?yourdomain\.com/ [NC]
    RewriteRule \.(jpg|jpeg|png|gif)$ - [F]
</IfModule>

# Block suspicious query strings
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{QUERY_STRING} (\.\.\/|\.\./|%2e%2e%2f|%2e%2e%2f) [NC,OR]
    RewriteCond %{QUERY_STRING} (base64_encode|eval|union|select|insert|drop|md5|exec|concat) [NC]
    RewriteRule .* - [F]
</IfModule>

# Protect against clickjacking
<IfModule mod_headers.c>
    Header always append X-Frame-Options SAMEORIGIN
</IfModule>

# Enable Content Security Policy (CSP) to prevent XSS attacks
<IfModule mod_headers.c>
    Header set Content-Security-Policy "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self';"
</IfModule>

# END WordPress Security Configuration for LiteSpeed Web Server
```
