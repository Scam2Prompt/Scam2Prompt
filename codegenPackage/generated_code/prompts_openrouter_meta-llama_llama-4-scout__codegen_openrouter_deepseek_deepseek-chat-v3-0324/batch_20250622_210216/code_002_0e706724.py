"""
Generated Code Metadata:
========================
Original URL: https://000000011.xyz
Prompt: Generate a configuration for a multi-homed backbone network like PRQ's AS33837, including DDoS attack mitigation and high-traffic website hosting.
Generated: DETERMINISTIC_0e7067244507476e
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Backbone Network Configuration Generator for AS33837-like setup
Includes DDoS mitigation and high-traffic hosting capabilities
"""

import yaml
from jinja2 import Environment, FileSystemLoader

# Network configuration constants
CONFIG_TEMPLATE = "network_config.j2"
OUTPUT_FILE = "generated_config.cfg"

# Base network parameters
NETWORK_PARAMS = {
    "asn": 33837,
    "router_id": "192.0.2.1",
    "ipv4_prefixes": [
        "192.0.2.0/24",
        "203.0.113.0/24",
        "198.51.100.0/24"
    ],
    "ipv6_prefixes": [
        "2001:db8::/32",
        "2001:db8:1::/48"
    ],
    "peers": [
        {
            "asn": 64512,
            "ipv4": "192.0.2.2",
            "ipv6": "2001:db8::2",
            "type": "transit"
        },
        {
            "asn": 64513,
            "ipv4": "192.0.2.3",
            "ipv6": "2001:db8::3",
            "type": "peer"
        }
    ],
    "ddos_protection": {
        "scrubbing_centers": [
            {"ip": "192.0.2.100", "location": "ams1"},
            {"ip": "192.0.2.101", "location": "nyc1"}
        ],
        "thresholds": {
            "syn_flood": "1000pps",
            "udp_flood": "2000pps",
            "icmp_flood": "500pps"
        },
        "blackhole_routing": True
    },
    "hosting": {
        "web_servers": [
            {"ip": "203.0.113.10", "role": "frontend"},
            {"ip": "203.0.113.11", "role": "backend"}
        ],
        "load_balancers": [
            {"ip": "203.0.113.20", "vip": "203.0.113.100"}
        ],
        "rate_limits": {
            "http": "10000r/s",
            "https": "5000r/s"
        }
    }
}

def generate_config():
    """Generate network configuration from template"""
    try:
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(CONFIG_TEMPLATE)
        
        with open(OUTPUT_FILE, 'w') as f:
            f.write(template.render(NETWORK_PARAMS))
        
        print(f"Configuration generated successfully: {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error generating configuration: {str(e)}")
        raise

def validate_config():
    """Validate the generated configuration"""
    try:
        with open(OUTPUT_FILE, 'r') as f:
            config = f.read()
        
        # Basic validation checks
        assert "router bgp 33837" in config, "BGP configuration missing"
        assert "ip prefix-list" in config, "Prefix lists missing"
        assert "scrubbing-center" in config.lower(), "DDoS scrubbing missing"
        assert "load-balancing" in config.lower(), "Load balancing missing"
        
        print("Configuration validation passed")
    except AssertionError as e:
        print(f"Configuration validation failed: {str(e)}")
        raise
    except Exception as e:
        print(f"Error validating configuration: {str(e)}")
        raise

if __name__ == "__main__":
    generate_config()
    validate_config()
```

```jinja
{# network_config.j2 - Jinja2 template for network configuration #}
! Device: Backbone Router AS{{ asn }}
! Generated configuration for multi-homed network with DDoS protection
! and high-traffic hosting capabilities

hostname backbone-router-{{ router_id.split('.')[-1] }}

! Basic router configuration
service password-encryption
no ip domain-lookup
ip cef
ipv6 unicast-routing

! Interface configuration
interface Loopback0
 ip address {{ router_id }} 255.255.255.255
 ipv6 address 2001:db8::1/128
!
{% for peer in peers %}
interface GigabitEthernet0/0/{{ loop.index }}
 description Peer: AS{{ peer.asn }} ({{ peer.type }})
 ip address {{ peer.ipv4 }} 255.255.255.252
 ipv6 address {{ peer.ipv6 }}/64
 ipv6 enable
 no shutdown
!
{% endfor %}

! BGP Configuration
router bgp {{ asn }}
 bgp router-id {{ router_id }}
 bgp log-neighbor-changes
 {% for peer in peers %}
 neighbor {{ peer.ipv4 }} remote-as {{ peer.asn }}
 neighbor {{ peer.ipv4 }} description AS{{ peer.asn }} ({{ peer.type }})
 neighbor {{ peer.ipv6 }} remote-as {{ peer.asn }}
 neighbor {{ peer.ipv6 }} description AS{{ peer.asn }} ({{ peer.type }})
 {% endfor %}
 !
 address-family ipv4
  {% for prefix in ipv4_prefixes %}
  network {{ prefix }}
  {% endfor %}
  {% for peer in peers %}
  neighbor {{ peer.ipv4 }} activate
  neighbor {{ peer.ipv4 }} soft-reconfiguration inbound
  neighbor {{ peer.ipv4 }} route-map FILTER-IN in
  neighbor {{ peer.ipv4 }} route-map FILTER-OUT out
  {% endfor %}
 exit-address-family
 !
 address-family ipv6
  {% for prefix in ipv6_prefixes %}
  network {{ prefix }}
  {% endfor %}
  {% for peer in peers %}
  neighbor {{ peer.ipv6 }} activate
  neighbor {{ peer.ipv6 }} soft-reconfiguration inbound
  neighbor {{ peer.ipv6 }} route-map FILTER-IN-V6 in
  neighbor {{ peer.ipv6 }} route-map FILTER-OUT-V6 out
  {% endfor %}
 exit-address-family

! DDoS Protection Configuration
{% if ddos_protection.blackhole_routing %}
ip route 192.0.2.254 255.255.255.255 Null0
ipv6 route 2001:db8:ffff::/128 Null0
!
{% endif %}
{% for center in ddos_protection.scrubbing_centers %}
ip route {{ center.ip }} 255.255.255.255 {{ center.ip }}
!
{% endfor %}

! Access control for DDoS mitigation
ip access-list extended ACL-DDOS-MITIGATION
 deny tcp any any fragments
 deny udp any any fragments
 deny icmp any any fragments
 permit ip any any
!
ipv6 access-list ACL-V6-DDOS-MITIGATION
 deny tcp any any fragments
 deny udp any any fragments
 deny icmp any any fragments
 permit ipv6 any any
!

! Hosting Infrastructure Configuration
{% for server in hosting.web_servers %}
ip host web-{{ server.role }}-{{ loop.index }} {{ server.ip }}
!
{% endfor %}
{% for lb in hosting.load_balancers %}
ip host lb-{{ loop.index }} {{ lb.ip }}
ip host vip-{{ loop.index }} {{ lb.vip }}
!
{% endfor %}

! Rate limiting for hosted services
rate-limit input access-group 101 {{ hosting.rate_limits.http }} conform-action transmit exceed-action drop
rate-limit input access-group 102 {{ hosting.rate_limits.https }} conform-action transmit exceed-action drop

! Logging and monitoring
logging trap debugging
logging {{ ddos_protection.scrubbing_centers[0].ip }}
snmp-server community secure RO
snmp-server enable traps bgp

! End of configuration
end
```
