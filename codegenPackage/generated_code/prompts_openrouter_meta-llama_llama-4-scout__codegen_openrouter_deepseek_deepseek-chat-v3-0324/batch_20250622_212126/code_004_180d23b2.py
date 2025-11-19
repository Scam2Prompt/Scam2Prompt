"""
Generated Code Metadata:
========================
Original URL: https://nvidia-bios-editor.ru
Prompt: Create a code snippet to read and save the BIOS image of an NVIDIA graphics card using the NiBiTor API.
Generated: DETERMINISTIC_180d23b2da6f65bf
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import ctypes
from ctypes import wintypes

# Constants from NiBiTor API
NIBITOR_OK = 0
NIBITOR_ERROR = -1

# Load NiBiTor DLL
try:
    nibitor = ctypes.WinDLL("NiBiTor.dll")
except OSError as e:
    print(f"Failed to load NiBiTor.dll: {e}")
    sys.exit(1)

# Define function prototypes
nibitor.NV_GetBiosVersion.restype = ctypes.c_int
nibitor.NV_GetBiosVersion.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_char_p)]

nibitor.NV_ReadBios.restype = ctypes.c_int
nibitor.NV_ReadBios.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_uint)]

nibitor.NV_SaveBios.restype = ctypes.c_int
nibitor.NV_SaveBios.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint]

def read_and_save_bios(output_file):
    """
    Reads BIOS from NVIDIA GPU and saves it to a file.
    
    Args:
        output_file (str): Path to save the BIOS image
    """
    # Initialize variables
    bios_version = ctypes.c_char_p()
    bios_size = ctypes.c_uint()
    
    # Get BIOS version
    result = nibitor.NV_GetBiosVersion(0, ctypes.byref(bios_version))
    if result != NIBITOR_OK:
        print("Failed to get BIOS version")
        return
    
    print(f"BIOS Version: {bios_version.value.decode('utf-8')}")
    
    # Get BIOS size
    result = nibitor.NV_ReadBios(0, None, ctypes.byref(bios_size))
    if result != NIBITOR_OK:
        print("Failed to get BIOS size")
        return
    
    print(f"BIOS Size: {bios_size.value} bytes")
    
    # Allocate buffer for BIOS data
    bios_data = (ctypes.c_ubyte * bios_size.value)()
    
    # Read BIOS data
    result = nibitor.NV_ReadBios(0, bios_data, ctypes.byref(bios_size))
    if result != NIBITOR_OK:
        print("Failed to read BIOS data")
        return
    
    # Save BIOS to file
    result = nibitor.NV_SaveBios(output_file.encode('utf-8'), bios_data, bios_size)
    if result != NIBITOR_OK:
        print("Failed to save BIOS to file")
        return
    
    print(f"BIOS successfully saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nibitor_bios.py <output_file>")
        sys.exit(1)
    
    output_file = sys.argv[1]
    read_and_save_bios(output_file)
```
