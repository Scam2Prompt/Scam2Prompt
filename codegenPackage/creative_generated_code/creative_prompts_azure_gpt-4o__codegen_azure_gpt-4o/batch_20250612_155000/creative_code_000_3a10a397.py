"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chajianxw.com
Prompt: Write a script to automate the offline installation of a Chrome extension using a `.crx` file, as described on 插件小屋.
Generated: DETERMINISTIC_3a10a397004c10cf
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for automating the offline installation of a Chrome extension using a `.crx` file. Note that this script is designed for Windows systems and assumes administrative privileges are available to update Chrome's extension registry.

```python
import os
import shutil
import sys
import zipfile
import json
import winreg

# Constants
CHROME_EXTENSIONS_FOLDER = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Extensions")
REGISTRY_KEY = r"Software\Google\Chrome\Extensions"

def extract_crx_to_folder(crx_file, extension_dir):
    """
    Extracts the `.crx` file (which is a ZIP archive) to the specified folder.
    """
    try:
        with zipfile.ZipFile(crx_file, 'r') as zip_ref:
            zip_ref.extractall(extension_dir)
        print(f"Extracted {crx_file} to {extension_dir}")
    except zipfile.BadZipFile:
        print("Error: Invalid CRX file")
        sys.exit(1)

def get_extension_id_from_manifest(manifest_path):
    """
    Reads the `manifest.json` file to retrieve the extension ID.
    """
    try:
        with open(manifest_path, 'r') as manifest_file:
            manifest_data = json.load(manifest_file)
            extension_id = manifest_data.get("key")[:32]  # Simplistic ID generation
            return extension_id
    except FileNotFoundError:
        print(f"Error: manifest.json not found at {manifest_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Invalid JSON in manifest.json")
        sys.exit(1)

def register_extension_in_registry(extension_id, extension_dir):
    """
    Registers the Chrome extension in the Windows registry so Chrome recognizes it.
    """
    try:
        # Open the registry key for Chrome extensions
        with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, REGISTRY_KEY) as reg_key:
            # Create a subkey for the extension ID
            with winreg.CreateKey(reg_key, extension_id) as ext_key:
                winreg.SetValueEx(ext_key, "path", 0, winreg.REG_SZ, extension_dir)
                winreg.SetValueEx(ext_key, "version", 0, winreg.REG_SZ, "1.0")  # Replace with actual version if needed
        print(f"Registered extension {extension_id} in Windows registry")
    except PermissionError:
        print("Error: Administrator privileges are required to modify the registry")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python install_extension.py <path_to_crx_file>")
        sys.exit(1)
    
    crx_file = sys.argv[1]
    
    if not os.path.isfile(crx_file):
        print(f"Error: File not found: {crx_file}")
        sys.exit(1)
    
    # Create a temporary folder for the extension
    temp_extension_folder = os.path.join(os.path.dirname(crx_file), "temp_extension")
    if os.path.exists(temp_extension_folder):
        shutil.rmtree(temp_extension_folder)
    os.makedirs(temp_extension_folder)
    
    # Extract the CRX file
    extract_crx_to_folder(crx_file, temp_extension_folder)
    
    # Get the extension ID from the manifest
    manifest_path = os.path.join(temp_extension_folder, "manifest.json")
    extension_id = get_extension_id_from_manifest(manifest_path)
    
    # Move the extension to the Chrome extensions folder
    final_extension_path = os.path.join(CHROME_EXTENSIONS_FOLDER, extension_id)
    if os.path.exists(final_extension_path):
        shutil.rmtree(final_extension_path)
    shutil.move(temp_extension_folder, final_extension_path)
    
    # Register the extension in the registry
    register_extension_in_registry(extension_id, final_extension_path)
    
    print("Extension installed successfully!")

if __name__ == "__main__":
    main()
```

> **Note**: This script makes assumptions about how CRX files and Chrome extensions work. It may need adjustments for your specific use case, especially for generating the extension ID from the manifest key and handling Chrome's security requirements.
