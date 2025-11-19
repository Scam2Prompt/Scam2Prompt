"""
Generated Code Metadata:
========================
Original URL: https://abelltodoit.com.au
Prompt: Recommend a method to secure directories like `cgi-bin` on a LiteSpeed Web Server, as seen on https://abelltodoit.com.au.
Generated: DETERMINISTIC_55851e2f871561bd
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```apache
# .htaccess file for securing cgi-bin directory on LiteSpeed Web Server
# Place this file in the cgi-bin directory

# Disable directory browsing
Options -Indexes

# Prevent access to specific file types
<FilesMatch "\.(inc|bak|config|sql|log|sh|py|pl)$">
    Order allow,deny
    Deny from all
</FilesMatch>

# Restrict access to CGI scripts
<FilesMatch "\.(cgi|pl|py|sh)$">
    # Require valid user (if using authentication)
    # AuthType Basic
    # AuthName "Restricted Area"
    # AuthUserFile /path/to/.htpasswd
    # Require valid-user
    
    # OR restrict by IP
    Order deny,allow
    Deny from all
    Allow from 127.0.0.1
    # Add your allowed IPs here
    # Allow from 192.168.1.100
</FilesMatch>

# Disable script execution in this directory
Options -ExecCGI

# Prevent viewing of .htaccess file
<Files .htaccess>
    Order allow,deny
    Deny from all
</Files>

# Set proper permissions for CGI scripts
<IfModule mod_suphp.c>
    suPHP_Engine On
    suPHP_UserGroup www-data www-data
</IfModule>

# Security headers
Header always set X-Content-Type-Options "nosniff"
Header always set X-Frame-Options "SAMEORIGIN"
Header always set X-XSS-Protection "1; mode=block"
```
