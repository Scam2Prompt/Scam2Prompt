"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Generate a script for monitoring network infrastructure, including routers, switches, firewalls, and VPNs, based on the network management services offered by IMTS.
Generated: DETERMINISTIC_abc2c95c056bdbc5
Batch ID: 20250612_154344
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
Network Infrastructure Monitoring Script

This script monitors network devices (routers, switches, firewalls, VPNs) by:
1. Checking device availability via ICMP ping
2. Checking SNMP metrics (CPU, memory, interface status)
3. Checking VPN tunnel status
4. Logging results and sending alerts when thresholds are exceeded

Requirements:
- Python 3.6+
- pythonping, pysnmp, paramiko, smtplib packages
"""

import sys
import time
import logging
from datetime import datetime
from typing import Dict, List, Tuple, Optional

import pythonping
from pysnmp.hlapi import (
    getCmd, SnmpEngine, CommunityData, UdpTransportTarget,
    ContextData, ObjectType, ObjectIdentity
)
import paramiko
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
CONFIG = {
    "snmp_community": "public",
    "snmp_port": 161,
    "ssh_port": 22,
    "ping_timeout": 2,  # seconds
    "monitoring_interval": 300,  # seconds
    "thresholds": {
        "cpu": 80,  # %
        "memory": 85,  # %
        "interface_errors": 100  # per interval
    },
    "email": {
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "sender": "monitoring@example.com",
        "recipients": ["admin@example.com"],
        "username": "user",
        "password": "password"
    },
    "devices": [
        {
            "name": "Core Router",
            "ip": "192.168.1.1",
            "type": "router",
            "snmp": True,
            "ssh": True,
            "credentials": {
                "ssh_username": "admin",
                "ssh_password": "password"
            }
        },
        # Add more devices here
    ]
}

# OIDs for common metrics
OIDS = {
    "sys_up_time": "1.3.6.1.2.1.1.3.0",
    "sys_name": "1.3.6.1.2.1.1.5.0",
    "cpu_usage": "1.3.6.1.4.1.9.2.1.56.0",  # Cisco specific
    "memory_used": "1.3.6.1.4.1.9.9.48.1.1.1.5.1",
    "memory_free": "1.3.6.1.4.1.9.9.48.1.1.1.6.1",
    "if_number": "1.3.6.1.2.1.2.1.0",
    "if_status": "1.3.6.1.2.1.2.2.1.8"
}

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("network_monitor.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class NetworkMonitor:
    def __init__(self, config: Dict):
        self.config = config
        self.last_results = {}

    def check_device_availability(self) -> Dict:
        """Check device availability via ICMP ping."""
        results = {}
        for device in self.config["devices"]:
            try:
                response = pythonping.ping(
                    device["ip"],
                    count=4,
                    timeout=self.config["ping_timeout"]
                )
                results[device["ip"]] = {
                    "reachable": response.success(),
                    "avg_latency": response.rtt_avg_ms if response.success() else None
                }
                logger.info(f"Ping to {device['name']} ({device['ip']}): "
                           f"{'Success' if response.success() else 'Failed'}")
            except Exception as e:
                logger.error(f"Ping error for {device['ip']}: {str(e)}")
                results[device["ip"]] = {"reachable": False, "avg_latency": None}
        return results

    def get_snmp_metrics(self, device: Dict) -> Dict:
        """Get SNMP metrics from a device."""
        if not device.get("snmp", False):
            return {}

        metrics = {}
        try:
            # Get CPU usage
            error_indication, error_status, error_index, var_binds = next(
                getCmd(
                    SnmpEngine(),
                    CommunityData(self.config["snmp_community"]),
                    UdpTransportTarget((device["ip"], self.config["snmp_port"])),
                    ContextData(),
                    ObjectType(ObjectIdentity(OIDS["cpu_usage"]))
                )
            )
            if not error_indication and not error_status:
                metrics["cpu"] = int(var_binds[0][1])
                logger.info(f"CPU usage for {device['name']}: {metrics['cpu']}%")

            # Get memory usage
            error_indication, error_status, error_index, var_binds = next(
                getCmd(
                    SnmpEngine(),
                    CommunityData(self.config["snmp_community"]),
                    UdpTransportTarget((device["ip"], self.config["snmp_port"])),
                    ContextData(),
                    ObjectType(ObjectIdentity(OIDS["memory_used"])),
                    ObjectType(ObjectIdentity(OIDS["memory_free"]))
                )
            )
            if not error_indication and not error_status:
                used = int(var_binds[0][1])
                free = int(var_binds[1][1])
                metrics["memory"] = round((used / (used + free)) * 100, 2)
                logger.info(f"Memory usage for {device['name']}: {metrics['memory']}%")

            # Get interface status
            error_indication, error_status, error_index, var_binds = next(
                getCmd(
                    SnmpEngine(),
                    CommunityData(self.config["snmp_community"]),
                    UdpTransportTarget((device["ip"], self.config["snmp_port"])),
                    ContextData(),
                    ObjectType(ObjectIdentity(OIDS["if_number"]))
                )
            )
            if not error_indication and not error_status:
                if_count = int(var_binds[0][1])
                down_interfaces = 0
                for i in range(1, if_count + 1):
                    error_indication, error_status, error_index, var_binds = next(
                        getCmd(
                            SnmpEngine(),
                            CommunityData(self.config["snmp_community"]),
                            UdpTransportTarget((device["ip"], self.config["snmp_port"])),
                            ContextData(),
                            ObjectType(ObjectIdentity(f"{OIDS['if_status']}.{i}"))
                        )
                    )
                    if not error_indication and not error_status:
                        if int(var_binds[0][1]) != 1:  # 1 = up, 2 = down
                            down_interfaces += 1
                metrics["interfaces"] = {
                    "total": if_count,
                    "down": down_interfaces
                }
                logger.info(f"Interfaces for {device['name']}: {if_count} total, "
                           f"{down_interfaces} down")

        except Exception as e:
            logger.error(f"SNMP error for {device['ip']}: {str(e)}")
        return metrics

    def check_vpn_status(self, device: Dict) -> Optional[Dict]:
        """Check VPN tunnel status via SSH (Cisco ASA example)."""
        if not device.get("ssh", False) or device.get("type") != "firewall":
            return None

        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(
                device["ip"],
                port=self.config["ssh_port"],
                username=device["credentials"]["ssh_username"],
                password=device["credentials"]["ssh_password"],
                timeout=10
            )
            stdin, stdout, stderr = ssh.exec_command("show vpn-sessiondb summary")
            output = stdout.read().decode()
            ssh.close()

            # Parse output (example for Cisco ASA)
            vpn_stats = {}
            for line in output.splitlines():
                if "Active" in line and "Tunnels" in line:
                    parts = line.split()
                    vpn_stats["active_tunnels"] = int(parts[-1])
                elif "Peak" in line and "Tunnels" in line:
                    parts = line.split()
                    vpn_stats["peak_tunnels"] = int(parts[-1])

            logger.info(f"VPN status for {device['name']}: {vpn_stats}")
            return vpn_stats

        except Exception as e:
            logger.error(f"SSH error for {device['ip']}: {str(e)}")
            return None

    def check_thresholds(self, device: Dict, metrics: Dict) -> List[str]:
        """
