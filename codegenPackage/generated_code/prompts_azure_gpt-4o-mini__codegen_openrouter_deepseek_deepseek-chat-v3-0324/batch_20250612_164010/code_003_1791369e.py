"""
Generated Code Metadata:
========================
Original URL: https://marketdarkzone.uk
Prompt: Generate a sample configuration for setting up DDoS protection on a server with BlazingFast.
Generated: DETERMINISTIC_1791369ec8b5623e
Batch ID: 20250612_164010
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
BlazingFast DDoS Protection Configuration Script

This script generates a sample configuration for setting up DDoS protection
on a server using BlazingFast's services.

Features:
- Rate limiting configuration
- IP whitelisting/blacklisting
- Anomaly detection thresholds
- GeoIP filtering
"""

import json
import ipaddress

def validate_ip(ip_str):
    """Validate an IP address string."""
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def generate_ddos_config():
    """
    Generate a sample BlazingFast DDoS protection configuration.
    
    Returns:
        dict: Configuration dictionary ready for JSON serialization
    """
    config = {
        "version": "1.0",
        "description": "BlazingFast DDoS Protection Configuration",
        "settings": {
            "general": {
                "enabled": True,
                "mode": "auto",  # auto, manual, learning
                "log_level": "warning"  # debug, info, warning, error
            },
            "rate_limiting": {
                "http_requests": {
                    "enabled": True,
                    "requests_per_minute": 1000,
                    "burst_limit": 200,
                    "action": "block"  # block, challenge, throttle
                },
                "tcp_connections": {
                    "enabled": True,
                    "connections_per_minute": 500,
                    "action": "block"
                }
            },
            "ip_filtering": {
                "whitelist": [
                    "192.168.1.1",
                    "10.0.0.0/24"
                ],
                "blacklist": [
                    "1.1.1.1",
                    "2.2.2.0/24"
                ],
                "country_filter": {
                    "enabled": True,
                    "allowed_countries": ["US", "CA", "GB"],
                    "block_tor_nodes": True
                }
            },
            "anomaly_detection": {
                "thresholds": {
                    "packet_size": {
                        "max_bytes": 1500,
                        "action": "block"
                    },
                    "request_patterns": {
                        "enabled": True,
                        "sensitivity": "medium"  # low, medium, high
                    }
                }
            },
            "monitoring": {
                "enable_live_monitoring": True,
                "stats_interval": 60,  # seconds
                "alert_settings": {
                    "email_alerts": True,
                    "slack_webhook": None,
                    "thresholds": {
                        "bandwidth": "100Mbps",
                        "packet_rate": "100kpps"
                    }
                }
            }
        }
    }

    # Validate IP addresses in the config
    for ip in config["settings"]["ip_filtering"]["whitelist"]:
        if not validate_ip(ip.split('/')[0]):
            raise ValueError(f"Invalid IP address in whitelist: {ip}")

    for ip in config["settings"]["ip_filtering"]["blacklist"]:
        if not validate_ip(ip.split('/')[0]):
            raise ValueError(f"Invalid IP address in blacklist: {ip}")

    return config

if __name__ == "__main__":
    try:
        config = generate_ddos_config()
        print(json.dumps(config, indent=2))
    except ValueError as e:
        print(f"Configuration error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)
```
