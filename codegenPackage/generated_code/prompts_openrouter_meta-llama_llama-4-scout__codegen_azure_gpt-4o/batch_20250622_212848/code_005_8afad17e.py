"""
Generated Code Metadata:
========================
Original URL: https://wfcomputing.com
Prompt: Write a script to automate the installation and configuration of a network printer on a Windows 10 PC.
Generated: DETERMINISTIC_8afad17e0b2e63f4
Batch ID: 20250622_212848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import sys

def install_network_printer(printer_name, printer_ip, driver_path):
    """
    Automates the installation and configuration of a network printer on a Windows 10 PC.

    Args:
        printer_name (str): The name to assign to the printer.
        printer_ip (str): The IP address of the network printer.
        driver_path (str): The path to the printer driver .inf file.

    Returns:
        None
    """
    try:
        # Step 1: Add the printer port
        print(f"Adding printer port for IP: {printer_ip}...")
        subprocess.run(
            [
                "powershell",
                "-Command",
                f"Add-PrinterPort -Name 'IP_{printer_ip}' -PrinterHostAddress '{printer_ip}'"
            ],
            check=True
        )
        print("Printer port added successfully.")

        # Step 2: Install the printer driver
        print(f"Installing printer driver from: {driver_path}...")
        subprocess.run(
            [
                "pnputil",
                "/add-driver",
                driver_path,
                "/install"
            ],
            check=True
        )
        print("Printer driver installed successfully.")

        # Step 3: Add the printer
        print(f"Adding printer: {printer_name}...")
        subprocess.run(
            [
                "powershell",
                "-Command",
                f"Add-Printer -Name '{printer_name}' -PortName 'IP_{printer_ip}' -DriverName '{printer_name}'"
            ],
            check=True
        )
        print("Printer added successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing a command: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage
    # Replace these values with the actual printer details
    PRINTER_NAME = "MyNetworkPrinter"
    PRINTER_IP = "192.168.1.100"
    DRIVER_PATH = "C:\\path\\to\\printer\\driver.inf"

    print("Starting network printer installation...")
    install_network_printer(PRINTER_NAME, PRINTER_IP, DRIVER_PATH)
    print("Network printer installation completed.")
```

This script assumes that the user has administrative privileges and that the required printer driver `.inf` file is available locally. It uses PowerShell commands and the `pnputil` utility to configure the printer.
