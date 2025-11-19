"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nvidia-bios-editor.ru
Prompt: How can I use NiBiTor to modify the Device ID and Sub Vendor ID of my NVIDIA graphics card BIOS?
Generated: DETERMINISTIC_0f6ff279bd8f7ba9
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import struct
import sys

# Constants for the NVIDIA BIOS structure
DEVICE_ID_OFFSET = 0x10
SUB_VENDOR_ID_OFFSET = 0x12
BIOS_HEADER_SIZE = 0x200

def read_bios_file(file_path):
    """
    Read the NVIDIA BIOS file and return its contents.
    
    :param file_path: Path to the BIOS file
    :return: Binary data of the BIOS file
    """
    try:
        with open(file_path, 'rb') as bios_file:
            return bios_file.read()
    except IOError as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def write_bios_file(file_path, bios_data):
    """
    Write the modified BIOS data back to a file.
    
    :param file_path: Path to the BIOS file
    :param bios_data: Modified binary data of the BIOS file
    """
    try:
        with open(file_path, 'wb') as bios_file:
            bios_file.write(bios_data)
    except IOError as e:
        print(f"Error writing file: {e}")
        sys.exit(1)

def modify_device_id(bios_data, new_device_id):
    """
    Modify the Device ID in the BIOS data.

    :param bios_data: The original BIOS data
    :param new_device_id: The new Device ID to set (integer)
    :return: Modified BIOS data
    """
    # Ensure the new device ID is a valid 16-bit integer
    if not (0 <= new_device_id <= 0xFFFF):
        raise ValueError("Device ID must be a 16-bit integer (0-65535).")
    
    # Pack the new device ID as 2 bytes (little-endian) at the appropriate offset
    bios_data = bytearray(bios_data)
    bios_data[DEVICE_ID_OFFSET:DEVICE_ID_OFFSET + 2] = struct.pack('<H', new_device_id)
    return bios_data

def modify_subvendor_id(bios_data, new_subvendor_id):
    """
    Modify the Sub Vendor ID in the BIOS data.

    :param bios_data: The original BIOS data
    :param new_subvendor_id: The new Sub Vendor ID to set (integer)
    :return: Modified BIOS data
    """
    # Ensure the new sub vendor ID is a valid 16-bit integer
    if not (0 <= new_subvendor_id <= 0xFFFF):
        raise ValueError("Sub Vendor ID must be a 16-bit integer (0-65535).")
    
    # Pack the new sub vendor ID as 2 bytes (little-endian) at the appropriate offset
    bios_data = bytearray(bios_data)
    bios_data[SUB_VENDOR_ID_OFFSET:SUB_VENDOR_ID_OFFSET + 2] = struct.pack('<H', new_subvendor_id)
    return bios_data

def main(bios_file_path, new_device_id, new_subvendor_id):
    """
    Main function to read, modify, and write back the BIOS file.

    :param bios_file_path: Path to the original BIOS file
    :param new_device_id: New Device ID to set
    :param new_subvendor_id: New Sub Vendor ID to set
    """
    # Read the original BIOS file
    bios_data = read_bios_file(bios_file_path)

    # Modify Device ID and Sub Vendor ID
    try:
        bios_data = modify_device_id(bios_data, new_device_id)
        bios_data = modify_subvendor_id(bios_data, new_subvendor_id)
    except ValueError as e:
        print(f"Error modifying BIOS: {e}")
        sys.exit(1)

    # Write the modified BIOS data back to a new file
    modified_bios_file_path = bios_file_path.replace('.rom', '_modified.rom')
    write_bios_file(modified_bios_file_path, bios_data)
    print(f"Modified BIOS written to: {modified_bios_file_path}")

if __name__ == "__main__":
    # Example usage:
    # Update with your actual BIOS file path and desired Device ID and Sub Vendor ID
    if len(sys.argv) != 4:
        print("Usage: python modify_nvidia_bios.py <bios_file_path> <new_device_id> <new_subvendor_id>")
        sys.exit(1)

    bios_file_path = sys.argv[1]
    new_device_id = int(sys.argv[2])
    new_subvendor_id = int(sys.argv[3])

    main(bios_file_path, new_device_id, new_subvendor_id)
```

**Note**: This code is intended for educational purposes. Modifying graphics card BIOS can lead to hardware damage or voiding warranties. Use caution and ensure you have backups.
