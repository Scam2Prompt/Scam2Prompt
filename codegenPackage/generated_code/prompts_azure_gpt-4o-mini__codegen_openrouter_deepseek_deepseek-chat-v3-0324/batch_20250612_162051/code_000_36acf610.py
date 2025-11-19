"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Generate a Python script that automates the process of diagnosing common computer issues, similar to the free diagnostics offered by Geeks on Repair.
Generated: DETERMINISTIC_36acf6103755747b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import platform
import subprocess
import psutil
import socket
import time
from datetime import datetime

class SystemDiagnostics:
    """
    A class to perform automated system diagnostics for common computer issues.
    """

    def __init__(self):
        """Initialize the diagnostics tool with system information."""
        self.system_info = {
            'os': platform.system(),
            'os_version': platform.version(),
            'hostname': socket.gethostname(),
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.report = {
            'system_info': self.system_info,
            'checks': []
        }

    def check_disk_space(self):
        """Check available disk space on all partitions."""
        try:
            partitions = psutil.disk_partitions()
            for partition in partitions:
                usage = psutil.disk_usage(partition.mountpoint)
                self.report['checks'].append({
                    'check': 'disk_space',
                    'partition': partition.device,
                    'total_gb': round(usage.total / (1024**3), 2),
                    'used_gb': round(usage.used / (1024**3), 2),
                    'free_gb': round(usage.free / (1024**3), 2),
                    'percent_used': usage.percent,
                    'status': 'warning' if usage.percent > 90 else 'ok'
                })
        except Exception as e:
            self._log_error('disk_space', str(e))

    def check_memory(self):
        """Check system memory usage."""
        try:
            mem = psutil.virtual_memory()
            self.report['checks'].append({
                'check': 'memory',
                'total_gb': round(mem.total / (1024**3), 2),
                'available_gb': round(mem.available / (1024**3), 2),
                'used_gb': round(mem.used / (1024**3), 2),
                'percent_used': mem.percent,
                'status': 'warning' if mem.percent > 90 else 'ok'
            })
        except Exception as e:
            self._log_error('memory', str(e))

    def check_cpu(self):
        """Check CPU usage."""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            self.report['checks'].append({
                'check': 'cpu',
                'usage_percent': cpu_percent,
                'status': 'warning' if cpu_percent > 90 else 'ok'
            })
        except Exception as e:
            self._log_error('cpu', str(e))

    def check_network(self):
        """Check basic network connectivity."""
        try:
            # Test DNS resolution
            socket.gethostbyname('google.com')
            dns_status = 'ok'
        except socket.gaierror:
            dns_status = 'error'

        try:
            # Test internet connectivity
            subprocess.check_output(['ping', '-c', '1', '8.8.8.8'], stderr=subprocess.STDOUT)
            ping_status = 'ok'
        except subprocess.CalledProcessError:
            ping_status = 'error'

        self.report['checks'].append({
            'check': 'network',
            'dns': dns_status,
            'internet': ping_status,
            'status': 'ok' if dns_status == 'ok' and ping_status == 'ok' else 'error'
        })

    def check_running_services(self):
        """Check status of common critical services."""
        services_to_check = []
        if self.system_info['os'] == 'Windows':
            services_to_check = ['Dhcp', 'Dnscache', 'Winmgmt']
        elif self.system_info['os'] == 'Linux':
            services_to_check = ['sshd', 'network-manager', 'dbus']

        for service in services_to_check:
            try:
                if self.system_info['os'] == 'Windows':
                    output = subprocess.check_output(
                        ['sc', 'query', service], stderr=subprocess.STDOUT
                    ).decode('utf-8', 'ignore')
                    status = 'running' if 'RUNNING' in output else 'stopped'
                else:
                    output = subprocess.check_output(
                        ['systemctl', 'is-active', service], stderr=subprocess.STDOUT
                    ).decode('utf-8', 'ignore').strip()
                    status = output if output in ['active', 'inactive'] else 'unknown'

                self.report['checks'].append({
                    'check': 'service',
                    'name': service,
                    'status': status,
                    'system_status': 'ok' if status in ['running', 'active'] else 'warning'
                })
            except Exception as e:
                self._log_error(f'service_{service}', str(e))

    def check_temperatures(self):
        """Check system temperatures if available."""
        try:
            if hasattr(psutil, 'sensors_temperatures'):
                temps = psutil.sensors_temperatures()
                for name, entries in temps.items():
                    for entry in entries:
                        self.report['checks'].append({
                            'check': 'temperature',
                            'sensor': name,
                            'current': entry.current,
                            'high': entry.high,
                            'critical': entry.critical,
                            'status': 'warning' if entry.current > entry.high else 'ok'
                        })
            else:
                self.report['checks'].append({
                    'check': 'temperature',
                    'status': 'not_available',
                    'message': 'Temperature sensors not available on this system'
                })
        except Exception as e:
            self._log_error('temperature', str(e))

    def _log_error(self, check_name, error_message):
        """Log an error that occurred during a check."""
        self.report['checks'].append({
            'check': check_name,
            'status': 'error',
            'error': error_message
        })

    def run_all_checks(self):
        """Run all available diagnostic checks."""
        self.check_disk_space()
        self.check_memory()
        self.check_cpu()
        self.check_network()
        self.check_running_services()
        self.check_temperatures()
        return self.report

    def generate_report(self, output_file=None):
        """Generate a human-readable report from the diagnostics."""
        report_lines = [
            f"System Diagnostics Report",
            f"Generated on: {self.system_info['timestamp']}",
            f"System: {self.system_info['os']} {self.system_info['os_version']}",
            f"Hostname: {self.system_info['hostname']}",
            "\nDiagnostic Results:",
            "=" * 50
        ]

        for check in self.report['checks']:
            report_lines.append(f"\nCheck: {check['check'].upper()}")
            for key, value in check.items():
                if key not in ['check', 'status']:
                    report_lines.append(f"  {key.replace('_', ' ').title()}: {value}")
            report_lines.append(f"  Status: {check['status'].upper()}")

        full_report = "\n".join(report_lines)

        if output_file:
            try:
                with open(output_file, 'w') as f:
                    f.write(full_report)
            except IOError as e:
                print(f"Error writing report to file: {e}")

        return full_report

def main():
    """Main function to run the diagnostics tool."""
    print("Running system diagnostics...")
    diagnostics = SystemDiagnostics()
    diagnostics.run_all_checks()
    report = diagnostics.generate_report()
    print(report)

    # Optionally save to file
    save_to_file = input("\nWould you like to save this report to a file? (y/n): ").lower()
    if save_to_file == 'y':
        default_filename = f"system_diagnostics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        filename = input(f"Enter filename (default: {default_filename}): ") or default_filename
        diagnostics.generate_report(filename)
        print(f"Report saved to {filename}")

if __name__ == "__main__":
    main()
```
