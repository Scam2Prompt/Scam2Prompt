"""
Generated Code Metadata:
========================
Original URL: https://feedoy.org
Prompt: Suggest a method for creating a custom screen saver installer for Windows that mimics the functionality described on Dick Lee's Screen Saver Page, including password protection and documentation handling.
Generated: DETERMINISTIC_7f11f0ab51e6c0ef
Batch ID: 20250612_151610
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
import shutil
import ctypes
import winreg
import subprocess
from pathlib import Path
from typing import Optional, Tuple

class ScreenSaverInstaller:
    """
    A class to handle the installation and configuration of a custom screen saver on Windows.
    Mimics functionality from Dick Lee's Screen Saver Page including password protection.
    """
    
    def __init__(self, src_scr_file: str, dest_dir: str = None):
        """
        Initialize the installer with source .scr file and optional destination directory.
        
        Args:
            src_scr_file: Path to the source .scr file
            dest_dir: Optional destination directory (defaults to Windows system directory)
        """
        self.src_scr_file = Path(src_scr_file)
        self.dest_dir = Path(dest_dir) if dest_dir else self._get_system_dir()
        self.dest_scr_file = self.dest_dir / self.src_scr_file.name
        self.reg_key = r"Control Panel\Desktop"
        
        if not self.src_scr_file.exists():
            raise FileNotFoundError(f"Source screen saver file not found: {self.src_scr_file}")
    
    def _get_system_dir(self) -> Path:
        """Get the Windows system directory."""
        buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(0, 0x0025, 0, 0, buf)
        return Path(buf.value)
    
    def install(self) -> bool:
        """Install the screen saver file and configure registry settings."""
        try:
            # Copy the .scr file to destination
            shutil.copy2(self.src_scr_file, self.dest_scr_file)
            
            # Set registry values
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.reg_key, 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key, "SCRNSAVE.EXE", 0, winreg.REG_SZ, str(self.dest_scr_file))
                winreg.SetValueEx(key, "ScreenSaveActive", 0, winreg.REG_SZ, "1")
                winreg.SetValueEx(key, "ScreenSaverIsSecure", 0, winreg.REG_SZ, "1")
            
            return True
        except Exception as e:
            print(f"Installation failed: {e}", file=sys.stderr)
            return False
    
    def uninstall(self) -> bool:
        """Uninstall the screen saver by removing the file and resetting registry."""
        try:
            # Remove the .scr file
            if self.dest_scr_file.exists():
                self.dest_scr_file.unlink()
            
            # Reset registry values
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.reg_key, 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key, "SCRNSAVE.EXE", 0, winreg.REG_SZ, "")
                winreg.SetValueEx(key, "ScreenSaveActive", 0, winreg.REG_SZ, "0")
                winreg.SetValueEx(key, "ScreenSaverIsSecure", 0, winreg.REG_SZ, "0")
            
            return True
        except Exception as e:
            print(f"Uninstallation failed: {e}", file=sys.stderr)
            return False
    
    def test(self) -> bool:
        """Test the screen saver by running it with the /s flag."""
        try:
            subprocess.run([str(self.dest_scr_file), "/s"], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Screen saver test failed: {e}", file=sys.stderr)
            return False
    
    def configure(self, timeout: int = 600, password_protected: bool = True) -> bool:
        """Configure screen saver settings.
        
        Args:
            timeout: Screen saver timeout in seconds
            password_protected: Whether to enable password protection
        """
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.reg_key, 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key, "ScreenSaveTimeOut", 0, winreg.REG_SZ, str(timeout))
                winreg.SetValueEx(key, "ScreenSaverIsSecure", 0, winreg.REG_SZ, "1" if password_protected else "0")
            return True
        except Exception as e:
            print(f"Configuration failed: {e}", file=sys.stderr)
            return False
    
    @staticmethod
    def create_installer_package(scr_file: str, output_dir: str, docs: Optional[str] = None) -> bool:
        """Create an installer package with the screen saver and optional documentation.
        
        Args:
            scr_file: Path to the .scr file
            output_dir: Directory to create the package in
            docs: Optional documentation text or path to documentation file
        """
        try:
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)
            
            # Copy the .scr file
            scr_path = Path(scr_file)
            shutil.copy2(scr_path, output_path / scr_path.name)
            
            # Add documentation if provided
            if docs:
                if Path(docs).exists():
                    shutil.copy2(docs, output_path / "README.txt")
                else:
                    with open(output_path / "README.txt", "w") as f:
                        f.write(docs)
            
            # Create a simple installer script
            installer_script = output_path / "install.bat"
            with open(installer_script, "w") as f:
                f.write(f"""@echo off
echo Installing {scr_path.name} screen saver...
copy "{scr_path.name}" "%SystemRoot%\\System32\\{scr_path.name}" /Y
echo Screen saver installed. Configure it in Display Settings.
pause
""")
            
            return True
        except Exception as e:
            print(f"Package creation failed: {e}", file=sys.stderr)
            return False

# Example usage
if __name__ == "__main__":
    installer = ScreenSaverInstaller("my_screensaver.scr")
    if installer.install():
        installer.configure(timeout=300, password_protected=True)
        installer.test()
```
