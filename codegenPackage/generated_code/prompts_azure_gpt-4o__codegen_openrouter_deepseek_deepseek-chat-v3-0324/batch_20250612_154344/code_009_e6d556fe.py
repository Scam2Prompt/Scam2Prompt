"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Write code to configure and monitor firewalls and VPNs for a secure business network, based on IMTS's network management services.
Generated: DETERMINISTIC_e6d556fedf9a9a80
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import logging
from typing import List, Dict, Optional
import json
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('network_security.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class FirewallManager:
    """Class to manage firewall configurations"""
    
    def __init__(self, firewall_type: str = 'iptables'):
        self.firewall_type = firewall_type
        
    def add_rule(self, rule: str) -> bool:
        """Add a firewall rule"""
        try:
            if self.firewall_type == 'iptables':
                cmd = f"iptables -A {rule}"
                subprocess.run(cmd, shell=True, check=True)
                logger.info(f"Added firewall rule: {rule}")
                return True
            # Add support for other firewall types here
            else:
                logger.error(f"Unsupported firewall type: {self.firewall_type}")
                return False
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to add firewall rule: {e}")
            return False
    
    def remove_rule(self, rule: str) -> bool:
        """Remove a firewall rule"""
        try:
            if self.firewall_type == 'iptables':
                cmd = f"iptables -D {rule}"
                subprocess.run(cmd, shell=True, check=True)
                logger.info(f"Removed firewall rule: {rule}")
                return True
            else:
                logger.error(f"Unsupported firewall type: {self.firewall_type}")
                return False
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to remove firewall rule: {e}")
            return False
    
    def list_rules(self) -> Optional[List[str]]:
        """List all firewall rules"""
        try:
            if self.firewall_type == 'iptables':
                result = subprocess.run(
                    ["iptables", "-L", "-n", "-v"],
                    capture_output=True,
                    text=True,
                    check=True
                )
                rules = result.stdout.split('\n')
                logger.info("Retrieved firewall rules")
                return rules
            else:
                logger.error(f"Unsupported firewall type: {self.firewall_type}")
                return None
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to list firewall rules: {e}")
            return None

class VPNManager:
    """Class to manage VPN configurations"""
    
    def __init__(self, vpn_type: str = 'openvpn'):
        self.vpn_type = vpn_type
        
    def start_vpn(self, config_path: str) -> bool:
        """Start VPN connection"""
        try:
            if self.vpn_type == 'openvpn':
                cmd = f"openvpn --config {config_path}"
                subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
                logger.info(f"Started VPN with config: {config_path}")
                return True
            else:
                logger.error(f"Unsupported VPN type: {self.vpn_type}")
                return False
        except Exception as e:
            logger.error(f"Failed to start VPN: {e}")
            return False
    
    def stop_vpn(self) -> bool:
        """Stop VPN connection"""
        try:
            if self.vpn_type == 'openvpn':
                subprocess.run(["pkill", "openvpn"], check=True)
                logger.info("Stopped VPN connection")
                return True
            else:
                logger.error(f"Unsupported VPN type: {self.vpn_type}")
                return False
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to stop VPN: {e}")
            return False
    
    def get_status(self) -> Optional[Dict[str, str]]:
        """Get VPN connection status"""
        try:
            if self.vpn_type == 'openvpn':
                result = subprocess.run(
                    ["pgrep", "-x", "openvpn"],
                    capture_output=True,
                    text=True
                )
                status = {
                    'active': bool(result.stdout.strip()),
                    'process_id': result.stdout.strip() or 'None'
                }
                logger.info("Retrieved VPN status")
                return status
            else:
                logger.error(f"Unsupported VPN type: {self.vpn_type}")
                return None
        except Exception as e:
            logger.error(f"Failed to get VPN status: {e}")
            return None

class NetworkMonitor:
    """Class to monitor network security status"""
    
    @staticmethod
    def check_network_connectivity(host: str = "8.8.8.8") -> bool:
        """Check basic network connectivity"""
        try:
            subprocess.run(
                ["ping", "-c", "1", host],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            logger.info(f"Network connectivity to {host} is active")
            return True
        except subprocess.CalledProcessError:
            logger.error(f"No network connectivity to {host}")
            return False
    
    @staticmethod
    def check_open_ports(host: str = "localhost") -> Optional[List[int]]:
        """Check for open ports on a host"""
        try:
            result = subprocess.run(
                ["nmap", "-T4", "-F", host],
                capture_output=True,
                text=True,
                check=True
            )
            open_ports = []
            for line in result.stdout.split('\n'):
                if '/tcp' in line and 'open' in line:
                    port = int(line.split('/')[0])
                    open_ports.append(port)
            logger.info(f"Found open ports on {host}: {open_ports}")
            return open_ports
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to scan ports: {e}")
            return None

class ConfigManager:
    """Class to manage configuration files"""
    
    @staticmethod
    def load_config(config_path: str) -> Optional[Dict]:
        """Load configuration from JSON file"""
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
                logger.info(f"Loaded configuration from {config_path}")
                return config
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Failed to load configuration: {e}")
            return None
    
    @staticmethod
    def save_config(config: Dict, config_path: str) -> bool:
        """Save configuration to JSON file"""
        try:
            with open(config_path, 'w') as f:
                json.dump(config, f, indent=4)
                logger.info(f"Saved configuration to {config_path}")
                return True
        except (IOError, TypeError) as e:
            logger.error(f"Failed to save configuration: {e}")
            return False

def main():
    """Main function to demonstrate functionality"""
    
    # Load configuration
    config = ConfigManager.load_config('network_config.json')
    if not config:
        logger.error("Could not load configuration. Exiting.")
        return
    
    # Initialize managers
    firewall = FirewallManager(config.get('firewall_type', 'iptables'))
    vpn = VPNManager(config.get('vpn_type', 'openvpn'))
    
    # Apply firewall rules
    for rule in config.get('firewall_rules', []):
        firewall.add_rule(rule)
    
    # Start VPN if configured
    if config.get('vpn_config'):
        vpn.start_vpn(config['vpn_config'])
    
    # Monitor network
    monitor = NetworkMonitor()
    while True:
        monitor.check_network_connectivity()
        monitor.check_open_ports()
        
        # Check VPN status
        vpn_status = vpn.get_status()
        logger.info(f"Current VPN Status: {vpn_status}")
        
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
```
