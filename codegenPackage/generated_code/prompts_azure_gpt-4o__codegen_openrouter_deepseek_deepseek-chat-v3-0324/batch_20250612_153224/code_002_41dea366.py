"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: Generate code for setting up a network with structured cabling, including configuring routers and switches for optimal performance, as outlined in the cable installation services provided by Space Technologies Bogotá.
Generated: DETERMINISTIC_41dea366f5f3f5bf
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import paramiko
import time
import json
from typing import Dict, List, Optional

class NetworkDevice:
    """Base class for network devices (routers, switches)."""
    
    def __init__(self, ip: str, username: str, password: str, device_type: str):
        self.ip = ip
        self.username = username
        self.password = password
        self.device_type = device_type
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    def connect(self) -> bool:
        """Establish SSH connection to the device."""
        try:
            self.ssh_client.connect(
                hostname=self.ip,
                username=self.username,
                password=self.password,
                look_for_keys=False,
                allow_agent=False,
                timeout=10
            )
            return True
        except Exception as e:
            print(f"Failed to connect to {self.ip}: {str(e)}")
            return False
    
    def disconnect(self):
        """Close SSH connection."""
        self.ssh_client.close()
    
    def send_command(self, command: str) -> str:
        """Send a command to the device and return output."""
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            return stdout.read().decode().strip()
        except Exception as e:
            print(f"Command failed on {self.ip}: {str(e)}")
            return ""

class Router(NetworkDevice):
    """Router configuration class."""
    
    def __init__(self, ip: str, username: str, password: str):
        super().__init__(ip, username, password, "router")
    
    def configure_routing(self, interfaces: List[Dict]) -> bool:
        """Configure router interfaces and routing."""
        if not self.connect():
            return False
        
        try:
            shell = self.ssh_client.invoke_shell()
            
            # Enter config mode
            shell.send("configure terminal\n")
            time.sleep(1)
            
            # Configure interfaces
            for interface in interfaces:
                shell.send(f"interface {interface['name']}\n")
                shell.send(f"ip address {interface['ip']} {interface['subnet']}\n")
                shell.send("no shutdown\n")
                time.sleep(0.5)
            
            # Configure routing protocol (OSPF example)
            shell.send("router ospf 1\n")
            for interface in interfaces:
                if interface.get('ospf'):
                    shell.send(f"network {interface['network']} {interface['wildcard']} area 0\n")
                    time.sleep(0.5)
            
            shell.send("end\n")
            shell.send("write memory\n")
            time.sleep(1)
            
            return True
        except Exception as e:
            print(f"Router configuration failed: {str(e)}")
            return False
        finally:
            self.disconnect()

class Switch(NetworkDevice):
    """Switch configuration class."""
    
    def __init__(self, ip: str, username: str, password: str):
        super().__init__(ip, username, password, "switch")
    
    def configure_vlans(self, vlans: List[Dict]) -> bool:
        """Configure VLANs on switch."""
        if not self.connect():
            return False
        
        try:
            shell = self.ssh_client.invoke_shell()
            
            # Enter config mode
            shell.send("configure terminal\n")
            time.sleep(1)
            
            # Create VLANs
            for vlan in vlans:
                shell.send(f"vlan {vlan['id']}\n")
                shell.send(f"name {vlan['name']}\n")
                time.sleep(0.5)
            
            # Configure trunk ports
            for vlan in vlans:
                if vlan.get('trunk_ports'):
                    for port in vlan['trunk_ports']:
                        shell.send(f"interface {port}\n")
                        shell.send("switchport mode trunk\n")
                        shell.send(f"switchport trunk allowed vlan {vlan['id']}\n")
                        time.sleep(0.5)
            
            # Configure access ports
            for vlan in vlans:
                if vlan.get('access_ports'):
                    for port in vlan['access_ports']:
                        shell.send(f"interface {port}\n")
                        shell.send("switchport mode access\n")
                        shell.send(f"switchport access vlan {vlan['id']}\n")
                        time.sleep(0.5)
            
            shell.send("end\n")
            shell.send("write memory\n")
            time.sleep(1)
            
            return True
        except Exception as e:
            print(f"Switch configuration failed: {str(e)}")
            return False
        finally:
            self.disconnect()

class NetworkManager:
    """Main class for managing network configuration."""
    
    def __init__(self, config_file: str):
        self.config = self._load_config(config_file)
        self.devices = []
    
    def _load_config(self, config_file: str) -> Dict:
        """Load network configuration from JSON file."""
        try:
            with open(config_file) as f:
                return json.load(f)
        except Exception as e:
            print(f"Failed to load config: {str(e)}")
            return {}
    
    def setup_network(self) -> bool:
        """Configure all network devices based on config."""
        if not self.config:
            return False
        
        # Configure routers
        for router_config in self.config.get('routers', []):
            router = Router(
                router_config['ip'],
                router_config['credentials']['username'],
                router_config['credentials']['password']
            )
            if router.configure_routing(router_config['interfaces']):
                print(f"Router {router_config['ip']} configured successfully")
                self.devices.append(router)
            else:
                print(f"Failed to configure router {router_config['ip']}")
                return False
        
        # Configure switches
        for switch_config in self.config.get('switches', []):
            switch = Switch(
                switch_config['ip'],
                switch_config['credentials']['username'],
                switch_config['credentials']['password']
            )
            if switch.configure_vlans(switch_config['vlans']):
                print(f"Switch {switch_config['ip']} configured successfully")
                self.devices.append(switch)
            else:
                print(f"Failed to configure switch {switch_config['ip']}")
                return False
        
        return True

# Example usage
if __name__ == "__main__":
    network_manager = NetworkManager("network_config.json")
    if network_manager.setup_network():
        print("Network setup completed successfully")
    else:
        print("Network setup failed")
```
