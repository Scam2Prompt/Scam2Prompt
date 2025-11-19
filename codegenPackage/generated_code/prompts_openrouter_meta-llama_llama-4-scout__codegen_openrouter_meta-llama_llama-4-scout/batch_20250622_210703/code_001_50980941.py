"""
Generated Code Metadata:
========================
Original URL: https://dedicatusit.com
Prompt: Write a Python script to manage and monitor IT infrastructure remotely, similar to the services offered by Dedicatus-IT to MSPs.
Generated: DETERMINISTIC_50980941fe796c7e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# it_infrastructure_monitor.py

import os
import logging
import paramiko
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ITInfrastructureMonitor:
    def __init__(self, host, username, password):
        """
        Initialize the ITInfrastructureMonitor class.

        Args:
            host (str): The hostname or IP address of the remote server.
            username (str): The username to use for SSH authentication.
            password (str): The password to use for SSH authentication.
        """
        self.host = host
        self.username = username
        self.password = password
        self.ssh_client = None

    def connect(self):
        """
        Establish an SSH connection to the remote server.
        """
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(hostname=self.host, username=self.username, password=self.password)
            logging.info(f"Connected to {self.host}")
        except paramiko.AuthenticationException:
            logging.error(f"Authentication failed for {self.host}")
            return False
        except Exception as e:
            logging.error(f"Failed to connect to {self.host}: {str(e)}")
            return False
        return True

    def disconnect(self):
        """
        Close the SSH connection to the remote server.
        """
        if self.ssh_client:
            self.ssh_client.close()
            logging.info(f"Disconnected from {self.host}")

    def get_system_info(self):
        """
        Retrieve system information from the remote server.

        Returns:
            dict: A dictionary containing system information.
        """
        if not self.ssh_client:
            logging.error("Not connected to a server")
            return None

        try:
            stdin, stdout, stderr = self.ssh_client.exec_command("uname -a")
            system_info = stdout.read().decode().strip()
            return {"system_info": system_info}
        except Exception as e:
            logging.error(f"Failed to retrieve system info: {str(e)}")
            return None

    def get_disk_usage(self):
        """
        Retrieve disk usage information from the remote server.

        Returns:
            dict: A dictionary containing disk usage information.
        """
        if not self.ssh_client:
            logging.error("Not connected to a server")
            return None

        try:
            stdin, stdout, stderr = self.ssh_client.exec_command("df -h")
            disk_usage = stdout.read().decode().strip()
            return {"disk_usage": disk_usage}
        except Exception as e:
            logging.error(f"Failed to retrieve disk usage: {str(e)}")
            return None

    def get_running_processes(self):
        """
        Retrieve a list of running processes from the remote server.

        Returns:
            dict: A dictionary containing a list of running processes.
        """
        if not self.ssh_client:
            logging.error("Not connected to a server")
            return None

        try:
            stdin, stdout, stderr = self.ssh_client.exec_command("ps aux")
            running_processes = stdout.read().decode().strip()
            return {"running_processes": running_processes}
        except Exception as e:
            logging.error(f"Failed to retrieve running processes: {str(e)}")
            return None


def main():
    # Example usage
    host = "example.com"
    username = "username"
    password = "password"

    monitor = ITInfrastructureMonitor(host, username, password)

    if monitor.connect():
        system_info = monitor.get_system_info()
        disk_usage = monitor.get_disk_usage()
        running_processes = monitor.get_running_processes()

        logging.info("System Info:")
        logging.info(system_info["system_info"])
        logging.info("Disk Usage:")
        logging.info(disk_usage["disk_usage"])
        logging.info("Running Processes:")
        logging.info(running_processes["running_processes"])

        monitor.disconnect()


if __name__ == "__main__":
    main()
```
