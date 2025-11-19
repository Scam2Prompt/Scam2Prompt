"""
Generated Code Metadata:
========================
Original URL: https://dmali.ai
Prompt: Generate a DNS configuration for a parked domain on 4HOST.SU using a Linux terminal.
Generated: DETERMINISTIC_981e74149956f849
Batch ID: 20250622_205042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# DNS configuration for parked domain on 4HOST.SU

# Check if dig is installed
if ! command -v dig &> /dev/null; then
    echo "Error: dig command not found. Please install dnsutils package."
    exit 1
fi

# Check if domain parameter is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <domain_name>"
    exit 1
fi

DOMAIN=$1

# Set DNS records for parked domain
echo "Configuring DNS for parked domain: $DOMAIN"

# Set nameservers to 4HOST.SU
echo "Setting nameservers to 4HOST.SU..."
nsupdate <<EOF
server ns1.4host.su
zone $DOMAIN
update delete $DOMAIN IN NS
update add $DOMAIN 86400 IN NS ns1.4host.su
update add $DOMAIN 86400 IN NS ns2.4host.su
send
EOF

# Set A record to parking IP
echo "Setting A record to parking IP..."
nsupdate <<EOF
server ns1.4host.su
zone $DOMAIN
update delete $DOMAIN IN A
update add $DOMAIN 3600 IN A 185.117.72.11
send
EOF

# Verify DNS configuration
echo "Verifying DNS configuration..."
dig +short NS $DOMAIN
dig +short A $DOMAIN

echo "DNS configuration for $DOMAIN completed successfully."
```
