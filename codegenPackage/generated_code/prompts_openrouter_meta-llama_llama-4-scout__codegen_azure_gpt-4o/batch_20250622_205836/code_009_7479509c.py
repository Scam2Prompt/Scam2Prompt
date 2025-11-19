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
  "log": {
    "access": "/var/log/v2ray/access.log",  // Path to access log file
    "error": "/var/log/v2ray/error.log",    // Path to error log file
    "loglevel": "warning"                  // Log level: debug, info, warning, error
  },
  "inbounds": [
    {
      "port": 1080,                        // Port for incoming connections
      "listen": "127.0.0.1",               // Bind address
      "protocol": "socks",                 // Protocol: SOCKS5
      "settings": {
        "auth": "noauth",                  // Authentication method: noauth or password
        "udp": true,                       // Enable UDP forwarding
        "ip": "127.0.0.1"                  // IP address for the SOCKS server
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "vmess",                 // Protocol: VMess
      "settings": {
        "vnext": [
          {
            "address": "example.com",      // Server address
            "port": 443,                   // Server port
            "users": [
              {
                "id": "your-uuid-here",    // Unique user ID (UUID)
                "alterId": 64,             // Alter ID for VMess protocol
                "security": "auto"         // Encryption method: auto, aes-128-gcm, etc.
              }
            ]
          }
        ]
      },
      "streamSettings": {
        "network": "tcp",                  // Network type: tcp, kcp, ws, etc.
        "security": "tls",                 // Security: tls or none
        "tlsSettings": {
          "serverName": "example.com",     // Server name for TLS handshake
          "allowInsecure": false           // Allow insecure connections (false recommended)
        }
      }
    }
  ],
  "dns": {
    "servers": [
      "8.8.8.8",                           // Google DNS
      "8.8.4.4"                            // Google DNS
    ]
  },
  "routing": {
    "domainStrategy": "AsIs",              // Domain strategy: AsIs, IPIfNonMatch, etc.
    "rules": [
      {
        "type": "field",
        "domain": [
          "geosite:cn"                     // Domains matching Chinese sites
        ],
        "outboundTag": "direct"            // Route to direct connection
      },
      {
        "type": "field",
        "domain": [
          "geosite:geolocation-!cn"        // Domains outside China
        ],
        "outboundTag": "proxy"             // Route to proxy connection
      }
    ]
  }
}
```
