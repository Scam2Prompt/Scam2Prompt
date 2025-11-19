"""
Generated Code Metadata:
========================
Original URL: https://prohoster.biz
Prompt: Create a sample configuration for a VPN server on ProHoster that allows P2P connections and hides the real IP address.
Generated: DETERMINISTIC_04b02bc07bb14375
Batch ID: 20250612_140034
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

class VPNConfig:
    def __init__(self, server_ip, server_port, protocol, p2p_allowed=True):
        """
        Initialize VPN configuration.

        Args:
            server_ip (str): IP address of the VPN server.
            server_port (int): Port number of the VPN server.
            protocol (str): Protocol to use (e.g., OpenVPN, WireGuard).
            p2p_allowed (bool): Whether P2P connections are allowed. Defaults to True.
        """
        self.server_ip = server_ip
        self.server_port = server_port
        self.protocol = protocol
        self.p2p_allowed = p2p_allowed

    def generate_config(self):
        """
        Generate VPN configuration.

        Returns:
            dict: VPN configuration.
        """
        config = {
            "server": {
                "ip": self.server_ip,
                "port": self.server_port,
                "protocol": self.protocol
            },
            "p2p": {
                "allowed": self.p2p_allowed
            },
            "security": {
                "hide_ip": True
            }
        }
        return config

    def to_json(self):
        """
        Convert VPN configuration to JSON.

        Returns:
            str: JSON representation of the VPN configuration.
        """
        return json.dumps(self.generate_config(), indent=4)


class ProHosterVPNConfig(VPNConfig):
    def __init__(self, server_ip, server_port, protocol, p2p_allowed=True):
        super().__init__(server_ip, server_port, protocol, p2p_allowed)
        self.prohoster_specific_config = {
            "obfuscation": True,
            "tcp_fastopen": True
        }

    def generate_config(self):
        config = super().generate_config()
        config["prohoster"] = self.prohoster_specific_config
        return config


def main():
    try:
        vpn_config = ProHosterVPNConfig(
            server_ip="example.com",
            server_port=1194,
            protocol="OpenVPN"
        )
        print(vpn_config.to_json())
    except Exception as e:
        print(f"Error generating VPN configuration: {str(e)}")


if __name__ == "__main__":
    main()
```
