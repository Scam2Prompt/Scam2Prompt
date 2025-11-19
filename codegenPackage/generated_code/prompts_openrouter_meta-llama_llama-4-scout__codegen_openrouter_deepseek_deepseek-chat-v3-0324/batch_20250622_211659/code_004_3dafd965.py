"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: "Create a Wi-Fi network configuration script for a professional setup, similar to those provided by Sistemabox's WIFI PROFISSIONAL service."
Generated: DETERMINISTIC_3dafd965b719415d
Batch ID: 20250622_211659
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
Wi-Fi Network Configuration Script

This script automates the configuration of Wi-Fi networks for professional setups.
It supports connecting to WPA/WPA2 secured networks and handles common errors.

Features:
- Scan for available networks
- Connect to a specified network
- Save configuration for auto-connect
- Error handling for common Wi-Fi issues
"""

import subprocess
import json
import re
import sys
from typing import Optional, Dict, List

class WiFiConfigError(Exception):
    """Custom exception for Wi-Fi configuration errors"""
    pass

class WiFiManager:
    def __init__(self, interface: str = 'wlan0'):
        """
        Initialize WiFiManager with network interface.
        
        Args:
            interface: Network interface name (default: wlan0)
        """
        self.interface = interface
        self.sudo_required = True

    def run_command(self, command: str, sudo: bool = False) -> str:
        """
        Execute a shell command and return output.
        
        Args:
            command: Command to execute
            sudo: Whether to run with sudo privileges
            
        Returns:
            Command output as string
            
        Raises:
            WiFiConfigError: If command execution fails
        """
        try:
            if sudo and self.sudo_required:
                command = f'sudo {command}'
            result = subprocess.run(
                command,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            raise WiFiConfigError(f"Command failed: {e.stderr.strip()}") from e

    def scan_networks(self) -> List[Dict[str, str]]:
        """
        Scan for available Wi-Fi networks.
        
        Returns:
            List of dictionaries with network info (SSID, signal, security)
            
        Raises:
            WiFiConfigError: If scanning fails
        """
        try:
            # Ensure interface is up
            self.run_command(f'ip link set {self.interface} up', sudo=True)
            
            # Scan for networks
            scan_result = self.run_command(f'iwlist {self.interface} scan', sudo=True)
            
            networks = []
            current_network = {}
            
            for line in scan_result.split('\n'):
                line = line.strip()
                
                if 'Cell' in line:
                    if current_network:
                        networks.append(current_network)
                    current_network = {}
                    
                if 'ESSID:' in line:
                    current_network['ssid'] = line.split('ESSID:')[1].strip().strip('"')
                    
                if 'Quality=' in line:
                    match = re.search(r'Quality=(\d+/\d+)', line)
                    if match:
                        current_network['signal'] = match.group(1)
                        
                if 'Encryption key:' in line:
                    current_network['encrypted'] = 'on' in line.lower()
                    
                if 'IE: IEEE 802.11i/WPA2' in line:
                    current_network['security'] = 'WPA2'
                    
            if current_network:
                networks.append(current_network)
                
            return networks
            
        except Exception as e:
            raise WiFiConfigError(f"Network scan failed: {str(e)}") from e

    def connect_to_network(self, ssid: str, password: Optional[str] = None) -> bool:
        """
        Connect to a Wi-Fi network.
        
        Args:
            ssid: Network SSID
            password: Network password (optional for open networks)
            
        Returns:
            True if connection succeeded
            
        Raises:
            WiFiConfigError: If connection fails
        """
        try:
            # Stop any existing wpa_supplicant process
            self.run_command('killall wpa_supplicant', sudo=True)
            
            # Generate wpa_supplicant config
            config = f'''
            ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
            update_config=1
            country=US
            
            network={{
                ssid="{ssid}"
                scan_ssid=1
            '''
            
            if password:
                config += f'    psk="{password}"\n'
            else:
                config += '    key_mgmt=NONE\n'
                
            config += '}\n'
            
            # Write config file
            config_path = f'/etc/wpa_supplicant/wpa_supplicant-{self.interface}.conf'
            self.run_command(f'echo \'{config}\' > {config_path}', sudo=True)
            self.run_command(f'chmod 600 {config_path}', sudo=True)
            
            # Start wpa_supplicant
            self.run_command(
                f'wpa_supplicant -B -i {self.interface} -c {config_path}',
                sudo=True
            )
            
            # Request DHCP
            self.run_command(f'dhclient {self.interface}', sudo=True)
            
            # Verify connection
            connected_ssid = self.run_command(
                f'iwgetid {self.interface} -r'
            )
            
            if connected_ssid != ssid:
                raise WiFiConfigError(f"Failed to connect to {ssid}")
                
            return True
            
        except Exception as e:
            raise WiFiConfigError(f"Connection failed: {str(e)}") from e

    def get_current_connection(self) -> Dict[str, str]:
        """
        Get current Wi-Fi connection information.
        
        Returns:
            Dictionary with current connection info
            
        Raises:
            WiFiConfigError: If unable to get connection info
        """
        try:
            result = {}
            
            # Get SSID
            ssid = self.run_command(f'iwgetid {self.interface} -r')
            result['ssid'] = ssid if ssid else None
            
            # Get IP address
            ip_addr = self.run_command(
                f'ip addr show {self.interface} | grep "inet " | awk \'{{print $2}}\''
            )
            result['ip_address'] = ip_addr if ip_addr else None
            
            # Get signal strength
            signal = self.run_command(
                f'iwconfig {self.interface} | grep "Signal level" | awk \'{{print $4}}\''
            )
            result['signal_strength'] = signal if signal else None
            
            return result
            
        except Exception as e:
            raise WiFiConfigError(f"Failed to get connection info: {str(e)}") from e

def main():
    """Main function for command-line usage"""
    try:
        wifi = WiFiManager()
        
        print("Available networks:")
        networks = wifi.scan_networks()
        for i, network in enumerate(networks, 1):
            print(f"{i}. {network.get('ssid', 'Unknown')} ({network.get('security', 'Open')})")
            
        selection = input("\nEnter network number or SSID: ")
        
        # Try to convert to number first
        try:
            selection = int(selection)
            if selection < 1 or selection > len(networks):
                raise ValueError
            ssid = networks[selection-1]['ssid']
        except ValueError:
            ssid = selection
            
        password = None
        if input(f"Does '{ssid}' require a password? (y/n): ").lower() == 'y':
            password = input("Enter password: ")
            
        print(f"\nConnecting to {ssid}...")
        if wifi.connect_to_network(ssid, password):
            connection = wifi.get_current_connection()
            print(f"\nSuccessfully connected to {ssid}")
            print(f"IP Address: {connection.get('ip_address', 'Unknown')}")
            print(f"Signal Strength: {connection.get('signal_strength', 'Unknown')}")
            
    except WiFiConfigError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(0)

if __name__ == '__main__':
    main()
```
