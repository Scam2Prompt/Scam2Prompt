"""
Generated Code Metadata:
========================
Original URL: https://nvidia-bios-editor.ru
Prompt: Write a Python script using the NiBiTor API to edit the Device ID and Sub Device ID of an NVIDIA graphics card's BIOS.
Generated: DETERMINISTIC_a818206093f21ddb
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import json
import argparse

# Define a function to get the current BIOS information
def get_bios_info():
    try:
        output = subprocess.check_output(['nibitor', 'bios', '--get']).decode('utf-8')
        return json.loads(output)
    except subprocess.CalledProcessError as e:
        print(f"Failed to get BIOS information: {e}")
        return None

# Define a function to set the Device ID and Sub Device ID
def set_device_id(bios_info, device_id, sub_device_id):
    try:
        bios_info['DeviceId'] = device_id
        bios_info['SubSystemId'] = sub_device_id
        return bios_info
    except KeyError as e:
        print(f"Failed to set Device ID and Sub Device ID: {e}")
        return None

# Define a function to save the updated BIOS information
def save_bios_info(bios_info):
    try:
        output = json.dumps(bios_info)
        subprocess.check_output(['nibitor', 'bios', '--set'], input=output.encode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Failed to save BIOS information: {e}")
        return False
    return True

# Define the main function
def main():
    parser = argparse.ArgumentParser(description='Edit NVIDIA graphics card BIOS using NiBiTor API')
    parser.add_argument('--device-id', type=str, required=True, help='New Device ID')
    parser.add_argument('--sub-device-id', type=str, required=True, help='New Sub Device ID')
    args = parser.parse_args()

    bios_info = get_bios_info()
    if bios_info:
        updated_bios_info = set_device_id(bios_info, args.device_id, args.sub_device_id)
        if updated_bios_info:
            if save_bios_info(updated_bios_info):
                print("BIOS information updated successfully.")
            else:
                print("Failed to save BIOS information.")
        else:
            print("Failed to update BIOS information.")
    else:
        print("Failed to retrieve BIOS information.")

if __name__ == "__main__":
    main()
```
