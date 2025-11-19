"""
Generated Code Metadata:
========================
Original URL: https://chillguy.lol
Prompt: Generate a bash script to verify if a domain is pointed to a server and suggest possible reasons for a default server page.
Generated: DETERMINISTIC_09481fbf477c1d1e
Batch ID: 20250622_210108
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Define usage function
usage() {
  echo "Usage: $0 <domain>"
  echo "Verify if a domain is pointed to a server and suggest possible reasons for a default server page."
  exit 1
}

# Check if domain is provided
if [ $# -eq 0 ]; then
  usage
fi

DOMAIN=$1

# Check if domain is valid
if ! [[ $DOMAIN =~ ^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
  echo "Invalid domain: $DOMAIN"
  exit 1
fi

# Perform DNS lookup
DNS_RECORDS=$(dig +short $DOMAIN)

# Check if DNS records exist
if [ -z "$DNS_RECORDS" ]; then
  echo "No DNS records found for $DOMAIN"
  exit 1
fi

# Perform HTTP request to domain
HTTP_RESPONSE=$(curl -s -f -I $DOMAIN)

# Check if HTTP request was successful
if [ $? -ne 0 ]; then
  echo "Failed to retrieve HTTP response from $DOMAIN"
  exit 1
fi

# Parse HTTP response
SERVER_HEADER=$(echo "$HTTP_RESPONSE" | grep -i Server)

# Check if server header is present
if [ -n "$SERVER_HEADER" ]; then
  echo "Server: $(echo "$SERVER_HEADER" | cut -d ':' -f2- | tr -d ' ')"
else
  echo "No server header found in HTTP response"
fi

# Check for default server page
if echo "$HTTP_RESPONSE" | grep -q -i "Welcome to"; then
  echo "Possible reason for default server page: Newly configured server or virtual host"
elif echo "$HTTP_RESPONSE" | grep -q -i "Apache"; then
  echo "Possible reason for default server page: Apache server default page"
elif echo "$HTTP_RESPONSE" | grep -q -i "nginx"; then
  echo "Possible reason for default server page: nginx server default page"
else
  echo "Unable to determine reason for default server page"
fi

# Check for common web server directories
COMMON_DIRS=(/var/www/html /var/www /usr/local/apache2/htdocs)

for dir in "${COMMON_DIRS[@]}"; do
  if [ -d "$dir" ]; then
    echo "Common web server directory found: $dir"
  fi
done

exit 0
```
