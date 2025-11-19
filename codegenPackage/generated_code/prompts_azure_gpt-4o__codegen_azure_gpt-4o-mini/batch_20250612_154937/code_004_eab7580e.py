"""
Generated Code Metadata:
========================
Original URL: https://marceldev.github.io
Prompt: Create a Python script that retrieves and displays kernel version information for use in a Discord Rich Presence integration, inspired by MarcelDev's project.
Generated: DETERMINISTIC_eab7580e31569cad
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import platform
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_kernel_version():
    """
    Retrieve the kernel version of the operating system.

    Returns:
        str: The kernel version as a string.
    """
    try:
        # Use the 'uname' command to get the kernel version
        kernel_version = subprocess.check_output(['uname', '-r'], text=True).strip()
        logging.info(f"Kernel version retrieved: {kernel_version}")
        return kernel_version
    except subprocess.CalledProcessError as e:
        logging.error(f"Error retrieving kernel version: {e}")
        return "Unknown Kernel Version"

def get_os_info():
    """
    Retrieve the operating system information.

    Returns:
        str: A formatted string containing the OS name and version.
    """
    os_name = platform.system()
    os_version = platform.version()
    os_info = f"{os_name} {os_version}"
    logging.info(f"Operating system information retrieved: {os_info}")
    return os_info

def main():
    """
    Main function to retrieve and display kernel and OS information.
    This function can be extended for Discord Rich Presence integration.
    """
    kernel_version = get_kernel_version()
    os_info = get_os_info()

    # Display the information
    print(f"Kernel Version: {kernel_version}")
    print(f"Operating System: {os_info}")

if __name__ == "__main__":
    main()
```
