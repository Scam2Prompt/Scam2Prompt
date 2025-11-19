"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imts.com.pk
Prompt: Create a configuration example for setting up a secure network infrastructure, including routers and firewalls, based on IMTS's network management services.
Generated: DETERMINISTIC_9cac9527c49e6c8b
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# Configuration Example for Secure Network Infrastructure
# This configuration is designed for a secure setup involving routers and firewalls,
# based on IMTS's network management services.

# Define the network interfaces
interfaces:
  # Router Interface Configuration
  router:
    hostname: "Router1"
    interfaces:
      - name: "eth0"
        ip_address: "192.168.1.1"
        subnet_mask: "255.255.255.0"
        description: "Main LAN Interface"
      - name: "eth1"
        ip_address: "10.0.0.1"
        subnet_mask: "255.255.255.0"
        description: "WAN Interface to ISP"

# Define firewall rules
firewall:
  # Default policy to drop all traffic
  default_policy: "DROP"
  rules:
    - rule_id: 1
      action: "ACCEPT"
      protocol: "tcp"
      src_ip: "192.168.1.0/24"
      dst_ip: "0.0.0.0/0"
      dst_port: "80"
      description: "Allow HTTP traffic from LAN"
    - rule_id: 2
      action: "ACCEPT"
      protocol: "tcp"
      src_ip: "192.168.1.0/24"
      dst_ip: "0.0.0.0/0"
      dst_port: "443"
      description: "Allow HTTPS traffic from LAN"
    - rule_id: 3
      action: "DROP"
      protocol: "tcp"
      src_ip: "0.0.0.0/0"
      dst_ip: "192.168.1.1"
      dst_port: "22"
      description: "Deny SSH access to the router from outside"

# VPN Configuration
vpn:
  enable: true
  type: "IPSec"
  local_ip: "192.168.1.1"
  remote_ip: "203.0.113.1"
  shared_secret: "sEcReT123"
  description: "Site-to-site VPN configuration"

# Monitoring and logging settings
monitoring:
  enable_logging: true
  log_level: "INFO"
  log_destination: "/var/log/network_security.log"
  rotation:
    max_size: "10MB"
    max_files: "5"
  
# Error handling
error_handling:
  - log_errors: true
  - alert_admin: true
  - retry_attempts: 3
```
