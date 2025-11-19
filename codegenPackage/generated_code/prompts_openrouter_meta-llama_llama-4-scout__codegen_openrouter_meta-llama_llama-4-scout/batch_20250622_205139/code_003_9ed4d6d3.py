"""
Generated Code Metadata:
========================
Original URL: https://openspa.info
Prompt: Develop a script to automate the process of updating OpenSPA firmware on an Octagon SF8008 receiver.
Generated: DETERMINISTIC_9ed4d6d381d71b29
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3

import os
import sys
import paramiko
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OpenSPAUpdater:
    def __init__(self, receiver_ip, username, password, firmware_file):
        self.receiver_ip = receiver_ip
        self.username = username
        self.password = password
        self.firmware_file = firmware_file

    def connect_to_receiver(self):
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(self.receiver_ip, username=self.username, password=self.password)
            logging.info(f"Connected to {self.receiver_ip}")
        except paramiko.AuthenticationException:
            logging.error("Authentication failed. Please check your credentials.")
            sys.exit(1)
        except paramiko.SSHException as ssh_exception:
            logging.error(f"Failed to connect to {self.receiver_ip}: {ssh_exception}")
            sys.exit(1)

    def update_firmware(self):
        try:
            # Copy firmware file to receiver
            sftp_client = self.ssh_client.open_sftp()
            sftp_client.put(self.firmware_file, "/tmp/firmware.tar.gz")
            sftp_client.close()
            logging.info(f"Firmware file copied to {self.receiver_ip}")
        except Exception as e:
            logging.error(f"Failed to copy firmware file: {e}")
            sys.exit(1)

        try:
            # Update firmware
            stdin, stdout, stderr = self.ssh_client.exec_command("opkg update && opkg install /tmp/firmware.tar.gz")
            stdout.channel.recv_exit_status()
            if stdout.channel.exit_status_ready() and stdout.channel.recv_exit_status() != 0:
                logging.error(f"Failed to update firmware: {stderr.read().decode('utf-8')}")
                sys.exit(1)
            logging.info("Firmware updated successfully")
        except Exception as e:
            logging.error(f"Failed to update firmware: {e}")
            sys.exit(1)

        try:
            # Reboot receiver
            stdin, stdout, stderr = self.ssh_client.exec_command("reboot")
            stdout.channel.recv_exit_status()
            logging.info("Receiver rebooted successfully")
        except Exception as e:
            logging.error(f"Failed to reboot receiver: {e}")
            sys.exit(1)

    def close_connection(self):
        self.ssh_client.close()
        logging.info(f"Disconnected from {self.receiver_ip}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        logging.error("Usage: python openSPA_updater.py <receiver_ip> <username> <password> <firmware_file>")
        sys.exit(1)

    receiver_ip = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    firmware_file = sys.argv[4]

    updater = OpenSPAUpdater(receiver_ip, username, password, firmware_file)
    updater.connect_to_receiver()
    updater.update_firmware()
    updater.close_connection()
```
