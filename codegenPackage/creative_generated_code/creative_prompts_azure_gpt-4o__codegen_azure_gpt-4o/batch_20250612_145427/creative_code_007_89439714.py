"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-ebh.net
Prompt: Generate a script to deploy CentOS on a virtual machine, ensuring compatibility with Red Hat Enterprise Linux configurations.
Generated: DETERMINISTIC_894397143bdd37fa
Batch ID: 20250612_145427
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
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_command(command, error_message):
    """
    Run a command using subprocess and handle errors gracefully.

    Args:
        command (list): Command to run as a list of strings.
        error_message (str): Error message to log if the command fails.

    Returns:
        str: The standard output of the command if successful.
    """
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        logging.info(f"Command succeeded: {' '.join(command)}")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"{error_message}. Error: {e.stderr.strip()}")
        raise

def validate_prerequisites():
    """
    Validate that the script is being run as root and that required tools are installed.
    """
    # Check if the script is run as root
    if os.geteuid() != 0:
        logging.error("This script must be run as root. Exiting.")
        raise PermissionError("Script must be run as root.")

    # Check if 'virt-install' and 'qemu-kvm' are installed
    required_tools = ['virt-install', 'qemu-kvm']
    for tool in required_tools:
        if not shutil.which(tool):
            logging.error(f"Required tool '{tool}' is not installed. Please install it and try again.")
            raise FileNotFoundError(f"Required tool '{tool}' is missing.")

def create_vm(config):
    """
    Create a virtual machine with CentOS.

    Args:
        config (dict): Configuration options for the virtual machine.
    """
    logging.info("Starting virtual machine creation process...")

    # Build the virt-install command
    command = [
        "virt-install",
        "--name", config['name'],
        "--vcpus", str(config['vcpus']),
        "--memory", str(config['memory']),
        "--disk", f"path={config['disk_path']},size={config['disk_size']}",
        "--os-variant", config['os_variant'],
        "--network", config['network'],
        "--graphics", config['graphics'],
        "--location", config['iso_path'],
        "--extra-args", config['extra_args']
    ]

    # Run the command
    run_command(command, "Failed to create the virtual machine.")
    logging.info("Virtual machine successfully created.")

def main():
    """
    Main entry point for the script to deploy CentOS on a virtual machine.
    """
    try:
        # Validate prerequisites
        validate_prerequisites()

        # Virtual machine configuration
        vm_config = {
            "name": "centos-vm",
            "vcpus": 2,
            "memory": 2048,  # RAM in MB
            "disk_path": "/var/lib/libvirt/images/centos-vm.qcow2",
            "disk_size": 20,  # Disk size in GB
            "os_variant": "centos8",  # Ensure this matches your CentOS version
            "network": "network=default",
            "graphics": "spice",
            "iso_path": "/path/to/centos.iso",  # Path to the CentOS ISO file
            "extra_args": "console=ttyS0,115200n8 serial"
        }

        # Ensure the disk path directory exists
        disk_dir = Path(vm_config['disk_path']).parent
        disk_dir.mkdir(parents=True, exist_ok=True)

        # Deploy the virtual machine
        create_vm(vm_config)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    main()
```

**Note**: Ensure to replace `/path/to/centos.iso` with the actual path to your CentOS ISO file.
