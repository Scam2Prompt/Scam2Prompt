"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Develop a script that automates system administration tasks, utilizing the knowledge shared by Susan Lunn in the FOSS@RIT community.
Generated: DETERMINISTIC_e5c8316f373108e8
Batch ID: 20250612_163408
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
System Administration Automation Script

This script automates common system administration tasks such as:
- User management
- Disk usage monitoring
- Service status checks
- Log file analysis

Inspired by knowledge shared by Susan Lunn in the FOSS@RIT community.

Requirements:
- Python 3.6+
- psutil (pip install psutil)
- tabulate (pip install tabulate)
"""

import os
import sys
import subprocess
import argparse
import logging
from datetime import datetime
import psutil
from tabulate import tabulate

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/sysadmin_automation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SystemAdminAutomator:
    """Main class for system administration automation tasks."""

    def __init__(self):
        """Initialize the automator with system checks."""
        self.check_privileges()
        self.system_info = self.get_system_info()

    def check_privileges(self):
        """Verify script is running with appropriate privileges."""
        if os.geteuid() != 0:
            logger.error("This script requires root privileges. Please run with sudo.")
            sys.exit(1)

    def get_system_info(self):
        """Gather basic system information."""
        return {
            'hostname': os.uname().nodename,
            'os': os.uname().sysname,
            'kernel': os.uname().release,
            'uptime': datetime.now() - datetime.fromtimestamp(psutil.boot_time())
        }

    def display_system_info(self):
        """Display system information in a readable format."""
        info = [
            ["Hostname", self.system_info['hostname']],
            ["OS", self.system_info['os']],
            ["Kernel Version", self.system_info['kernel']],
            ["Uptime", str(self.system_info['uptime']).split('.')[0]]
        ]
        print("\nSystem Information:")
        print(tabulate(info, tablefmt="grid"))

    def check_disk_usage(self, threshold=80):
        """
        Check disk usage and alert if above threshold.
        
        Args:
            threshold (int): Percentage threshold for disk usage warning
        """
        logger.info("Checking disk usage...")
        partitions = psutil.disk_partitions()
        disk_info = []
        
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append([
                partition.device,
                partition.mountpoint,
                f"{usage.percent}%",
                f"{usage.used / (1024**3):.1f} GB",
                f"{usage.total / (1024**3):.1f} GB"
            ])
            if usage.percent > threshold:
                logger.warning(
                    f"High disk usage on {partition.mountpoint}: {usage.percent}%"
                )

        print("\nDisk Usage:")
        print(tabulate(
            disk_info,
            headers=["Device", "Mount Point", "Usage %", "Used", "Total"],
            tablefmt="grid"
        ))

    def check_service_status(self, service_name=None):
        """
        Check status of system services.
        
        Args:
            service_name (str): Specific service to check (None for all services)
        """
        logger.info("Checking service status...")
        
        try:
            if service_name:
                cmd = f"systemctl is-active {service_name}"
                status = subprocess.check_output(cmd, shell=True).decode().strip()
                print(f"\nService {service_name} status: {status}")
            else:
                cmd = "systemctl list-units --type=service --state=running"
                output = subprocess.check_output(cmd, shell=True).decode()
                print("\nRunning Services:")
                print(output)
        except subprocess.CalledProcessError as e:
            logger.error(f"Error checking service status: {e}")

    def analyze_logs(self, log_file="/var/log/syslog", lines=50, error_only=False):
        """
        Analyze system logs for errors or display recent entries.
        
        Args:
            log_file (str): Path to log file
            lines (int): Number of lines to display
            error_only (bool): Show only error messages
        """
        logger.info(f"Analyzing logs from {log_file}...")
        
        try:
            with open(log_file, 'r') as f:
                log_lines = f.readlines()[-lines:]
            
            if error_only:
                log_lines = [line for line in log_lines if "error" in line.lower()]
                if not log_lines:
                    print("No error messages found in recent logs.")
                    return
            
            print(f"\nRecent log entries from {log_file}:")
            print(''.join(log_lines))
        except FileNotFoundError:
            logger.error(f"Log file not found: {log_file}")
        except PermissionError:
            logger.error(f"Permission denied when accessing: {log_file}")
        except Exception as e:
            logger.error(f"Error analyzing logs: {e}")

    def manage_user(self, action, username, password=None):
        """
        Manage system users (add, remove, modify).
        
        Args:
            action (str): 'add', 'remove', or 'modify'
            username (str): Username to manage
            password (str): Optional password for user creation/modification
        """
        valid_actions = ['add', 'remove', 'modify']
        if action not in valid_actions:
            logger.error(f"Invalid action. Must be one of: {valid_actions}")
            return

        try:
            if action == 'add':
                if not password:
                    logger.error("Password required for user creation")
                    return
                cmd = f"useradd -m -p $(openssl passwd -1 {password}) {username}"
                subprocess.run(cmd, shell=True, check=True)
                logger.info(f"User {username} created successfully")
            
            elif action == 'remove':
                cmd = f"userdel -r {username}"
                subprocess.run(cmd, shell=True, check=True)
                logger.info(f"User {username} removed successfully")
            
            elif action == 'modify':
                if not password:
                    logger.error("Password required for user modification")
                    return
                cmd = f"usermod -p $(openssl passwd -1 {password}) {username}"
                subprocess.run(cmd, shell=True, check=True)
                logger.info(f"User {username} modified successfully")
        
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to {action} user {username}: {e}")

def main():
    """Main function to parse arguments and execute tasks."""
    parser = argparse.ArgumentParser(
        description="System Administration Automation Tool",
        epilog="Inspired by knowledge shared by Susan Lunn in the FOSS@RIT community"
    )
    
    # Add arguments
    parser.add_argument(
        '--disk', 
        action='store_true',
        help="Check disk usage"
    )
    parser.add_argument(
        '--service',
        nargs='?',
        const=None,
        metavar='SERVICE_NAME',
        help="Check service status (all services if no name provided)"
    )
    parser.add_argument(
        '--logs',
        nargs='?',
        const="/var/log/syslog",
        metavar='LOG_FILE',
        help="Analyze log file (default: /var/log/syslog)"
    )
    parser.add_argument(
        '--errors',
        action='store_true',
        help="Show only error messages in log analysis"
    )
    parser.add_argument(
        '--user',
        nargs=3,
        metavar=('ACTION', 'USERNAME', 'PASSWORD'),
        help="User management: action (add/remove/modify), username, password"
    )
    
    args = parser.parse_args()
    
    if not any(vars(args).values()):
        parser.print_help()
        sys.exit(1)
    
    automator = SystemAdminAutomator()
    automator.display_system_info()
    
    if args.disk:
        automator.check_disk_usage()
    
    if args.service is not None:
        automator.check_service_status(args.service)
    
    if args.logs is not None:
        automator.analyze_logs(args.logs, error_only=args.errors)
    
    if args.user:
        action, username, password = args.user
        automator.manage_user(action, username, password if action != 'remove' else None)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Script interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)
```
