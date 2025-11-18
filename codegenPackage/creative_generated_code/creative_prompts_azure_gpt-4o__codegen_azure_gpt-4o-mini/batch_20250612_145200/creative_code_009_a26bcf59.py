"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idn-hosting.com
Prompt: Create a configuration for dual-stack IPv4 and IPv6 networking on IDN Hosting's data centers in Jakarta and Singapore.
Generated: DETERMINISTIC_a26bcf59ca97756f
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Configuration for dual-stack networking
class DualStackNetworkConfig:
    def __init__(self, location):
        self.location = location
        self.config = {
            "ipv4": {
                "enabled": True,
                "subnet": "192.0.2.0/24",
                "gateway": "192.0.2.1",
                "dns": ["8.8.8.8", "8.8.4.4"]
            },
            "ipv6": {
                "enabled": True,
                "subnet": "2001:db8::/32",
                "gateway": "2001:db8::1",
                "dns": ["2001:4860:4860::8888", "2001:4860:4860::8844"]
            }
        }

    def generate_config(self):
        """Generate the dual-stack configuration."""
        try:
            config_json = json.dumps(self.config, indent=4)
            logging.info(f"Configuration for {self.location} generated successfully.")
            return config_json
        except Exception as e:
            logging.error(f"Error generating configuration: {e}")
            return None

def main():
    """Main function to create networking configurations."""
    try:
        # Create configurations for both Jakarta and Singapore
        jakarta_config = DualStackNetworkConfig("Jakarta")
        singapore_config = DualStackNetworkConfig("Singapore")

        # Generate and print configurations
        logging.info("Generating configurations...")
        print("Jakarta Configuration:\n", jakarta_config.generate_config())
        print("Singapore Configuration:\n", singapore_config.generate_config())
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
