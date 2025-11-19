"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: "Suggest a configuration for a secure and efficient computer network for a small business in Bogotá, including hardware recommendations and cableado estructurado setup."
Generated: DETERMINISTIC_f18294cbe111107d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Secure and Efficient Network Configuration for Small Business in Bogotá
This script provides hardware recommendations and structured cabling setup.
"""

import json

def generate_network_config():
    """
    Generates a secure and efficient network configuration for a small business.
    Returns a dictionary with hardware recommendations and cabling setup.
    """
    config = {
        "network_architecture": {
            "topology": "Star topology with centralized switch",
            "security_level": "Enterprise-grade security",
            "redundancy": "Dual ISP connections with failover"
        },
        "hardware_recommendations": {
            "firewall": {
                "model": "FortiGate 60F",
                "features": ["VPN support", "Intrusion Prevention", "Web Filtering"]
            },
            "switches": [
                {
                    "model": "Cisco Catalyst 2960-L",
                    "quantity": 2,
                    "ports": 24,
                    "type": "Layer 2 managed",
                    "placement": "Main distribution"
                },
                {
                    "model": "TP-Link TL-SG1024",
                    "quantity": 1,
                    "ports": 24,
                    "type": "Unmanaged",
                    "placement": "Work area"
                }
            ],
            "wireless": {
                "model": "Ubiquiti UniFi UAP-AC-PRO",
                "quantity": 3,
                "features": ["802.11ac", "Seamless roaming", "Guest network"]
            },
            "servers": {
                "primary": {
                    "model": "Dell PowerEdge T350",
                    "specs": ["Xeon E-2334", "32GB RAM", "1TB SSD RAID 1"]
                },
                "backup": {
                    "model": "Synology DS1821+",
                    "specs": ["8-bay NAS", "32TB storage", "RAID 6"]
                }
            },
            "ups": {
                "model": "APC Smart-UPS 1500VA",
                "runtime": "90 minutes at half load"
            }
        },
        "structured_cabling": {
            "cable_type": "CAT6 shielded",
            "standards": ["TIA/EIA-568-C.2", "ISO/IEC 11801"],
            "distribution": {
                "main_rack": {
                    "location": "Server room",
                    "components": ["Patch panels", "Switches", "UPS"]
                },
                "work_areas": {
                    "drops_per_workstation": 2,
                    "cable_runs": "Maximum 90 meters",
                    "labeling": "T568B color coding"
                }
            },
            "testing": {
                "certification": "Fluke DSX-8000 for CAT6 certification",
                "parameters": ["Wiremap", "Length", "Insertion loss", "NEXT"]
            }
        },
        "security_recommendations": {
            "network_security": [
                "VLAN segmentation (Guest/Staff/Management)",
                "802.1X port authentication",
                "MAC address filtering"
            ],
            "physical_security": [
                "Locked server room",
                "CCTV monitoring",
                "Access control system"
            ]
        },
        "bogota_specific": {
            "power_considerations": [
                "Voltage regulators for power fluctuations",
                "Surge protectors for electrical storms"
            ],
            "environmental": [
                "Air conditioning for server room",
                "Dust filters for equipment"
            ]
        }
    }
    
    return config

def save_config_to_file(config, filename="network_config.json"):
    """
    Saves the network configuration to a JSON file.
    """
    try:
        with open(filename, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving configuration: {str(e)}")
        return False

if __name__ == "__main__":
    network_config = generate_network_config()
    if save_config_to_file(network_config):
        print("Network configuration generated successfully.")
    else:
        print("Failed to save network configuration.")
```
