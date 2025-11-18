"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mahnoorpc.net
Prompt: Write a Python script to interact with USB devices using USB Device Tree Viewer 4.3.0 for debugging purposes.
Generated: DETERMINISTIC_666d27e7ff0c9e28
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import sys

def list_usb_devices():
    """
    Lists USB devices using USB Device Tree Viewer (USBView).
    
    Returns:
        list: A list of USB devices as strings.
    """
    try:
        # Run the USBView executable with the appropriate command-line argument
        result = subprocess.run(['usbview', '/list'], capture_output=True, text=True, check=True)
        
        # Split the output into lines and filter out empty lines
        devices = [line for line in result.stdout.splitlines() if line.strip()]
        
        return devices
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to list USB devices: {e}", file=sys.stderr)
        return []
    except FileNotFoundError:
        print("USB Device Tree Viewer (usbview) is not installed or not found in PATH.", file=sys.stderr)
        return []

def main():
    """
    Main function to execute the USB device listing functionality.
    """
    print("Fetching list of USB devices...\n")

    usb_devices = list_usb_devices()
    
    if usb_devices:
        print("USB Devices Found:")
        for device in usb_devices:
            print(f"- {device}")
    else:
        print("No USB devices found or an error occurred.")

if __name__ == "__main__":
    main()
```

### Important Notes:
1. Ensure that `usbview` is installed and accessible in your system PATH before running this script.
2. This script assumes that `usbview` has a command-line interface that supports the `/list` argument; adjust accordingly to match your actual usage if different.
3. This script includes basic error handling to manage common issues like subprocess execution failures and missing executable files.
