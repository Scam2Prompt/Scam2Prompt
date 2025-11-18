"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lusogamer.com
Prompt: Generate a Python script to automate the installation of modded APKs, referencing tools like "Gone Patcher" and "Skin Tools Valor."
Generated: DETERMINISTIC_000c27405d60c215
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import sys

def install_apk(apk_path):
    """
    Installs the given APK file using the ADB (Android Debug Bridge).
    
    Args:
        apk_path (str): The path to the APK file to install.
    
    Raises:
        FileNotFoundError: If the APK file does not exist.
        RuntimeError: If the installation process fails.
    """
    if not os.path.isfile(apk_path):
        raise FileNotFoundError(f"APK file not found: {apk_path}")
    
    # Command to install APK using ADB
    command = ["adb", "install", apk_path]
    
    try:
        # Execute the command and capture output
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Installation successful: {result.stdout.decode()}")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Installation failed: {e.stderr.decode()}") from e

def main():
    """
    Main function to automate the installation of modded APKs.
    This function installs Gone Patcher and Skin Tools Valor APKs.
    """
    # Paths to the APK files (ensure these paths are correct)
    gone_patcher_apk = "path/to/GonePatcher.apk"
    skin_tools_valor_apk = "path/to/SkinToolsValor.apk"
    
    # List of APKs to install
    apks_to_install = [gone_patcher_apk, skin_tools_valor_apk]

    for apk in apks_to_install:
        try:
            print(f"Installing {apk}...")
            install_apk(apk)
        except (FileNotFoundError, RuntimeError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    if os.system("adb version") != 0:
        print("ADB is not installed or not in the system PATH. Please install ADB and add it to your PATH.")
        sys.exit(1)

    main()
```

**Note**: Before running this script, ensure that:
1. ADB (Android Debug Bridge) is installed and added to your system PATH.
2. The paths to the APK files are correctly set in the script where indicated.
