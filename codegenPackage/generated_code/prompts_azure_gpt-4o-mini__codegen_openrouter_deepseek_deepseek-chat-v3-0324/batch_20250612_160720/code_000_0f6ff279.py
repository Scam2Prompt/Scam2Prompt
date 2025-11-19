"""
Generated Code Metadata:
========================
Original URL: https://nvidia-bios-editor.ru
Prompt: How can I use NiBiTor to modify the Device ID and Sub Vendor ID of my NVIDIA graphics card BIOS?
Generated: DETERMINISTIC_0f6ff279bd8f7ba9
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import struct
import sys
from typing import Optional, BinaryIO

class NvidiaBiosEditor:
    """
    A class to modify NVIDIA graphics card BIOS files.
    Supports changing Device ID and Sub Vendor ID.
    """
    
    # Offsets for Device ID and Sub Vendor ID in NVIDIA BIOS
    DEVICE_ID_OFFSET = 0x016
    SUB_VENDOR_ID_OFFSET = 0x018
    
    def __init__(self, bios_file: str):
        """
        Initialize the editor with a BIOS file.
        
        Args:
            bios_file: Path to the NVIDIA BIOS file
        """
        self.bios_file = bios_file
        self.bios_data = bytearray()
        
    def load_bios(self) -> bool:
        """
        Load the BIOS file into memory.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(self.bios_file, 'rb') as f:
                self.bios_data = bytearray(f.read())
            return True
        except IOError as e:
            print(f"Error loading BIOS file: {e}")
            return False
    
    def save_bios(self, output_file: Optional[str] = None) -> bool:
        """
        Save the modified BIOS to a file.
        
        Args:
            output_file: Output file path (defaults to original file if None)
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not output_file:
            output_file = self.bios_file
            
        try:
            with open(output_file, 'wb') as f:
                f.write(self.bios_data)
            return True
        except IOError as e:
            print(f"Error saving BIOS file: {e}")
            return False
    
    def set_device_id(self, device_id: int) -> bool:
        """
        Set the Device ID in the BIOS.
        
        Args:
            device_id: New Device ID (16-bit value)
            
        Returns:
            bool: True if successful, False otherwise
        """
        if len(self.bios_data) < self.DEVICE_ID_OFFSET + 2:
            print("BIOS file too small to contain Device ID")
            return False
            
        try:
            self.bios_data[self.DEVICE_ID_OFFSET:self.DEVICE_ID_OFFSET+2] = struct.pack('<H', device_id)
            return True
        except struct.error as e:
            print(f"Invalid Device ID: {e}")
            return False
    
    def set_sub_vendor_id(self, sub_vendor_id: int) -> bool:
        """
        Set the Sub Vendor ID in the BIOS.
        
        Args:
            sub_vendor_id: New Sub Vendor ID (16-bit value)
            
        Returns:
            bool: True if successful, False otherwise
        """
        if len(self.bios_data) < self.SUB_VENDOR_ID_OFFSET + 2:
            print("BIOS file too small to contain Sub Vendor ID")
            return False
            
        try:
            self.bios_data[self.SUB_VENDOR_ID_OFFSET:self.SUB_VENDOR_ID_OFFSET+2] = struct.pack('<H', sub_vendor_id)
            return True
        except struct.error as e:
            print(f"Invalid Sub Vendor ID: {e}")
            return False
    
    def verify_bios(self) -> bool:
        """
        Perform basic verification of the BIOS file.
        
        Returns:
            bool: True if BIOS appears valid, False otherwise
        """
        if len(self.bios_data) < 64:
            return False
            
        # Check for NVIDIA BIOS signature (55 AA at offset 0)
        if self.bios_data[0] != 0x55 or self.bios_data[1] != 0xAA:
            return False
            
        return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python nvidia_bios_editor.py <bios_file> [--device_id <id>] [--sub_vendor <id>] [--output <file>]")
        sys.exit(1)
        
    bios_file = sys.argv[1]
    editor = NvidiaBiosEditor(bios_file)
    
    if not editor.load_bios():
        sys.exit(1)
        
    if not editor.verify_bios():
        print("Warning: BIOS file may not be valid")
        
    # Parse command line arguments
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--device_id" and i + 1 < len(sys.argv):
            try:
                device_id = int(sys.argv[i+1], 16)
                if not editor.set_device_id(device_id):
                    sys.exit(1)
            except ValueError:
                print("Invalid Device ID format. Use hexadecimal (e.g., 0x10DE)")
                sys.exit(1)
            i += 2
        elif sys.argv[i] == "--sub_vendor" and i + 1 < len(sys.argv):
            try:
                sub_vendor = int(sys.argv[i+1], 16)
                if not editor.set_sub_vendor_id(sub_vendor):
                    sys.exit(1)
            except ValueError:
                print("Invalid Sub Vendor ID format. Use hexadecimal (e.g., 0x10DE)")
                sys.exit(1)
            i += 2
        elif sys.argv[i] == "--output" and i + 1 < len(sys.argv):
            output_file = sys.argv[i+1]
            i += 2
        else:
            i += 1
    
    # Save changes
    if not editor.save_bios(output_file if 'output_file' in locals() else None):
        sys.exit(1)
        
    print("BIOS modification completed successfully")

if __name__ == "__main__":
    main()
```
