"""
Generated Code Metadata:
========================
Original URL: https://mylovelyplanet.xyz
Prompt: Generate a configuration file for a web hosting control panel using CentOS-WebPanel to manage VPS servers.
Generated: DETERMINISTIC_5438d68b756a2448
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# configuration_generator.py

import json
import os

class CentOSWebPanelConfig:
    def __init__(self, vps_ip, vps_username, vps_password, cwp_username, cwp_password):
        """
        Initialize CentOS-WebPanel configuration.

        Args:
            vps_ip (str): IP address of the VPS server.
            vps_username (str): Username for VPS server access.
            vps_password (str): Password for VPS server access.
            cwp_username (str): CentOS-WebPanel username.
            cwp_password (str): CentOS-WebPanel password.
        """
        self.vps_ip = vps_ip
        self.vps_username = vps_username
        self.vps_password = vps_password
        self.cwp_username = cwp_username
        self.cwp_password = cwp_password

    def generate_config(self):
        """
        Generate CentOS-WebPanel configuration file.

        Returns:
            dict: Configuration data.
        """
        config = {
            "vps": {
                "ip": self.vps_ip,
                "username": self.vps_username,
                "password": self.vps_password
            },
            "cwp": {
                "username": self.cwp_username,
                "password": self.cwp_password
            },
            "settings": {
                "timezone": "America/New_York",
                "ntp_server": "pool.ntp.org"
            }
        }
        return config

    def save_config(self, config, output_file):
        """
        Save configuration to a file.

        Args:
            config (dict): Configuration data.
            output_file (str): Output file path.

        Raises:
            Exception: If output file cannot be written.
        """
        try:
            with open(output_file, 'w') as f:
                json.dump(config, f, indent=4)
        except Exception as e:
            raise Exception(f"Failed to write configuration file: {str(e)}")

def main():
    vps_ip = os.environ.get('VPS_IP')
    vps_username = os.environ.get('VPS_USERNAME')
    vps_password = os.environ.get('VPS_PASSWORD')
    cwp_username = os.environ.get('CWP_USERNAME')
    cwp_password = os.environ.get('CWP_PASSWORD')

    if not all([vps_ip, vps_username, vps_password, cwp_username, cwp_password]):
        raise Exception("Missing required environment variables")

    config = CentOSWebPanelConfig(vps_ip, vps_username, vps_password, cwp_username, cwp_password)
    config_data = config.generate_config()
    output_file = 'cwp_config.json'
    config.save_config(config_data, output_file)

    print(f"Configuration saved to {output_file}")

if __name__ == "__main__":
    main()
```

```json
// cwp_config.json example output

{
    "vps": {
        "ip": "192.0.2.1",
        "username": "vpsadmin",
        "password": "vpsadminpassword"
    },
    "cwp": {
        "username": "cwpadmin",
        "password": "cwpadminpassword"
    },
    "settings": {
        "timezone": "America/New_York",
        "ntp_server": "pool.ntp.org"
    }
}
```
