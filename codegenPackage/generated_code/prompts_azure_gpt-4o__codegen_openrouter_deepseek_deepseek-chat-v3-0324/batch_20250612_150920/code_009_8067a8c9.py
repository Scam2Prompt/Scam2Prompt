"""
Generated Code Metadata:
========================
Original URL: https://square-bear.co.uk
Prompt: Develop a Python script to detect and remove spyware from a computer, as suggested on Square Bear's website, using tools like Adaware or Spybot Search and Destroy.
Generated: DETERMINISTIC_8067a8c9b82306f5
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Spyware Detection and Removal Tool

This script automates the detection and removal of spyware using Adaware and Spybot Search & Destroy.
It checks for the presence of these tools, runs scans, and removes detected threats.

Requirements:
- Adaware and Spybot Search & Destroy must be installed on the system.
- Admin privileges may be required for full functionality.
"""

import os
import subprocess
import sys
import platform
import shutil
from typing import Optional, List

class SpywareRemover:
    """
    A class to handle spyware detection and removal using third-party tools.
    """

    def __init__(self):
        self.system_os = platform.system()
        self.tools = {
            'adaware': self._get_adaware_path(),
            'spybot': self._get_spybot_path()
        }

    def _get_adaware_path(self) -> Optional[str]:
        """Check for Adaware installation and return its path."""
        if self.system_os == 'Windows':
            paths = [
                os.path.join(os.environ['ProgramFiles'], 'Adaware', 'Adaware.exe'),
                os.path.join(os.environ['ProgramFiles(x86)'], 'Adaware', 'Adaware.exe')
            ]
            for path in paths:
                if os.path.exists(path):
                    return path
        return None

    def _get_spybot_path(self) -> Optional[str]:
        """Check for Spybot Search & Destroy installation and return its path."""
        if self.system_os == 'Windows':
            paths = [
                os.path.join(os.environ['ProgramFiles'], 'Spybot - Search & Destroy 2', 'SDTray.exe'),
                os.path.join(os.environ['ProgramFiles(x86)'], 'Spybot - Search & Destroy 2', 'SDTray.exe')
            ]
            for path in paths:
                if os.path.exists(path):
                    return path
        return None

    def _run_scan(self, tool_path: str, tool_name: str) -> bool:
        """Run a scan using the specified tool."""
        if not tool_path:
            print(f"{tool_name} not found. Please install it first.")
            return False

        try:
            print(f"Running {tool_name} scan...")
            if tool_name.lower() == 'adaware':
                subprocess.run([tool_path, '/scan', '/full'], check=True)
            elif tool_name.lower() == 'spybot':
                subprocess.run([tool_path, '/scan', '/autofix', '/autoclose'], check=True)
            print(f"{tool_name} scan completed successfully.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error running {tool_name}: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error with {tool_name}: {e}")
            return False

    def run_full_scan(self) -> bool:
        """Run scans with all available tools."""
        success = True
        if self.tools['adaware']:
            success &= self._run_scan(self.tools['adaware'], 'Adaware')
        else:
            print("Adaware not found. Skipping...")

        if self.tools['spybot']:
            success &= self._run_scan(self.tools['spybot'], 'Spybot')
        else:
            print("Spybot Search & Destroy not found. Skipping...")

        return success

    def check_admin(self) -> bool:
        """Check if the script is running with admin privileges."""
        if self.system_os == 'Windows':
            try:
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
            except:
                return False
        else:
            return os.getuid() == 0

def main():
    """Main function to execute the spyware removal process."""
    print("=== Spyware Detection and Removal Tool ===")
    
    remover = SpywareRemover()
    
    if remover.system_os != 'Windows':
        print("This tool currently only supports Windows systems.")
        sys.exit(1)

    if not remover.check_admin():
        print("Warning: Admin privileges not detected. Some functions may not work properly.")
    
    print("\nDetecting installed anti-spyware tools...")
    print(f"Adaware: {'Found' if remover.tools['adaware'] else 'Not Found'}")
    print(f"Spybot Search & Destroy: {'Found' if remover.tools['spybot'] else 'Not Found'}")

    if not any(remover.tools.values()):
        print("\nNo supported anti-spyware tools found. Please install Adaware or Spybot Search & Destroy.")
        sys.exit(1)

    print("\nStarting spyware scan and removal...")
    if remover.run_full_scan():
        print("\nSpyware removal process completed successfully.")
    else:
        print("\nSpyware removal process encountered errors. Please check the logs.")

if __name__ == "__main__":
    main()
```
