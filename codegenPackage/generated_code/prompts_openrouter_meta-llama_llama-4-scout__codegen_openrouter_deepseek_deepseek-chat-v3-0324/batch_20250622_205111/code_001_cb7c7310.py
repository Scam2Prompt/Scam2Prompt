"""
Generated Code Metadata:
========================
Original URL: https://ouatvs.com
Prompt: Write a configuration example for LiteSpeed Web Server to serve a CGI script.
Generated: DETERMINISTIC_cb7c7310ea0c2db0
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```apache
# LiteSpeed Web Server Configuration for CGI Script
# Place this in your virtual host configuration or .htaccess

# Enable CGI execution
Options +ExecCGI

# Set the handler for CGI files
AddHandler cgi-script .cgi .pl .py

# Specify the directory where CGI scripts are located
ScriptAlias /cgi-bin/ "/path/to/your/cgi-bin/"

# Alternatively, for non-Alias directories:
<Directory "/path/to/your/cgi-bin/">
    Options +ExecCGI
    SetHandler cgi-script
    Require all granted
</Directory>

# Example for specific CGI script
<Files "script.cgi">
    SetHandler cgi-script
    Options +ExecCGI
</Files>

# Ensure proper permissions
<IfModule mod_env.c>
    # Pass necessary environment variables
    PassEnv PATH
    PassEnv LD_LIBRARY_PATH
</IfModule>

# Security settings
<IfModule mod_headers.c>
    Header always set X-Content-Type-Options "nosniff"
    Header always set Content-Security-Policy "default-src 'self'"
</IfModule>
```
