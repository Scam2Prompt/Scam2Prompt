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

```python
import os
import shutil
import subprocess
import sys
import tempfile

def install_chrome_extension(crx_file_path):
    """
    Automates the offline installation of a Chrome extension using a .crx file.

    Parameters:
    crx_file_path (str): The file path of the .crx extension file to install.

    Raises:
    FileNotFoundError: If the .crx file is not found.
    subprocess.CalledProcessError: If the installation command fails.
    """
    
    # Define the path to the Chrome profile and extensions directory
    chrome_profile_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data', 'Default')
    extensions_path = os.path.join(chrome_profile_path, 'Extensions')

    # Check if the .crx file exists
    if not os.path.isfile(crx_file_path):
        raise FileNotFoundError(f"The specified .crx file does not exist: {crx_file_path}")

    # Create a temporary directory to extract the .crx file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract the .crx file to get the extension files
        extract_crx(crx_file_path, temp_dir)

        # Copy the extracted extension folder to the Chrome extensions directory
        extension_id = get_extension_id(crx_file_path)
        extension_target_path = os.path.join(extensions_path, extension_id)

        if not os.path.exists(extension_target_path):
            os.makedirs(extension_target_path)

        # Copy extracted files to the target extension path
        shutil.copytree(temp_dir, extension_target_path, dirs_exist_ok=True)

        print(f"Extension installed from {crx_file_path} to {extension_target_path}")

def extract_crx(crx_file_path, output_dir):
    """
    Extracts the contents of a .crx file to a specified directory.

    Parameters:
    crx_file_path (str): The file path of the .crx file to extract.
    output_dir (str): The directory to output the extracted files.
    """
    # Use the unzip utility to extract the .crx file
    try:
        subprocess.run(['unzip', crx_file_path, '-d', output_dir], check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to extract .crx file: {e}")

def get_extension_id(crx_file_path):
    """
    Retrieves the extension ID from the .crx file name.

    Parameters:
    crx_file_path (str): The file path of the .crx file.

    Returns:
    str: The extension ID derived from the .crx file name.
    """
    # Assuming the .crx file name is in the format <extension_id>.crx
    return os.path.splitext(os.path.basename(crx_file_path))[0]

if __name__ == "__main__":
    # Check command line arguments for the .crx file path
    if len(sys.argv) != 2:
        print("Usage: python install_chrome_extension.py <path_to_crx_file>")
        sys.exit(1)

    crx_file_path = sys.argv[1]

    try:
        install_chrome_extension(crx_file_path)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
```
