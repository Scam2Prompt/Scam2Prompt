"""
Generated Code Metadata:
========================
Original URL: https://dudemine.com
Prompt: Develop a Python-based tool that mimics the functionality of the "dudeminecraft server problems diagnoser" from dudemine.com, with features for troubleshooting server crashes and latency issues.
Generated: DETERMINISTIC_5846a00348cd9a16
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import subprocess
import platform
import socket
import time
import psutil
import requests
from datetime import datetime

class MinecraftServerDiagnoser:
    """
    A tool to diagnose common Minecraft server problems such as crashes and latency issues.
    """
    
    def __init__(self):
        self.server_path = None
        self.server_log_path = None
        self.server_ip = None
        self.server_port = 25565
        self.timeout = 5  # seconds for network checks
        
    def set_server_path(self, path):
        """Set the path to the Minecraft server directory."""
        if os.path.isdir(path):
            self.server_path = path
            self.server_log_path = os.path.join(path, "logs", "latest.log")
            return True
        return False
    
    def set_server_address(self, ip, port=25565):
        """Set the server IP address and port."""
        self.server_ip = ip
        self.server_port = port
    
    def check_system_resources(self):
        """Check system resources (CPU, RAM, disk)."""
        results = {
            'cpu_usage': psutil.cpu_percent(interval=1),
            'ram_usage': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent
        }
        return results
    
    def check_network_latency(self):
        """Check network latency to the server."""
        if not self.server_ip:
            return None
            
        try:
            start_time = time.time()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            sock.connect((self.server_ip, self.server_port))
            sock.close()
            latency = (time.time() - start_time) * 1000  # in milliseconds
            return latency
        except Exception as e:
            return None
    
    def check_server_status(self):
        """Check if the server process is running."""
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            if 'java' in proc.info['name'].lower():
                if 'minecraft' in ' '.join(proc.info['cmdline']).lower():
                    return True
        return False
    
    def analyze_logs(self):
        """Analyze server logs for common errors."""
        if not self.server_log_path or not os.path.exists(self.server_log_path):
            return None
            
        common_errors = [
            'OutOfMemoryError',
            'Exception',
            'Error',
            'Crash',
            'Timeout',
            'Failed',
            'Disconnected'
        ]
        
        found_errors = []
        
        try:
            with open(self.server_log_path, 'r', encoding='utf-8', errors='ignore') as log_file:
                for line in log_file:
                    for error in common_errors:
                        if error in line:
                            found_errors.append(line.strip())
                            break
        except Exception as e:
            return None
            
        return found_errors if found_errors else None
    
    def check_port_status(self):
        """Check if the server port is open."""
        if not self.server_ip:
            return None
            
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.server_ip, self.server_port))
            sock.close()
            return result == 0
        except Exception as e:
            return None
    
    def check_java_version(self):
        """Check installed Java version."""
        try:
            result = subprocess.run(['java', '-version'], stderr=subprocess.PIPE, text=True)
            version_info = result.stderr.split('\n')[0]
            return version_info
        except Exception as e:
            return None
    
    def generate_report(self):
        """Generate a comprehensive diagnostic report."""
        report = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'system': {
                'os': platform.system(),
                'os_version': platform.version(),
                'python_version': platform.python_version()
            },
            'server_status': self.check_server_status(),
            'system_resources': self.check_system_resources(),
            'network': {
                'latency_ms': self.check_network_latency(),
                'port_open': self.check_port_status()
            },
            'java_version': self.check_java_version(),
            'log_errors': self.analyze_logs()
        }
        return report
    
    def print_report(self, report):
        """Print the diagnostic report in a readable format."""
        print("\n=== Minecraft Server Diagnostic Report ===")
        print(f"Generated at: {report['timestamp']}")
        print(f"\nSystem Information:")
        print(f"- OS: {report['system']['os']} {report['system']['os_version']}")
        print(f"- Python: {report['system']['python_version']}")
        
        print("\nServer Status:")
        print(f"- Running: {'Yes' if report['server_status'] else 'No'}")
        
        print("\nSystem Resources:")
        res = report['system_resources']
        print(f"- CPU Usage: {res['cpu_usage']}%")
        print(f"- RAM Usage: {res['ram_usage']}%")
        print(f"- Disk Usage: {res['disk_usage']}%")
        
        print("\nNetwork Information:")
        net = report['network']
        print(f"- Latency: {net['latency_ms']:.2f} ms" if net['latency_ms'] else "- Latency: Could not measure")
        print(f"- Port {self.server_port}: {'Open' if net['port_open'] else 'Closed' if net['port_open'] is not None else 'Unknown'}")
        
        print("\nJava Version:")
        print(f"- {report['java_version']}" if report['java_version'] else "- Could not determine Java version")
        
        print("\nLog Errors Found:")
        if report['log_errors']:
            for error in report['log_errors']:
                print(f"- {error}")
        else:
            print("- No significant errors found in logs or logs unavailable")

def main():
    diagnoser = MinecraftServerDiagnoser()
    
    print("Minecraft Server Diagnostic Tool")
    print("--------------------------------")
    
    # Get server path
    while True:
        path = input("Enter path to your Minecraft server directory (or leave blank to skip): ").strip()
        if not path:
            break
        if diagnoser.set_server_path(path):
            break
        print("Invalid path. Please try again.")
    
    # Get server address
    while True:
        ip = input("Enter server IP (or leave blank for localhost): ").strip() or "127.0.0.1"
        port = input(f"Enter server port (default 25565): ").strip()
        try:
            port = int(port) if port else 25565
            diagnoser.set_server_address(ip, port)
            break
        except ValueError:
            print("Invalid port number. Please try again.")
    
    print("\nRunning diagnostics...")
    report = diagnoser.generate_report()
    diagnoser.print_report(report)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nDiagnostic cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        sys.exit(1)
```
