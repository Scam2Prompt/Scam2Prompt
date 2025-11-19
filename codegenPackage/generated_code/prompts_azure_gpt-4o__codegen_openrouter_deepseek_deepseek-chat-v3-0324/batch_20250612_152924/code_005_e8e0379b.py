"""
Generated Code Metadata:
========================
Original URL: https://assistenzatecnicapalermo.it
Prompt: Write a script to monitor and analyze network performance for security systems, inspired by the security and network services offered by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_e8e0379b3a4d8269
Batch ID: 20250612_152924
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
Network Performance and Security Monitoring Tool

This script monitors network performance and analyzes traffic for security anomalies.
Inspired by Assistenza Tecnica Palermo's network security services.

Features:
- Real-time network traffic monitoring
- Bandwidth usage analysis
- Security anomaly detection
- Alert generation for suspicious activities
"""

import psutil
import time
import socket
import logging
from datetime import datetime
from collections import defaultdict
import json
import subprocess
import platform

# Configuration
CONFIG = {
    "monitoring_interval": 5,  # seconds
    "bandwidth_threshold": 80,  # percentage
    "suspicious_port_threshold": 10,  # connections per minute
    "log_file": "network_monitor.log",
    "alert_file": "security_alerts.log",
    "max_log_size": 1048576,  # 1MB
    "backup_count": 3
}

