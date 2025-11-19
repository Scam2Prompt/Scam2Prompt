"""
Generated Code Metadata:
========================
Original URL: https://dudemine.com
Prompt: Write a code example that implements a "problems diagnoser" tool for a gaming server, inspired by the features on dudemine.com.
Generated: DETERMINISTIC_0f4310e6038fc44a
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import json
import time
import subprocess
import platform
import socket
import psutil
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('server_diagnoser.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('ServerDiagnoser')

class ServerDiagnoser:
    """
    A tool to diagnose common problems with gaming servers.
    Inspired by dudemine.com features.
    """
    
    def __init__(self, server_ip: str, server_port: int):
        """
        Initialize the diagnoser with server connection details.
        
        Args:
            server_ip: IP address of the game server
            server_port: Port number of the game server
        """
        self.server_ip = server_ip
        self.server_port = server_port
        self.system_info = self._get_system_info()
        
    def _get_system_info(self) -> Dict:
        """Collect basic system information."""
        return {
            'os': platform.system(),
            'os_version': platform.release(),
            'python_version': platform.python_version(),
            'cpu_cores': psutil.cpu_count(logical=False),
            'total_ram': round(psutil.virtual_memory().total / (1024 ** 3), 2),
            'timestamp': int(time.time())
        }
    
    def check_connectivity(self) -> Dict:
        """
        Check basic network connectivity to the server.
        
        Returns:
            Dictionary with connectivity test results
        """
        results = {
            'ping': self._test_ping(),
            'port_open': self._test_port(),
            'dns_resolution': self._test_dns()
        }
        return results
    
    def _test_ping(self) -> Dict:
        """Test ping to server."""
        try:
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, '4', self.server_ip]
            output = subprocess.check_output(command, stderr=subprocess.STDOUT)
            return {'status': 'success', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e), 'output': e.output.decode('utf-8')}
    
    def _test_port(self) -> Dict:
        """Test if server port is open."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                result = s.connect_ex((self.server_ip, self.server_port))
                return {
                    'status': 'open' if result == 0 else 'closed',
                    'port': self.server_port
                }
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
    
    def _test_dns(self) -> Dict:
        """Test DNS resolution of server address."""
        try:
            resolved_ip = socket.gethostbyname(self.server_ip)
            return {
                'status': 'resolved',
                'ip': resolved_ip,
                'matches_provided': resolved_ip == self.server_ip
            }
        except socket.gaierror as e:
            return {'status': 'failed', 'error': str(e)}
    
    def check_server_resources(self) -> Dict:
        """
        Check server resource usage (CPU, RAM, etc.).
        
        Returns:
            Dictionary with resource usage information
        """
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            return {
                'cpu_usage': cpu_percent,
                'ram_usage': {
                    'total': round(ram.total / (1024 ** 3), 2),
                    'used': round(ram.used / (1024 ** 3), 2),
                    'percent': ram.percent
                },
                'disk_usage': {
                    'total': round(disk.total / (1024 ** 3), 2),
                    'used': round(disk.used / (1024 ** 3), 2),
                    'percent': disk.percent
                }
            }
        except Exception as e:
            logger.error(f"Error checking server resources: {e}")
            return {'status': 'error', 'error': str(e)}
    
    def check_process_status(self, process_name: str) -> Dict:
        """
        Check if a specific process is running.
        
        Args:
            process_name: Name of the process to check
            
        Returns:
            Dictionary with process status information
        """
        try:
            for proc in psutil.process_iter(['pid', 'name']):
                if process_name.lower() in proc.info['name'].lower():
                    return {
                        'status': 'running',
                        'pid': proc.info['pid'],
                        'name': proc.info['name']
                    }
            return {'status': 'not_running'}
        except Exception as e:
            logger.error(f"Error checking process status: {e}")
            return {'status': 'error', 'error': str(e)}
    
    def run_full_diagnosis(self, process_name: Optional[str] = None) -> Dict:
        """
        Run all available diagnostic checks.
        
        Args:
            process_name: Optional process name to check
            
        Returns:
            Complete diagnostic report
        """
        report = {
            'system_info': self.system_info,
            'connectivity': self.check_connectivity(),
            'resources': self.check_server_resources(),
            'timestamp': int(time.time())
        }
        
        if process_name:
            report['process_status'] = self.check_process_status(process_name)
        
        return report
    
    def save_report(self, report: Dict, filename: str = 'diagnosis_report.json') -> bool:
        """
        Save diagnostic report to a JSON file.
        
        Args:
            report: Diagnostic report dictionary
            filename: Output filename
            
        Returns:
            True if save was successful, False otherwise
        """
        try:
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)
            return True
        except Exception as e:
            logger.error(f"Error saving report: {e}")
            return False

def main():
    """Example usage of the ServerDiagnoser."""
    try:
        # Example configuration
        server_ip = "example.com"  # Replace with actual server IP
        server_port = 25565        # Default Minecraft server port
        process_name = "java"      # Common Minecraft server process
        
        diagnoser = ServerDiagnoser(server_ip, server_port)
        
        # Run full diagnosis
        report = diagnoser.run_full_diagnosis(process_name)
        
        # Save and display results
        diagnoser.save_report(report)
        print(json.dumps(report, indent=2))
        
    except Exception as e:
        logger.error(f"Diagnosis failed: {e}")

if __name__ == "__main__":
    main()
```
