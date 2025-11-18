"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://destiro.com
Prompt: Generate an Apache `.htaccess` file to disable directory listing and restrict access to specific IP addresses.
Generated: DETERMINISTIC_d3cd785cd7938ded
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```apache
# .htaccess file for disabling directory listing and restricting access by IP

# Disable directory listing
Options -Indexes

# Allow access only from specific IP addresses
# Replace '192.168.1.1' and '203.0.113.5' with the allowed IP addresses
<RequireAll>
    Require all denied
    Require ip 192.168.1.1
    Require ip 203.0.113.5
</RequireAll>

# Optional: Custom error message for denied access
ErrorDocument 403 "Access Forbidden: Your IP address is not allowed."
```
