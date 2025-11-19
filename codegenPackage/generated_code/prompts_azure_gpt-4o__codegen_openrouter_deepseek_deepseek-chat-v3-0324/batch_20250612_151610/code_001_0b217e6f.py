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

```python
#!/usr/bin/env python3
import subprocess
import sys
import os
from typing import Optional, List

class GamingServerConfigurator:
    """
    Configures a dedicated IP for a gaming server with low latency optimization.
    """
    
    def __init__(self, interface: str, ip_address: str, netmask: str = "255.255.255.0", gateway: Optional[str] = None):
        """
        Initialize the configurator with network parameters.
        
        Args:
            interface: Network interface name (e.g., eth0)
            ip_address: Dedicated IP address to assign
            netmask: Network mask (default: 255.255.255.0)
            gateway: Optional gateway address
        """
        self.interface = interface
        self.ip_address = ip_address
        self.netmask = netmask
        self.gateway = gateway
        self.validate_parameters()
    
    def validate_parameters(self) -> None:
        """Validate the provided network parameters."""
        if not self.interface:
            raise ValueError("Network interface cannot be empty")
        if not self.ip_address:
            raise ValueError("IP address cannot be empty")
    
    def run_command(self, command: List[str]) -> None:
        """
        Execute a shell command with error handling.
        
        Args:
            command: List of command arguments
            
        Raises:
            subprocess.CalledProcessError: If command fails
        """
        try:
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Command failed: {' '.join(command)}\nError: {e.stderr.decode()}") from e
    
    def configure_static_ip(self) -> None:
        """Configure a static IP address on the interface."""
        commands = [
            ["ip", "addr", "add", f"{self.ip_address}/{self.netmask}", "dev", self.interface],
            ["ip", "link", "set", "dev", self.interface, "up"]
        ]
        
        if self.gateway:
            commands.append(["ip", "route", "add", "default", "via", self.gateway])
        
        for cmd in commands:
            self.run_command(cmd)
    
    def optimize_network(self) -> None:
        """Apply network optimizations for low latency gaming."""
        optimizations = [
            # Increase socket buffer sizes
            ["sysctl", "-w", "net.core.rmem_max=4194304"],
            ["sysctl", "-w", "net.core.wmem_max=4194304"],
            ["sysctl", "-w", "net.core.rmem_default=4194304"],
            ["sysctl", "-w", "net.core.wmem_default=4194304"],
            
            # TCP optimizations
            ["sysctl", "-w", "net.ipv4.tcp_window_scaling=1"],
            ["sysctl", "-w", "net.ipv4.tcp_timestamps=1"],
            ["sysctl", "-w", "net.ipv4.tcp_sack=1"],
            ["sysctl", "-w", "net.ipv4.tcp_no_metrics_save=1"],
            ["sysctl", "-w", "net.ipv4.tcp_low_latency=1"],
            
            # Disable slow start after idle
            ["sysctl", "-w", "net.ipv4.tcp_slow_start_after_idle=0"],
            
            # Increase local port range
            ["sysctl", "-w", "net.ipv4.ip_local_port_range='1024 65535'"],
            
            # Increase connection tracking
            ["sysctl", "-w", "net.netfilter.nf_conntrack_max=524288"],
        ]
        
        for opt in optimizations:
            self.run_command(opt)
    
    def configure_firewall(self) -> None:
        """Configure basic firewall rules for gaming server."""
        firewall_rules = [
            ["iptables", "-A", "INPUT", "-p", "tcp", "--dport", "27015:27030", "-j", "ACCEPT"],  # Steam ports
            ["iptables", "-A", "INPUT", "-p", "udp", "--dport", "27015:27030", "-j", "ACCEPT"],
            ["iptables", "-A", "INPUT", "-p", "udp", "--dport", "4380", "-j", "ACCEPT"],
            ["iptables", "-A", "INPUT", "-p", "udp", "--dport", "3478:3480", "-j", "ACCEPT"],  # STUN/TURN
            ["iptables", "-A", "INPUT", "-m", "conntrack", "--ctstate", "ESTABLISHED,RELATED", "-j", "ACCEPT"],
            ["iptables", "-P", "INPUT", "DROP"],
            ["iptables", "-P", "FORWARD", "DROP"],
        ]
        
        for rule in firewall_rules:
            self.run_command(rule)
    
    def save_configuration(self) -> None:
        """Persist configuration changes across reboots."""
        try:
            with open("/etc/rc.local", "a") as f:
                f.write(f"\nip addr add {self.ip_address}/{self.netmask} dev {self.interface}\n")
                f.write(f"ip link set dev {self.interface} up\n")
                if self.gateway:
                    f.write(f"ip route add default via {self.gateway}\n")
        except IOError as e:
            raise RuntimeError(f"Failed to save configuration: {str(e)}")
    
    def configure(self) -> None:
        """Execute full configuration process."""
        print(f"Configuring dedicated IP {self.ip_address} for gaming server...")
        self.configure_static_ip()
        self.optimize_network()
        self.configure_firewall()
        self.save_configuration()
        print("Configuration completed successfully!")

def main():
    if os.geteuid() != 0:
        print("Error: This script must be run as root", file=sys.stderr)
        sys.exit(1)
    
    try:
        configurator = GamingServerConfigurator(
            interface="eth0",
            ip_address="192.168.1.100",
            netmask="255.255.255.0",
            gateway="192.168.1.1"
        )
        configurator.configure()
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
