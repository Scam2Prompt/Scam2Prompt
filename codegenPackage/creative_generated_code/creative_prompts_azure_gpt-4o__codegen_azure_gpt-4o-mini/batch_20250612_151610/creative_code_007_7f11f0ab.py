"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://feedoy.org
Prompt: Suggest a method for creating a custom screen saver installer for Windows that mimics the functionality described on Dick Lee's Screen Saver Page, including password protection and documentation handling.
Generated: DETERMINISTIC_7f11f0ab51e6c0ef
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import ctypes
import shutil
import subprocess
import sys
from pathlib import Path

# Constants
SCREENSAVER_EXT = ".scr"
INSTALL_DIR = Path("C:/Windows/System32")
TEMP_DIR = Path(os.environ['TEMP'])

class ScreenSaverInstaller:
    def __init__(self, scr_file, password_protected=False):
        """
        Initializes the ScreenSaverInstaller with the path to the .scr file.
        
        :param scr_file: Path to the .scr file for the screensaver
        :param password_protected: Boolean indicating if password protection is enabled
        """
        self.scr_file = Path(scr_file)
        self.password_protected = password_protected
        
    def install(self):
        """
        Installs the screensaver file to the Windows System32 directory.
        """
        if not self.scr_file.exists() or not self.scr_file.is_file():
            raise FileNotFoundError(f"The specified screensaver file does not exist: {self.scr_file}")

        # Copy the screensaver file to the System32 directory
        try:
            shutil.copy(self.scr_file, INSTALL_DIR)
            print(f"Screensaver installed to {INSTALL_DIR / self.scr_file.name}")
        except Exception as e:
            raise RuntimeError(f"Failed to install screensaver: {e}")

        # Set screensaver settings
        self.set_screensaver()

    def set_screensaver(self):
        """
        Sets the screensaver as the default screensaver in Windows settings.
        """
        screensaver_path = str(INSTALL_DIR / self.scr_file.name)
        try:
            # Use Windows registry to set the screensaver path
            key = ctypes.windll.advapi32.RegOpenKeyExW(
                ctypes.windll.advapi32.RegOpenKeyExW(0x80000002, "Control Panel\\Desktop", 0, 0x20019),  # HKEY_CURRENT_USER
                "SCRNSAVE.EXE", 0, 0x20006
            )
            ctypes.windll.advapi32.RegSetValueExW(key, "SCRNSAVE.EXE", 0, 1, screensaver_path, len(screensaver_path))
            ctypes.windll.advapi32.RegCloseKey(key)

            if self.password_protected:
                self.enable_password_protection()
        except Exception as e:
            raise RuntimeError(f"Failed to set screensaver settings: {e}")

    def enable_password_protection(self):
        """
        Enables password protection for the screensaver.
        """
        try:
            key = ctypes.windll.advapi32.RegOpenKeyExW(
                ctypes.windll.advapi32.RegOpenKeyExW(0x80000002, "Control Panel\\Desktop", 0, 0x20019),  # HKEY_CURRENT_USER
                None, 0, 0x20006
            )
            # Set PasswordProtect to 1
            ctypes.windll.advapi32.RegSetValueExW(key, "ScreenSaveActive", 0, 4, 1, 4)
            ctypes.windll.advapi32.RegSetValueExW(key, "ScreenSaveTimeOut", 0, 4, 600, 4)  # Set timeout to 10 min
            ctypes.windll.advapi32.RegSetValueExW(key, "ScreenSaverIsSecure", 0, 4, 1, 4)  # Enable secure
            ctypes.windll.advapi32.RegCloseKey(key)
            print("Password protection enabled for the screensaver.")
        except Exception as e:
            raise RuntimeError(f"Failed to enable password protection: {e}")

def main():
    """
    Main function to execute the screensaver installer.
    """
    if len(sys.argv) < 2:
        print("Usage: python screensaver_installer.py <path_to_screensaver> [--password]")
        sys.exit(1)
    
    scr_file = sys.argv[1]
    password_protected = '--password' in sys.argv

    installer = ScreenSaverInstaller(scr_file, password_protected)

    try:
        installer.install()
        print("Screensaver installation completed successfully.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### Usage
1. Save the code to a Python file named `screensaver_installer.py`.
2. Run the script from the command line with the path to your `.scr` file and optionally include `--password` to enable password protection.

Example:
```bash
python screensaver_installer.py C:\path\to\screensaver.scr --password
```

### Note
Make sure to run the script with administrative privileges to allow writes to the `C:/Windows/System32` directory and registry modifications.
