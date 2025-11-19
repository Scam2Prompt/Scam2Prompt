"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudbalancer.io
Prompt: Generate a sample configuration for a managed firewall that aligns with the security standards outlined by kyberio.
Generated: DETERMINISTIC_9ddf0eff55d512a0
Batch ID: 20250612_135929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```json
{
  "firewallConfiguration": {
    "generalSettings": {
      "firewallEnabled": true,              // Enable or disable the firewall globally
      "loggingLevel": "info",              // Logging level: "info", "warn", "error"
      "defaultAction": "deny"              // Default policy for unmatched traffic: "allow" or "deny"
    },
    "networkSettings": {
      "allowedProtocols": [                // Specify allowed protocols for inbound and outbound traffic
        "TCP",
        "UDP",
        "ICMP"
      ],
      "maxConnections": 10000,             // Maximum concurrent connections allowed
      "connectionTimeout": 600             // Connection timeout in seconds
    },
    "rules": [
      {
        "ruleName": "Allow_HTTP_and_HTTPS",// Name of the rule for easy identification
        "priority": 1,                     // Priority of the rule (lower number = higher priority)
        "action": "allow",                 // Action: "allow" or "deny"
        "protocols": ["TCP"],              // Protocols covered by this rule
        "ports": [80, 443],                // Ports allowed by this rule
        "sourceIPs": ["0.0.0.0/0"],        // Source IP range: "0.0.0.0/0" means all sources
        "destinationIPs": ["0.0.0.0/0"],   // Destination IP range: "0.0.0.0/0" means all destinations
        "description": "Permit web traffic"// Human-readable description of the rule
      },
      {
        "ruleName": "Deny_All_ICMP",
        "priority": 2,
        "action": "deny",
        "protocols": ["ICMP"],
        "description": "Block all ICMP traffic to prevent ping floods"
      },
      {
        "ruleName": "Restrict_SSH_Management",
        "priority": 3,
        "action": "allow",
        "protocols": ["TCP"],
        "ports": [22],
        "sourceIPs": ["192.168.1.0/24"],   // Allow SSH only from specific trusted network
        "description": "Restrict SSH access to internal admins"
      }
    ],
    "advancedSettings": {
      "intrusionDetection": true,          // Enable or disable intrusion detection
      "rateLimiting": {                    // Rate limiting settings to prevent DoS attacks
        "enabled": true,
        "maxRequestsPerSecond": 100        // Maximum allowed requests per second per IP
      },
      "applicationLayerFiltering": true    // Enable application layer filtering (e.g., layer 7 filtering)
    },
    "errorHandling": {
      "notifyOnBlock": true,               // Notify admin whenever traffic is blocked
      "notificationSettings": {
        "email": "admin@kyberio.com"       // Email address for notifications
      }
    }
  }
}
```
