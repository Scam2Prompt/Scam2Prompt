"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linkairdrop.com
Prompt: Provide a detailed example of setting up custom access rules for a proxy host using Nginx Proxy Manager.
Generated: DETERMINISTIC_686a60d3c65ca9d4
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
version: '3.8'

services:
  nginx-proxy-manager:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    restart: unless-stopped
    ports:
      - "80:80"    # Default HTTP port
      - "81:81"    # Admin interface port
      - "443:443"  # Default HTTPS port
    environment:
      - DB_SQLITE=true  # Use SQLite for database
      - TZ=America/New_York # Set timezone
    volumes:
      - ./data:/data   # Persistent data storage
      - ./letsencrypt:/etc/letsencrypt # SSL certificates storage

# Once the container is set up, edit the custom access rules in the Nginx Proxy Manager UI
# Example configuration snippet for a proxy host with custom access rules in the Nginx Proxy Manager UI.

# To manually configure custom access rules, add the following under the "Advanced" tab of a Proxy Host:
# ===========================
# Example custom access rules
# ===========================
#
# # Block IPs from accessing the proxy host
# deny 192.168.1.100;   # Block specific IP
# deny 10.0.0.0/8;      # Block entire subnet
#
# # Allow access to the proxy host only to specific IPs
# allow 203.0.113.50;   # Allow specific IP
# allow 198.51.100.0/24; # Allow subnet range
# deny all;             # Deny all other traffic
#
# ===========================
# You can apply these access rules by pasting them into the "Custom Nginx Configuration" field for a proxy host.
```
