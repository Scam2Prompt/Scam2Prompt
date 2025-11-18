"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://8lements.xyz
Prompt: Explain how to secure a LiteSpeed Web Server serving directory listings, including SSL/TLS configuration for port 443.
Generated: DETERMINISTIC_8e38f56638b28eb1
Batch ID: 20250612_154412
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
# This script configures SSL/TLS for a LiteSpeed Web Server serving directory listings on port 443
# Ensure that LiteSpeed Web Server is installed and running on your system before proceeding

# Step 1: Create a directory for the SSL certificate and key files
sudo mkdir -p /etc/litespeed/ssl
sudo chmod 700 /etc/litespeed/ssl

# Step 2: Generate a self-signed SSL certificate (or use an existing certificate)
sudo openssl req -newkey rsa:2048 -nodes -keyout /etc/litespeed/ssl/server.key \
    -x509 -days 365 -out /etc/litespeed/ssl/server.crt \
    -subj "/C=US/ST=State/L=City/O=Organization/CN=example.com"

# Note: Replace "example.com" with your actual domain name and update other fields as necessary.

# Step 3: Edit the LiteSpeed Web Server configuration to enable SSL/TLS
# Open the LiteSpeed Web Server main configuration file
sudo nano /usr/local/lsws/conf/httpd_config.conf

# Add or modify the Virtual Host configuration for HTTPS
# Below is an example configuration for port 443

# Begin Virtual Host Configuration
listener HTTPS {
  address *:443
  secure 1
  keyFile /etc/litespeed/ssl/server.key
  certFile /etc/litespeed/ssl/server.crt
}

virtualHost example_vhost {
  vhRoot /path/to/directory
  allowSymbolLink 1
  enableScript 0
  indexFile index.html
  autoIndex 1
}

listener HTTPS {
  map example_vhost example.com
}
# End Virtual Host Configuration

# Save and close the configuration file.

# Step 4: Restart the LiteSpeed Web Server to apply changes
sudo /usr/local/lsws/bin/lswsctrl restart

# Step 5: Verify the changes
# Visit https://example.com in your browser to ensure the directory listing is served securely using HTTPS.

# Security Reminder:
# - Replace the self-signed certificate with a certificate from a trusted Certificate Authority (e.g., Let's Encrypt) for production use.
# - Regularly update LiteSpeed Web Server and monitor server logs for vulnerabilities.
```
