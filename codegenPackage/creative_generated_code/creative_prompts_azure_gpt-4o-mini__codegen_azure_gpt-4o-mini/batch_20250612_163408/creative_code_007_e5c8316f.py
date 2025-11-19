"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Develop a script that automates system administration tasks, utilizing the knowledge shared by Susan Lunn in the FOSS@RIT community.
Generated: DETERMINISTIC_e5c8316f373108e8
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_command(command):
    """
    Run a shell command and return the output.
    
    Args:
        command (str): The command to run in the shell.
    
    Returns:
        tuple: A tuple containing the exit code, stdout, and stderr.
    """
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        logging.info(f"Executed command: {command}")
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        logging.error(f"Error running command '{command}': {e}")
        return 1, '', str(e)

def check_disk_space():
    """
    Check the disk space usage and log the results.
    """
    logging.info("Checking disk space...")
    return_code, stdout, stderr = run_command("df -h")
    if return_code == 0:
        logging.info("Disk space usage:\n" + stdout)
    else:
        logging.error("Failed to check disk space:\n" + stderr)

def update_system():
    """
    Update the system packages.
    """
    logging.info("Updating system packages...")
    return_code, stdout, stderr = run_command("sudo apt-get update && sudo apt-get upgrade -y")
    if return_code == 0:
        logging.info("System packages updated successfully.")
    else:
        logging.error("Failed to update system packages:\n" + stderr)

def clean_temp_files():
    """
    Clean the temporary files to free up space.
    """
    logging.info("Cleaning temporary files...")
    return_code, stdout, stderr = run_command("sudo rm -rf /tmp/*")
    if return_code == 0:
        logging.info("Temporary files cleaned successfully.")
    else:
        logging.error("Failed to clean temporary files:\n" + stderr)

def main():
    """
    Main function to execute system administration tasks.
    """
    logging.info("Starting system administration tasks...")
    
    check_disk_space()
    update_system()
    clean_temp_files()

    logging.info("System administration tasks completed.")

if __name__ == "__main__":
    main()
```
