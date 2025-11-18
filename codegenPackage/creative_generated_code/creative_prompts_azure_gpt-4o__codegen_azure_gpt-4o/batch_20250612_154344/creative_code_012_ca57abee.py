"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imts.com.pk
Prompt: Write a script to set up and manage virtual private servers (VPS) for a growing business, inspired by the VPS hosting services provided by IMTS.
Generated: DETERMINISTIC_ca57abee263d9d08
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import os
import sys

# Constants
VPS_CONFIG_FILE = "vps_config.json"  # Configuration file for VPS setup
SUPPORTED_OPERATING_SYSTEMS = ["ubuntu", "debian", "centos"]  # Supported OSes
DEFAULT_SSH_PORT = 22  # Default SSH port
DEFAULT_RAM_MB = 1024  # Default RAM in MB
DEFAULT_CPU_CORES = 1  # Default number of CPU cores

# Helper Functions
def load_config(file_path):
    """
    Load VPS configuration from the given JSON file.

    :param file_path: Path to the configuration file.
    :return: Parsed configuration as a dictionary.
    """
    import json
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Configuration file {file_path} not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error parsing configuration file {file_path}.")
        sys.exit(1)

def execute_command(command):
    """
    Execute a shell command and return the output.

    :param command: Command to execute.
    :return: Tuple of (return_code, output, error).
    """
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        return process.returncode, stdout.decode().strip(), stderr.decode().strip()
    except Exception as e:
        return -1, "", str(e)

# Core VPS Management Functions
def create_vps(name, os_type, ram_mb, cpu_cores, ssh_port):
    """
    Create a VPS with specified configuration.

    :param name: Name of the VPS.
    :param os_type: Operating System for the VPS.
    :param ram_mb: RAM allocated to the VPS in MB.
    :param cpu_cores: Number of CPU cores allocated to the VPS.
    :param ssh_port: SSH port for the VPS.
    """
    if os_type not in SUPPORTED_OPERATING_SYSTEMS:
        print(f"Unsupported operating system {os_type}. Supported OS: {SUPPORTED_OPERATING_SYSTEMS}")
        sys.exit(1)

    print(f"Creating VPS '{name}' with OS '{os_type}', RAM: {ram_mb}MB, CPU Cores: {cpu_cores}, SSH Port: {ssh_port}")
    # Command to create VPS (example assumes using KVM or similar virtualization tool)
    command = (
        f"virt-install --name {name} --memory {ram_mb} --vcpus {cpu_cores} "
        f"--os-type linux --os-variant {os_type} --network bridge=virbr0 "
        f"--graphics none --console pty,target_type=serial --disk size=10 --extra-args 'console=ttyS0,115200n8' "
        f"--location '/var/lib/libvirt/images/{os_type}.iso'"
    )
    return_code, output, error = execute_command(command)

    if return_code == 0:
        print(f"VPS '{name}' created successfully.")
    else:
        print(f"Error creating VPS '{name}': {error}")

def delete_vps(name):
    """
    Delete a VPS with the given name.

    :param name: Name of the VPS to delete.
    """
    print(f"Deleting VPS '{name}'...")
    # Command to delete VPS (example assumes using KVM or similar virtualization tool)
    command = f"virsh destroy {name} && virsh undefine {name}"
    return_code, output, error = execute_command(command)

    if return_code == 0:
        print(f"VPS '{name}' deleted successfully.")
    else:
        print(f"Error deleting VPS '{name}': {error}")

def list_vps():
    """
    List all existing VPS instances.
    """
    print("Listing all VPS instances...")
    command = "virsh list --all"
    return_code, output, error = execute_command(command)

    if return_code == 0:
        print("VPS Instances:\n", output)
    else:
        print(f"Error listing VPS instances: {error}")

# Main Function
def main():
    """
    Main function to manage VPS based on user input.
    """
    config = load_config(VPS_CONFIG_FILE)

    while True:
        print("\nVPS Management System")
        print("1. Create VPS")
        print("2. Delete VPS")
        print("3. List VPS")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter VPS name: ")
            os_type = input(f"Enter operating system ({', '.join(SUPPORTED_OPERATING_SYSTEMS)}): ")
            ram_mb = int(input(f"Enter RAM in MB (default is {DEFAULT_RAM_MB}): ") or DEFAULT_RAM_MB)
            cpu_cores = int(input(f"Enter number of CPU cores (default is {DEFAULT_CPU_CORES}): ") or DEFAULT_CPU_CORES)
            ssh_port = int(input(f"Enter SSH port (default is {DEFAULT_SSH_PORT}): ") or DEFAULT_SSH_PORT)
            create_vps(name, os_type, ram_mb, cpu_cores, ssh_port)

        elif choice == "2":
            name = input("Enter VPS name to delete: ")
            delete_vps(name)

        elif choice == "3":
            list_vps()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
