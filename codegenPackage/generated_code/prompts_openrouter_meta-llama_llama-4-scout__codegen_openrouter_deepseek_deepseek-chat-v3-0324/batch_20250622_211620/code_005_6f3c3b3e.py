"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: "Create a script to monitor and manage IT infrastructure, including routers, switches, firewalls, and VPNs, using Python and SNMP."
Generated: DETERMINISTIC_6f3c3b3e5dffacf3
Batch ID: 20250622_211620
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
IT Infrastructure Monitoring and Management Script

This script monitors and manages network devices (routers, switches, firewalls, VPNs)
using SNMP protocol. It provides functionality to:
- Collect device metrics
- Check device status
- Perform basic management tasks

Requirements:
- Python 3.6+
- pysnmp library
"""

import time
from datetime import datetime
from pysnmp.hlapi import (
    getCmd,
    SnmpEngine,
    CommunityData,
    UdpTransportTarget,
    ContextData,
    ObjectType,
    ObjectIdentity,
    OctetString,
)
from pysnmp.smi.rfc1902 import ObjectIdentity
import logging
from typing import List, Dict, Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("infra_monitor.log"),
        logging.StreamHandler()
    ]
)

class DeviceMonitor:
    """Class to monitor and manage network devices using SNMP"""
    
    def __init__(self, community: str = "public", timeout: int = 2, retries: int = 2):
        """
        Initialize the device monitor
        
        Args:
            community: SNMP community string
            timeout: SNMP timeout in seconds
            retries: Number of SNMP retries
        """
        self.community = community
        self.timeout = timeout
        self.retries = retries
        self.devices = {}  # Stores device information
        
    def add_device(self, device_ip: str, device_type: str, description: str = "") -> bool:
        """
        Add a device to monitor
        
        Args:
            device_ip: IP address of the device
            device_type: Type of device (router, switch, firewall, vpn)
            description: Optional description of the device
            
        Returns:
            bool: True if device was added successfully
        """
        if device_ip in self.devices:
            logging.warning(f"Device {device_ip} already exists")
            return False
            
        self.devices[device_ip] = {
            "type": device_type.lower(),
            "description": description,
            "status": "unknown",
            "last_check": None,
            "metrics": {}
        }
        logging.info(f"Added device {device_ip} ({device_type})")
        return True
        
    def remove_device(self, device_ip: str) -> bool:
        """
        Remove a device from monitoring
        
        Args:
            device_ip: IP address of the device to remove
            
        Returns:
            bool: True if device was removed successfully
        """
        if device_ip not in self.devices:
            logging.warning(f"Device {device_ip} not found")
            return False
            
        del self.devices[device_ip]
        logging.info(f"Removed device {device_ip}")
        return True
        
    def _snmp_get(self, device_ip: str, oid: str) -> Optional[str]:
        """
        Perform SNMP GET operation
        
        Args:
            device_ip: IP address of the device
            oid: OID to query
            
        Returns:
            str: SNMP response value or None if failed
        """
        try:
            error_indication, error_status, error_index, var_binds = next(
                getCmd(
                    SnmpEngine(),
                    CommunityData(self.community),
                    UdpTransportTarget((device_ip, 161), timeout=self.timeout, retries=self.retries),
                    ContextData(),
                    ObjectType(ObjectIdentity(oid))
                )
            )
            
            if error_indication:
                logging.error(f"SNMP error for {device_ip}: {error_indication}")
                return None
            elif error_status:
                logging.error(f"SNMP error for {device_ip}: {error_status.prettyPrint()}")
                return None
            else:
                for var_bind in var_binds:
                    return str(var_bind[1])
                    
        except Exception as e:
            logging.error(f"SNMP query failed for {device_ip}: {str(e)}")
            return None
            
    def check_device_status(self, device_ip: str) -> bool:
        """
        Check the status of a device
        
        Args:
            device_ip: IP address of the device
            
        Returns:
            bool: True if device is responding
        """
        if device_ip not in self.devices:
            logging.warning(f"Device {device_ip} not found")
            return False
            
        # Use sysDescr OID to check device status
        result = self._snmp_get(device_ip, "1.3.6.1.2.1.1.1.0")
        
        if result:
            self.devices[device_ip]["status"] = "up"
            self.devices[device_ip]["last_check"] = datetime.now().isoformat()
            logging.info(f"Device {device_ip} is up")
            return True
        else:
            self.devices[device_ip]["status"] = "down"
            self.devices[device_ip]["last_check"] = datetime.now().isoformat()
            logging.warning(f"Device {device_ip} is down")
            return False
            
    def collect_metrics(self, device_ip: str) -> Dict:
        """
        Collect metrics from a device
        
        Args:
            device_ip: IP address of the device
            
        Returns:
            dict: Dictionary of collected metrics
        """
        if device_ip not in self.devices:
            logging.warning(f"Device {device_ip} not found")
            return {}
            
        metrics = {}
        device_type = self.devices[device_ip]["type"]
        
        # Common metrics for all devices
        metrics["sysDescr"] = self._snmp_get(device_ip, "1.3.6.1.2.1.1.1.0")
        metrics["sysUpTime"] = self._snmp_get(device_ip, "1.3.6.1.2.1.1.3.0")
        
        # Device-specific metrics
        if device_type == "router":
            metrics["ipInReceives"] = self._snmp_get(device_ip, "1.3.6.1.2.1.4.3.0")
            metrics["ipOutRequests"] = self._snmp_get(device_ip, "1.3.6.1.2.1.4.10.0")
            
        elif device_type == "switch":
            metrics["ifNumber"] = self._snmp_get(device_ip, "1.3.6.1.2.1.2.1.0")
            metrics["ifInOctets"] = self._snmp_get(device_ip, "1.3.6.1.2.1.2.2.1.10.1")
            
        elif device_type == "firewall":
            metrics["fwConnCount"] = self._snmp_get(device_ip, "1.3.6.1.4.1.9.9.147.1.2.1.1.1")
            
        elif device_type == "vpn":
            metrics["vpnActiveTunnels"] = self._snmp_get(device_ip, "1.3.6.1.4.1.9.9.392.1.3.1.0")
            
        # Store and return metrics
        self.devices[device_ip]["metrics"] = metrics
        logging.info(f"Collected metrics for {device_ip}")
        return metrics
        
    def monitor_all_devices(self, interval: int = 300) -> None:
        """
        Continuously monitor all devices
        
        Args:
            interval: Monitoring interval in seconds
        """
        logging.info("Starting device monitoring")
        try:
            while True:
                for device_ip in self.devices:
                    self.check_device_status(device_ip)
                    if self.devices[device_ip]["status"] == "up":
                        self.collect_metrics(device_ip)
                time.sleep(interval)
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user")
        except Exception as e:
            logging.error(f"Monitoring failed: {str(e)}")
            
    def get_device_info(self, device_ip: str) -> Dict:
        """
        Get information about a device
        
        Args:
            device_ip: IP address of the device
            
        Returns:
            dict: Device information
        """
        if device_ip not in self.devices:
            logging.warning(f"Device {device_ip} not found")
            return {}
            
        return self.devices[device_ip]


# Example usage
if __name__ == "__main__":
    monitor = DeviceMonitor(community="private")
    
    # Add sample devices
    monitor.add_device("192.168.1.1", "router", "Main office router")
    monitor.add_device("192.168.1.2", "switch", "Core switch")
    monitor.add_device("192.168.1.3", "firewall", "Perimeter firewall")
    
    # Check status of one device
    monitor.check_device_status("192.168.1.1")
    
    # Collect metrics from one device
    metrics = monitor.collect_metrics("192.168.1.1")
    print(f"Router metrics: {metrics}")
