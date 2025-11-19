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
import os
import subprocess
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='system_admin_tasks.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_command(command):
    """
    Executes a shell command and returns the output.
    
    Args:
        command (str): The command to execute.
    
    Returns:
        str: The output of the command.
    
    Raises:
        RuntimeError: If the command fails to execute.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f"Executed command: {command}")
        return result.stdout.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {command} with error: {e.stderr.decode('utf-8').strip()}")
        raise RuntimeError(f"Command '{command}' failed with error: {e.stderr.decode('utf-8').strip()}")

def update_system():
    """Updates the system packages."""
    logging.info("Starting system update...")
    run_command("sudo apt update && sudo apt upgrade -y")
    logging.info("System update completed.")

def clean_system():
    """Cleans up unnecessary packages and files."""
    logging.info("Starting system cleanup...")
    run_command("sudo apt autoremove -y")
    run_command("sudo apt clean")
    logging.info("System cleanup completed.")

def check_disk_usage():
    """Checks and logs the disk usage."""
    logging.info("Checking disk usage...")
    disk_usage = run_command("df -h")
    logging.info(f"Disk usage:\n{disk_usage}")

def check_memory_usage():
    """Checks and logs the memory usage."""
    logging.info("Checking memory usage...")
    memory_usage = run_command("free -h")
    logging.info(f"Memory usage:\n{memory_usage}")

def main():
    """Main function to execute system administration tasks."""
    logging.info("Starting system administration tasks...")
    try:
        update_system()
        clean_system()
        check_disk_usage()
        check_memory_usage()
    except RuntimeError as e:
        logging.error(f"An error occurred during system administration tasks: {e}")
    logging.info("System administration tasks completed.")

if __name__ == "__main__":
    main()
```
