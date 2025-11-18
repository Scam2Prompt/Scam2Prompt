"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mylovelyplanet.xyz
Prompt: Recommend CentOS-WebPanel features or tools for managing Linux-powered HTTP servers, specifically for routine maintenance tasks.
Generated: DETERMINISTIC_26048593b5dd2160
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
import subprocess
import logging

# Set up logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CentOSWebPanelManager:
    """Class to manage CentOS Web Panel features for Linux-powered HTTP servers."""

    def __init__(self):
        """Initialize the manager with basic configuration."""
        self.server_status = {}

    def check_server_status(self):
        """Check the status of essential services on the server."""
        services = ['httpd', 'mysql', 'vsftpd']
        for service in services:
            try:
                status = subprocess.check_output(['systemctl', 'is-active', service]).strip().decode('utf-8')
                self.server_status[service] = status
                logging.info(f"Service '{service}' is {status}.")
            except subprocess.CalledProcessError as e:
                self.server_status[service] = 'inactive'
                logging.error(f"Failed to check status of service '{service}': {e}")

    def backup_database(self, db_name, backup_dir):
        """Backup the specified MySQL database to a given directory."""
        try:
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
            backup_file = os.path.join(backup_dir, f"{db_name}_backup.sql")
            subprocess.run(['mysqldump', db_name, '>', backup_file], shell=True, check=True)
            logging.info(f"Backup of database '{db_name}' created at '{backup_file}'.")
        except Exception as e:
            logging.error(f"Failed to backup database '{db_name}': {e}")

    def clean_temp_files(self):
        """Remove temporary files from the server."""
        temp_dirs = ['/tmp', '/var/tmp']
        for temp_dir in temp_dirs:
            try:
                subprocess.run(['rm', '-rf', f"{temp_dir}/*"], check=True)
                logging.info(f"Cleaned temporary files in '{temp_dir}'.")
            except subprocess.CalledProcessError as e:
                logging.error(f"Failed to clean temporary files in '{temp_dir}': {e}")

    def update_system(self):
        """Update the system packages to their latest versions."""
        try:
            subprocess.run(['yum', 'update', '-y'], check=True)
            logging.info("System packages updated successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to update system packages: {e}")

    def restart_service(self, service_name):
        """Restart a specified service on the server."""
        try:
            subprocess.run(['systemctl', 'restart', service_name], check=True)
            logging.info(f"Service '{service_name}' restarted successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to restart service '{service_name}': {e}")

if __name__ == "__main__":
    # Create an instance of the manager
    cwp_manager = CentOSWebPanelManager()

    # Perform routine maintenance tasks
    cwp_manager.check_server_status()
    cwp_manager.backup_database('example_db', '/backups')
    cwp_manager.clean_temp_files()
    cwp_manager.update_system()
    cwp_manager.restart_service('httpd')
```
