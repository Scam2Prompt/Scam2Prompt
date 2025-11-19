"""
Generated Code Metadata:
========================
Original URL: https://destiro.com
Prompt: Generate an Apache `.htaccess` file to disable directory listing and restrict access to specific IP addresses.
Generated: DETERMINISTIC_d3cd785cd7938ded
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# .htaccess file to disable directory listing and restrict access to specific IP addresses

# Disable directory listing
Options -Indexes

# Restrict access to specific IP addresses
Order deny,allow
Deny from all

# Allow from specific IP addresses
Allow from 192.168.1.100
Allow from 10.0.0.100

# Allow from a specific network
Allow from 192.168.1.0/24

# Error handling for access denied
ErrorDocument 403 /403-forbidden.html
ErrorDocument 401 /401-unauthorized.html

# Enable rewrite engine for potential future use
RewriteEngine On
```
