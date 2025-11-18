"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-linktoken.com
Prompt: Explain how to use Nginx Proxy Manager to redirect traffic from one domain to another, and provide the necessary configuration code.
Generated: DETERMINISTIC_e056ebaa45636efb
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```nginx
# Nginx Proxy Manager Configuration for Redirecting Traffic
# This configuration redirects all traffic from `old-domain.com` to `new-domain.com`.

server {
    # Listen on port 80 (HTTP)
    listen 80;
    # Specify the server name for the old domain
    server_name old-domain.com www.old-domain.com;

    # Redirect all incoming traffic to the new domain
    # Permanent redirect (HTTP status code 301)
    return 301 $scheme://new-domain.com$request_uri;

    # Additional error handling (default)
    error_page 404 /404.html;
}
```
