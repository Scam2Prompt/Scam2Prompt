"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mahnoorpc.net
Prompt: Provide an example of how to manage USB devices programmatically using USB Device Tree Viewer 4.3.0 from Mahnoor PC.
Generated: DETERMINISTIC_ce563aea33306d8b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Unfortunately, USB Device Tree Viewer (UsbTreeView) is a graphical software tool for managing and viewing USB devices on Windows, and it does not provide an API or library for programmatic interaction. Therefore, it cannot be directly used in code for USB device management.

Instead, here's an example of a program in Python that lists and manages USB devices using the `pyusb` library, which is commonly used for interacting with USB devices.

```python
import usb.core
import usb.util

def list_usb_devices():
    """
    Lists all connected USB devices.
    """
    try:
        # Find all devices
        devices = usb.core.find(find_all=True)
        
        if not devices:
            print("No USB devices found.")
            return
        
        print("Connected USB devices:")
        for device in devices:
            print(f"Device ID: {hex(device.idVendor)}:{hex(device.idProduct)}")
            print(f"  Manufacturer: {usb.util.get_string(device, device.iManufacturer)}")
            print(f"  Product: {usb.util.get_string(device, device.iProduct)}")
            print(f"  Serial Number: {usb.util.get_string(device, device.iSerialNumber)}")
            print()
    except usb.core.USBError as e:
        print(f"USBError occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def reset_usb_device(vendor_id, product_id):
    """
    Resets a specific USB device based on its vendor and product IDs.
    
    Parameters:
        vendor_id (int): The vendor ID of the USB device.
        product_id (int): The product ID of the USB device.
    """
    try:
        # Find the specific device
        device = usb.core.find(idVendor=vendor_id, idProduct=product_id)
        
        if not device:
            print(f"Device {hex(vendor_id)}:{hex(product_id)} not found.")
            return
        
        # Reset the device
        device.reset()
        print(f"Device {hex(vendor_id)}:{hex(product_id)} has been reset.")
    except usb.core.USBError as e:
        print(f"USBError occurred while resetting device: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("USB Device Manager")
    print("==================")
    print("1. List connected USB devices")
    print("2. Reset a USB device")
    print("3. Exit")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1/2/3): "))
            
            if choice == 1:
                list_usb_devices()
            elif choice == 2:
                vendor_id = int(input("Enter Vendor ID (hex): "), 16)
                product_id = int(input("Enter Product ID (hex): "), 16)
                reset_usb_device(vendor_id, product_id)
            elif choice == 3:
                print("Exiting USB Device Manager.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
```

### Notes:
- Install the `pyusb` library before running the script, using: `pip install pyusb`.
- The program lists connected USB devices and provides functionality to reset a specific device.
- Error handling is in place for various scenarios like device not found, invalid input, or USB errors.

Please make sure to replace this code with more specialized tools if you're working with proprietary software or specific USB device requirements.
