"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-linktoken.com
Prompt: Provide an example of a JSON configuration file for Nginx Proxy Manager to handle multiple subdomains.
Generated: DETERMINISTIC_d3922d95ce06592c
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```json
{
  "hosts": [
    {
      "domain": "subdomain1.example.com",
      "forward_ip": "192.168.1.101",
      "forward_port": 8080,
      "ssl": {
        "enabled": true,
        "force_https": true,
        "certificate_provider": "letsencrypt",
        "certificate_email": "admin@example.com"
      },
      "access_log": "/var/log/nginx/subdomain1-access.log",
      "error_log": "/var/log/nginx/subdomain1-error.log"
    },
    {
      "domain": "subdomain2.example.com",
      "forward_ip": "192.168.1.102",
      "forward_port": 3000,
      "ssl": {
        "enabled": true,
        "force_https": true,
        "certificate_provider": "letsencrypt",
        "certificate_email": "admin@example.com"
      },
      "access_log": "/var/log/nginx/subdomain2-access.log",
      "error_log": "/var/log/nginx/subdomain2-error.log"
    },
    {
      "domain": "subdomain3.example.com",
      "forward_ip": "192.168.1.103",
      "forward_port": 5000,
      "ssl": {
        "enabled": false,
        "force_https": false
      },
      "access_log": "/var/log/nginx/subdomain3-access.log",
      "error_log": "/var/log/nginx/subdomain3-error.log"
    }
  ]
}
```