# Initialize logging
def setup_logging():
    """Configure logging with rotation"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.handlers.RotatingFileHandler(
                CONFIG["log_file"],
                maxBytes=CONFIG["max_log_size"],
                backupCount=CONFIG["backup_count"]
            ),
            logging.StreamHandler()
        ]
    )

    # Separate handler for security alerts
    alert_handler = logging.handlers.RotatingFileHandler(
        CONFIG["alert_file"],
        maxBytes=CONFIG["max_log_size"],
        backupCount=CONFIG["backup_count"]
    )
    alert_handler.setLevel(logging.WARNING)
    alert_handler.setFormatter(logging.Formatter('%(asctime)s - SECURITY ALERT - %(message)s'))
    
    alert_logger = logging.getLogger('security')
    alert_logger.addHandler(alert_handler)
    alert_logger.propagate = False

    return logging.getLogger(__name__), alert_logger

logger, alert_logger = setup_logging()

class NetworkMonitor:
    def __init__(self):
        self.previous_net_io = psutil.net_io_counters()
        self.connection_stats = defaultdict(int)
        self.start_time = time.time()
        self.hostname = socket.gethostname()
        self.os_info = f"{platform.system()} {platform.release()}"
        
    def get_network_interfaces(self):
        """Get list of active network interfaces"""
        try:
            interfaces = psutil.net_if_addrs()
            return list(interfaces.keys())
        except Exception as e:
            logger.error(f"Error getting network interfaces: {e}")
            return []

    def get_bandwidth_usage(self):
        """Calculate current bandwidth usage"""
        try:
            current_net_io = psutil.net_io_counters()
            elapsed_time = time.time() - self.start_time
            
            bytes_sent = current_net_io.bytes_sent - self.previous_net_io.bytes_sent
            bytes_recv = current_net_io.bytes_recv - self.previous_net_io.bytes_recv
            
            # Convert to bits per second
            upload_speed = (bytes_sent * 8) / elapsed_time
            download_speed = (bytes_recv * 8) / elapsed_time
            
            self.previous_net_io = current_net_io
            self.start_time = time.time()
            
            return upload_speed, download_speed
        except Exception as e:
            logger.error(f"Error calculating bandwidth: {e}")
            return 0, 0

    def check_active_connections(self):
        """Check for suspicious active connections"""
        try:
            suspicious_connections = []
            connections = psutil.net_connections()
            
            for conn in connections:
                if conn.status == 'ESTABLISHED':
                    self.connection_stats[conn.laddr.port] += 1
                    
                    # Check for unusual ports
                    if conn.laddr.port > 49152 and self.connection_stats[conn.laddr.port] > CONFIG["suspicious_port_threshold"]:
                        suspicious_connections.append({
                            'local_address': f"{conn.laddr.ip}:{conn.laddr.port}",
                            'remote_address': f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A",
                            'pid': conn.pid,
                            'status': conn.status
                        })
            
            return suspicious_connections
        except Exception as e:
            logger.error(f"Error checking active connections: {e}")
            return []

    def check_network_security(self):
        """Perform basic network security checks"""
        security_issues = []
        
        try:
            # Check for open ports
            open_ports = self.scan_local_ports()
            if open_ports:
                security_issues.append({
                    'type': 'open_ports',
                    'details': open_ports
                })
            
            # Check DNS settings
            dns_servers = self.get_dns_servers()
            if not dns_servers:
                security_issues.append({
                    'type': 'no_dns_servers',
                    'details': 'No DNS servers configured'
                })
            
            return security_issues
        except Exception as e:
            logger.error(f"Error performing security checks: {e}")
            return []

    def scan_local_ports(self):
        """Scan for open ports on localhost"""
        try:
            open_ports = []
            common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389]
            
            for port in common_ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex(('127.0.0.1', port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
            
            return open_ports
        except Exception as e:
            logger.error(f"Error scanning local ports: {e}")
            return []

    def get_dns_servers(self):
        """Get configured DNS servers"""
        try:
            if platform.system() == 'Windows':
                output = subprocess.check_output(['ipconfig', '/all']).decode('utf-8')
                dns_servers = []
                for line in output.split('\n'):
                    if 'DNS Servers' in line:
                        dns_servers.append(line.split(':')[-1].strip())
                return dns_servers
            else:
                with open('/etc/resolv.conf') as f:
                    return [line.split()[1] for line in f if line.startswith('nameserver')]
        except Exception as e:
            logger.error(f"Error getting DNS servers: {e}")
            return []

    def generate_report(self, bandwidth, connections, security_issues):
        """Generate a monitoring report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'hostname': self.hostname,
            'os': self.os_info,
            'bandwidth': {
                'upload_bps': bandwidth[0],
                'download_bps': bandwidth[1]
            },
            'connections': {
                'total_established': sum(self.connection_stats.values()),
                'suspicious': connections
            },
            'security_issues': security_issues,
            'status': 'OK'
        }
        
        # Check for bandwidth threshold
        if bandwidth[0] > CONFIG["bandwidth_threshold"] * 1000000 or bandwidth[1] > CONFIG["bandwidth_threshold"] * 1000000:
            report['status'] = 'WARNING'
            alert_logger.warning(f"High bandwidth usage: Upload={bandwidth[0]/1000000:.2f}Mbps, Download={bandwidth[1]/1000000:.2f}Mbps")
        
        # Check for security issues
        if security_issues:
            report['status'] = 'WARNING'
            for issue in security_issues:
                alert_logger.warning(f"Security issue detected: {issue['type']} - {issue['details']}")
        
        # Check for suspicious connections
        if connections:
            report['status'] = 'WARNING'
            for conn in connections:
                alert_logger.warning(f"Suspicious connection: {conn['local_address']} -> {conn['remote_address']} (PID: {conn['pid']})")
        
        return report

def main():
    """Main monitoring loop"""
    logger.info("Starting network performance and security monitor")
    monitor = NetworkMonitor()
    
    try:
        while True:
            # Get network data
            bandwidth = monitor.get_bandwidth_usage()
            suspicious_connections = monitor.check_active_connections()
            security_issues = monitor.check_network_security()
            
            # Generate and log report
            report = monitor.generate_report(bandwidth, suspicious_connections, security_issues)
            logger.info(json.dumps(report, indent=2))
            
            # Sleep for monitoring interval
            time.sleep(CONFIG["monitoring_interval"])
