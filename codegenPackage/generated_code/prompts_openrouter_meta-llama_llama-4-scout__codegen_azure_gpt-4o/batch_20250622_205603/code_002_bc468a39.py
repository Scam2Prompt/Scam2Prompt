"""
Generated Code Metadata:
========================
Original URL: https://stethgift.org
Prompt: What are the best practices for troubleshooting Windows 10 boot issues, specifically the "Choose an Option" screen?
Generated: DETERMINISTIC_bc468a39527833a0
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is a Python script that automates troubleshooting Windows 10 boot issues, specifically targeting the "Choose an Option" screen. The script uses subprocess to execute commands and provides logging for diagnostics.

```python
import subprocess
import logging
import os

# Configure logging
LOG_FILE = "windows_boot_troubleshooting.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_command(command):
    """
    Run a system command and return the output.
    Logs errors if the command fails.
    """
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        logging.info(f"Command '{' '.join(command)}' executed successfully.")
        logging.info(f"Output: {result.stdout.strip()}")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing command '{' '.join(command)}': {e.stderr.strip()}")
        return None

def check_boot_configuration():
    """
    Check the boot configuration using bcdedit.
    """
    logging.info("Checking boot configuration...")
    return run_command(["bcdedit"])

def repair_boot_files():
    """
    Attempt to repair boot files using bootrec commands.
    """
    logging.info("Repairing boot files...")
    commands = [
        ["bootrec", "/fixmbr"],
        ["bootrec", "/fixboot"],
        ["bootrec", "/scanos"],
        ["bootrec", "/rebuildbcd"]
    ]
    for cmd in commands:
        run_command(cmd)

def check_disk_health():
    """
    Run chkdsk to check disk health.
    """
    logging.info("Checking disk health...")
    return run_command(["chkdsk", "C:", "/f", "/r"])

def reset_system_files():
    """
    Reset system files using DISM and SFC tools.
    """
    logging.info("Resetting system files...")
    # Run DISM to repair the Windows image
    run_command(["dism", "/online", "/cleanup-image", "/restorehealth"])
    # Run SFC to repair system files
    run_command(["sfc", "/scannow"])

def main():
    """
    Main function to troubleshoot Windows 10 boot issues.
    """
    logging.info("Starting Windows 10 boot troubleshooting...")
    
    # Step 1: Check boot configuration
    boot_config = check_boot_configuration()
    if boot_config:
        logging.info("Boot configuration retrieved successfully.")
    else:
        logging.warning("Failed to retrieve boot configuration.")

    # Step 2: Repair boot files
    logging.info("Attempting to repair boot files...")
    repair_boot_files()

    # Step 3: Check disk health
    logging.info("Checking disk health...")
    disk_health = check_disk_health()
    if disk_health:
        logging.info("Disk health check completed successfully.")
    else:
        logging.warning("Disk health check failed.")

    # Step 4: Reset system files
    logging.info("Resetting system files...")
    reset_system_files()

    logging.info("Windows 10 boot troubleshooting completed.")

if __name__ == "__main__":
    # Ensure the script is run with administrator privileges
    if os.name == "nt":
        try:
            # Check if the script is running as administrator
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
            if not is_admin:
                logging.error("This script must be run as an administrator.")
                print("Please run this script as an administrator.")
                exit(1)
        except Exception as e:
            logging.error(f"Error checking administrator privileges: {e}")
            print("Unable to verify administrator privileges.")
            exit(1)

    # Run the main troubleshooting function
    main()
```

### Key Features:
- **Logging**: Logs all actions and errors to a file for diagnostics.
- **Error Handling**: Captures and logs errors for each command.
- **Administrator Check**: Ensures the script is run with elevated privileges.
- **Modular Design**: Functions are modular and reusable.

Save this script as a `.py` file and run it on a Windows machine with Python installed. Ensure you execute it with administrator privileges for proper functionality.
