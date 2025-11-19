"""
Generated Code Metadata:
========================
Original URL: https://masitsolutions.net
Prompt: Generate a script to configure Fortinet firewalls for managed IT services, based on MASIT Solutions' certified partnership with Fortinet.
Generated: DETERMINISTIC_d0d9c7dc5bd8d80f
Batch ID: 20250612_153224
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
Fortinet Firewall Configuration Script for MASIT Solutions

This script automates the configuration of Fortinet firewalls for managed IT services,
leveraging MASIT Solutions' certified partnership with Fortinet.

Features:
- Basic firewall setup
- Interface configuration
- Security policies
- VPN configuration
- System settings
"""

import paramiko
import time
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('fortinet_config.log'),
        logging.StreamHandler()
    ]
)

class FortinetConfigurator:
    """Main class for Fortinet firewall configuration."""
    
    def __init__(self, host: str, username: str, password: str, port: int = 22):
        """
        Initialize the Fortinet configurator.
        
        Args:
            host: Firewall IP address or hostname
            username: Admin username
            password: Admin password
            port: SSH port (default: 22)
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.shell = None
        
    def connect(self) -> bool:
        """Establish SSH connection to the firewall."""
        try:
            self.ssh.connect(
                self.host,
                port=self.port,
                username=self.username,
                password=self.password,
                look_for_keys=False,
                allow_agent=False
            )
            self.shell = self.ssh.invoke_shell()
            time.sleep(1)  # Wait for shell to initialize
            return True
        except Exception as e:
            logging.error(f"Connection failed: {str(e)}")
            return False
    
    def disconnect(self):
        """Close SSH connection."""
        if self.ssh:
            self.ssh.close()
    
    def send_command(self, command: str, wait_time: float = 1.0) -> str:
        """
        Send a command to the firewall and return the output.
        
        Args:
            command: CLI command to execute
            wait_time: Time to wait for command execution
            
        Returns:
            Command output as string
        """
        if not self.shell:
            raise ConnectionError("SSH connection not established")
            
        self.shell.send(command + '\n')
        time.sleep(wait_time)
        output = self.shell.recv(10000).decode('utf-8')
        return output
    
    def configure_basic_settings(self, hostname: str, timezone: str = 'UTC'):
        """Configure basic system settings."""
        try:
            self.send_command(f'config system global')
            self.send_command(f'set hostname {hostname}')
            self.send_command(f'set timezone {timezone}')
            self.send_command('end')
            logging.info(f"Basic settings configured: hostname={hostname}, timezone={timezone}")
        except Exception as e:
            logging.error(f"Failed to configure basic settings: {str(e)}")
    
    def configure_interface(self, interface: str, ip: str, mask: str, description: str = ''):
        """Configure a network interface."""
        try:
            self.send_command(f'config system interface')
            self.send_command(f'edit {interface}')
            self.send_command(f'set ip {ip} {mask}')
            if description:
                self.send_command(f'set description "{description}"')
            self.send_command('end')
            logging.info(f"Interface {interface} configured: IP={ip}/{mask}")
        except Exception as e:
            logging.error(f"Failed to configure interface {interface}: {str(e)}")
    
    def configure_admin_account(self, username: str, password: str, trusthost: str = '0.0.0.0 0.0.0.0'):
        """Configure an admin account."""
        try:
            self.send_command('config system admin')
            self.send_command(f'edit {username}')
            self.send_command(f'set password {password}')
            self.send_command(f'set trusthost {trusthost}')
            self.send_command('set accprofile super_admin')
            self.send_command('end')
            logging.info(f"Admin account {username} configured")
        except Exception as e:
            logging.error(f"Failed to configure admin account: {str(e)}")
    
    def configure_security_policy(
        self,
        policy_id: int,
        name: str,
        srcintf: str,
        dstintf: str,
        srcaddr: str,
        dstaddr: str,
        service: str,
        action: str = 'accept',
        logtraffic: str = 'all'
    ):
        """Configure a security policy."""
        try:
            self.send_command('config firewall policy')
            self.send_command(f'edit {policy_id}')
            self.send_command(f'set name {name}')
            self.send_command(f'set srcintf {srcintf}')
            self.send_command(f'set dstintf {dstintf}')
            self.send_command(f'set srcaddr {srcaddr}')
            self.send_command(f'set dstaddr {dstaddr}')
            self.send_command(f'set service {service}')
            self.send_command(f'set action {action}')
            self.send_command(f'set logtraffic {logtraffic}')
            self.send_command('end')
            logging.info(f"Security policy {policy_id} ({name}) configured")
        except Exception as e:
            logging.error(f"Failed to configure security policy: {str(e)}")
    
    def configure_vpn(
        self,
        vpn_name: str,
        interface: str,
        psk: str,
        remote_gw: str,
        local_gw: str,
        phase1_proposal: str = 'aes256-sha256',
        phase2_proposal: str = 'aes256-sha256'
    ):
        """Configure an IPsec VPN tunnel."""
        try:
            # Phase 1 configuration
            self.send_command('config vpn ipsec phase1-interface')
            self.send_command(f'edit {vpn_name}')
            self.send_command(f'set interface {interface}')
            self.send_command(f'set peertype any')
            self.send_command(f'set proposal {phase1_proposal}')
            self.send_command(f'set psksecret {psk}')
            self.send_command(f'set remote-gw {remote_gw}')
            self.send_command('end')
            
            # Phase 2 configuration
            self.send_command('config vpn ipsec phase2-interface')
            self.send_command(f'edit {vpn_name}')
            self.send_command(f'set phase1name {vpn_name}')
            self.send_command(f'set proposal {phase2_proposal}')
            self.send_command(f'set src-addr-type name')
            self.send_command(f'set dst-addr-type name')
            self.send_command(f'set src-name {local_gw}')
            self.send_command(f'set dst-name {remote_gw}')
            self.send_command('end')
            
            logging.info(f"VPN {vpn_name} configured")
        except Exception as e:
            logging.error(f"Failed to configure VPN: {str(e)}")
    
    def save_configuration(self):
        """Save the current configuration."""
        try:
            output = self.send_command('execute backup config flash', wait_time=3.0)
            if 'successful' in output.lower():
                logging.info("Configuration saved successfully")
            else:
                logging.error("Failed to save configuration")
        except Exception as e:
            logging.error(f"Failed to save configuration: {str(e)}")

def main():
    """Main execution function."""
    # Example configuration - replace with actual values
    config = {
        'host': '192.168.1.1',
        'username': 'admin',
        'password': 'admin',
        'hostname': 'MASIT-FW01',
        'interfaces': [
            {'name': 'port1', 'ip': '192.168.1.1', 'mask': '255.255.255.0', 'description': 'LAN'},
            {'name': 'port2', 'ip': '203.0.113.1', 'mask': '255.255.255.248', 'description': 'WAN'}
        ],
        'admin_accounts': [
            {'username': 'masit-admin', 'password': 'SecurePassword123!'}
        ],
        'policies': [
            {
                'id': 1,
                'name': 'LAN-to-WAN',
                'srcintf': 'port1',
                'dstintf': 'port2',
                'srcaddr': 'all',
                'dstaddr': 'all',
                'service': 'ALL'
            }
        ],
        'vpns': [
            {
                'name': 'MASIT-HQ-VPN',
                'interface': 'port2',
                'psk': 'SharedSecret123',
                'remote_gw': '203.0.113.2',
                'local_gw': '192.168.1.0/24'
            }
        ]
    }
    
    try:
        # Initialize and connect to firewall
        fw
