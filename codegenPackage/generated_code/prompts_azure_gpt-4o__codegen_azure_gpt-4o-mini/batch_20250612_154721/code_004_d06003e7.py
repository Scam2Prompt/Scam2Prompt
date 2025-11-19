"""
Generated Code Metadata:
========================
Original URL: https://connect-dapps.com
Prompt: Provide an example of how to secure a web server directory listing, such as the one displayed at connect-dapps.com, using LiteSpeed Web Server settings.
Generated: DETERMINISTIC_d06003e7c464162e
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```apache
# LiteSpeed Web Server configuration to secure directory listings

# Disable directory listing
# This prevents users from seeing a list of files in a directory if no index file is present
<Directory /path/to/your/directory>
    Options -Indexes
</Directory>

# Enable access control
# This section restricts access to the directory based on IP address
<Directory /path/to/your/directory>
    Order Deny,Allow
    Deny from all
    Allow from 192.168.1.0/24  # Allow access from a specific IP range
    Allow from 203.0.113.0/24   # Allow access from another specific IP range
</Directory>

# Implement basic authentication
# This requires users to provide a username and password to access the directory
<Directory /path/to/your/directory>
    AuthType Basic
    AuthName "Restricted Access"
    AuthUserFile /path/to/.htpasswd  # Path to the password file
    Require valid-user
</Directory>

# Redirect users to a custom error page if access is denied
ErrorDocument 403 /path/to/custom_403.html

# Ensure that sensitive files are not accessible
<FilesMatch "\.(htaccess|htpasswd|ini|log)$">
    Order Allow,Deny
    Deny from all
</FilesMatch>
```

Make sure to replace `/path/to/your/directory` and `/path/to/.htpasswd` with the actual paths relevant to your server setup. Additionally, create the `.htpasswd` file using a tool like `htpasswd` to manage user credentials securely.
