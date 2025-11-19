"""
Generated Code Metadata:
========================
Original URL: https://marufonlinebd.net
Prompt: Generate code to configure a dedicated IP for a gaming server, optimizing for low latency as described in MARUF ONLINE BD's services.
Generated: DETERMINISTIC_0b217e6fdcb0874d
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Dedicated IP Configuration for Gaming Server**
=====================================================

**Prerequisites**
---------------

* Python 3.8+
* `paramiko` library for SSH connections
* `netmiko` library for network device interactions

**Code**
------
```python
import paramiko
from netmiko import ConnectHandler
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GamingServerConfigurator:
    def __init__(self, ip, username, password, device_type):
        self.ip = ip
        self.username = username
        self.password = password
        self.device_type = device_type

    def configure_dedicated_ip(self):
        try:
            # Establish SSH connection
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip, username=self.username, password=self.password)

            # Establish Netmiko connection
            net_connect = ConnectHandler(device_type=self.device_type, ip=self.ip, username=self.username, password=self.password)

            # Configure dedicated IP
            config_commands = [
                "interface GigabitEthernet0/0",
                "ip address 10.10.10.10 255.255.255.0",
                "no shutdown",
                "exit",
                "ip route 0.0.0.0 0.0.0.0 10.10.10.1"
            ]

            output = net_connect.send_config_set(config_commands)
            logger.info(output)

            # Optimize for low latency
            self.optimize_for_low_latency(net_connect)

            # Save configuration
            net_connect.save_config()

        except paramiko.AuthenticationException:
            logger.error("Authentication failed. Please check credentials.")
        except Exception as e:
            logger.error(f"An error occurred: {e}")

    def optimize_for_low_latency(self, net_connect):
        try:
            # Configure QoS
            qos_commands = [
                "policy-map QoS_POLICY",
                "class ALL",
                "priority 100",
                "exit",
                "interface GigabitEthernet0/0",
                "service-policy input QoS_POLICY"
            ]

            output = net_connect.send_config_set(qos_commands)
            logger.info(output)

            # Configure TCP optimization
            tcp_commands = [
                "ip tcp nagle",
                "ip tcp window-scale",
                "ip tcp path-mtu-discovery"
            ]

            output = net_connect.send_config_set(tcp_commands)
            logger.info(output)

        except Exception as e:
            logger.error(f"An error occurred while optimizing for low latency: {e}")

if __name__ == "__main__":
    configurator = GamingServerConfigurator(
        ip="192.168.1.100",
        username="admin",
        password="password",
        device_type="cisco_ios"
    )

    configurator.configure_dedicated_ip()
```
**Requirements File**
-------------------
```makefile
paramiko==2.7.2
netmiko==3.1.0
```
**Usage**
-----

1. Install required libraries: `pip install -r requirements.txt`
2. Run the script: `python gaming_server_configurator.py`
