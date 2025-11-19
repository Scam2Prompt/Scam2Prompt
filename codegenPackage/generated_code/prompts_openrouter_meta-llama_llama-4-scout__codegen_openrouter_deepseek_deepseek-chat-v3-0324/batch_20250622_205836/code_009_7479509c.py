"""
Generated Code Metadata:
========================
Original URL: https://v2ool.com
Prompt: Create a V2Ray client configuration file for a Linux system using a specific set of protocols and settings.
Generated: DETERMINISTIC_7479509c3250b86f
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```json
{
  // V2Ray client configuration file
  // This configures a client to connect to a V2Ray server with specified protocols
  "log": {
    "access": "/var/log/v2ray/access.log",
    "error": "/var/log/v2ray/error.log",
    "loglevel": "warning"
  },
  "inbounds": [
    {
      "port": 1080,
      "protocol": "socks",
      "settings": {
        "auth": "noauth",
        "udp": true,
        "ip": "127.0.0.1"
      },
      "tag": "socks-inbound"
    },
    {
      "port": 8080,
      "protocol": "http",
      "settings": {
        "allowTransparent": false
      },
      "tag": "http-inbound"
    }
  ],
  "outbounds": [
    {
      "protocol": "vmess",
      "settings": {
        "vnext": [
          {
            "address": "your_server_ip_or_domain", // Replace with actual server address
            "port": 443,
            "users": [
              {
                "id": "your_uuid_here", // Replace with actual UUID
                "alterId": 64,
                "security": "auto"
              }
            ]
          }
        ]
      },
      "streamSettings": {
        "network": "ws",
        "security": "tls",
        "wsSettings": {
          "path": "/your_path", // Replace with actual path
          "headers": {
            "Host": "your_domain" // Replace with actual domain
          }
        },
        "tlsSettings": {
          "serverName": "your_domain", // Replace with actual domain
          "allowInsecure": false
        }
      },
      "tag": "proxy"
    },
    {
      "protocol": "freedom",
      "settings": {},
      "tag": "direct"
    },
    {
      "protocol": "blackhole",
      "settings": {},
      "tag": "block"
    }
  ],
  "routing": {
    "domainStrategy": "IPOnDemand",
    "rules": [
      {
        "type": "field",
        "ip": [
          "geoip:private"
        ],
        "outboundTag": "direct"
      },
      {
        "type": "field",
        "domain": [
          "geosite:category-ads-all"
        ],
        "outboundTag": "block"
      }
    ]
  },
  "dns": {
    "servers": [
      "8.8.8.8",
      "8.8.4.4",
      {
        "address": "1.1.1.1",
        "port": 53,
        "domains": [
          "geosite:netflix",
          "geosite:youtube"
        ]
      }
    ]
  }
}
```
