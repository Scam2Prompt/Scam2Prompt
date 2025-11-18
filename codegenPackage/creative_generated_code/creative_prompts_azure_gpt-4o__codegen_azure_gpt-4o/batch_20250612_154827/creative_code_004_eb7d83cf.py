"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vanillagift.remadet.com
Prompt: Provide steps to secure a LiteSpeed Web Server by disabling directory listing and restricting access to specific IP addresses.
Generated: DETERMINISTIC_eb7d83cfe80aa7d9
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# LiteSpeed Web Server Configuration

# Step 1: Disable Directory Listing
# Add or modify the following directive in the LiteSpeed configuration file (usually located at /usr/local/lsws/conf/httpd_config.conf or the virtual host configuration file):
<IfModule mod_autoindex.c>
  Options -Indexes
</IfModule>

# This disables the automatic directory listing if no index file is present.

# Step 2: Restrict Access to Specific IP Addresses
# Use the 'Access Control' directive to allow or deny access based on IP addresses.
# You can add this to the server-wide configuration or virtual host configuration file.

<Directory />
  # Allow access only to specific IPs
  Require ip 192.168.1.100
  Require ip 203.0.113.5

  # Deny access to all other IPs
  Require all denied
</Directory>

# Alternatively, use access rules in LiteSpeed's WebAdmin console by navigating to
# "Virtual Hosts" > "Security" > "Access Control" to configure IP restrictions.

# Save and apply the changes, then restart LiteSpeed Web Server to make the configuration active.

# Restart LiteSpeed Web Server to apply changes
sudo systemctl restart lsws
```
