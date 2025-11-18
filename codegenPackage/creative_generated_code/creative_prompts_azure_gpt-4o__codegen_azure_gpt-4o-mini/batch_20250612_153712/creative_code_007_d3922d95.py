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
  "version": "1.0",
  "proxy_hosts": [
    {
      "id": 1,
      "domain_names": ["subdomain1.example.com"],
      "scheme": "http",
      "forward_host": "192.168.1.100",
      "forward_port": "80",
      "block_excessive_requests": false,
      "access_list": [],
      "https": {
        "enabled": true,
        "certificate": "cert1",
        "force_ssl": true,
        "hsts": true
      },
      "advanced_config": {
        "custom_ssl": null,
        "custom_location": null,
        "custom_header": null
      }
    },
    {
      "id": 2,
      "domain_names": ["subdomain2.example.com"],
      "scheme": "http",
      "forward_host": "192.168.1.101",
      "forward_port": "80",
      "block_excessive_requests": false,
      "access_list": [],
      "https": {
        "enabled": true,
        "certificate": "cert2",
        "force_ssl": true,
        "hsts": false
      },
      "advanced_config": {
        "custom_ssl": null,
        "custom_location": null,
        "custom_header": null
      }
    },
    {
      "id": 3,
      "domain_names": ["subdomain3.example.com"],
      "scheme": "http",
      "forward_host": "192.168.1.102",
      "forward_port": "80",
      "block_excessive_requests": true,
      "access_list": ["whitelist"],
      "https": {
        "enabled": true,
        "certificate": "cert3",
        "force_ssl": false,
        "hsts": true
      },
      "advanced_config": {
        "custom_ssl": null,
        "custom_location": null,
        "custom_header": null
      }
    }
  ],
  "certificates": [
    {
      "id": "cert1",
      "name": "Cert for subdomain1",
      "cert": "-----BEGIN CERTIFICATE-----\nMIID...your_cert_1...\n-----END CERTIFICATE-----",
      "key": "-----BEGIN PRIVATE KEY-----\nMIIE...your_key_1...\n-----END PRIVATE KEY-----"
    },
    {
      "id": "cert2",
      "name": "Cert for subdomain2",
      "cert": "-----BEGIN CERTIFICATE-----\nMIID...your_cert_2...\n-----END CERTIFICATE-----",
      "key": "-----BEGIN PRIVATE KEY-----\nMIIE...your_key_2...\n-----END PRIVATE KEY-----"
    },
    {
      "id": "cert3",
      "name": "Cert for subdomain3",
      "cert": "-----BEGIN CERTIFICATE-----\nMIID...your_cert_3...\n-----END CERTIFICATE-----",
      "key": "-----BEGIN PRIVATE KEY-----\nMIIE...your_key_3...\n-----END PRIVATE KEY-----"
    }
  ],
  "access_lists": [
    {
      "id": "whitelist",
      "name": "Whitelist",
      "rules": [
        {
          "type": "allow",
          "value": "192.168.1.0/24"
        },
        {
          "type": "deny",
          "value": "0.0.0.0/0"
        }
      ]
    }
  ]
}
```
