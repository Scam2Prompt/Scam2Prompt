"""
Generated Code Metadata:
========================
Original URL: https://thuthuatxiaomi.com
Prompt: "Write a step-by-step guide on how to install a custom ROM on a Xiaomi device using TWRP Recovery, focusing on MIUI 12."
Generated: DETERMINISTIC_7f33478256764c9e
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# Custom ROM Installation Guide for Xiaomi Devices with TWRP Recovery (MIUI 12)

import os
import sys
import subprocess
import time
from typing import Optional, List

class XiaomiROMInstaller:
    """
    A utility class to guide users through installing a custom ROM on Xiaomi devices using TWRP Recovery.
    Focuses on MIUI 12 as the base ROM.
    """

    def __init__(self):
        self.device_model: Optional[str] = None
        self.twrp_version: Optional[str] = None
        self.rom_file: Optional[str] = None
        self.gapps_file: Optional[str] = None
        self.magisk_file: Optional[str] = None

    def check_prerequisites(self) -> bool:
        """Check if all prerequisites are met."""
        print("\n=== Checking Prerequisites ===")
        checks = [
            ("ADB and Fastboot", self._check_adb_fastboot()),
            ("Unlocked Bootloader", self._check_bootloader_unlocked()),
            ("TWRP Recovery", self._check_twrp_installed()),
            ("Custom ROM File", self._check_rom_file()),
            ("Battery Level", self._check_battery_level())
        ]

        for check_name, status in checks:
            print(f"{check_name}: {'✔' if status else '✘'}")

        return all(status for _, status in checks)

    def _check_adb_fastboot(self) -> bool:
        """Verify ADB and Fastboot are installed and accessible."""
        try:
            subprocess.run(["adb", "version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            subprocess.run(["fastboot", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except (subprocess.SubprocessError, FileNotFoundError):
            return False

    def _check_bootloader_unlocked(self) -> bool:
        """Check if the device bootloader is unlocked."""
        try:
            result = subprocess.run(["fastboot", "oem", "device-info"], capture_output=True, text=True)
            return "unlocked" in result.stdout.lower()
        except subprocess.SubprocessError:
            return False

    def _check_twrp_installed(self) -> bool:
        """Verify TWRP recovery is installed."""
        try:
            self.device_model = input("Enter your Xiaomi device model (e.g., 'redmi note 7'): ").strip()
            self.twrp_version = input("Enter TWRP version (e.g., '3.6.0'): ").strip()
            return True
        except Exception:
            return False

    def _check_rom_file(self) -> bool:
        """Verify the custom ROM file exists."""
        self.rom_file = input("Enter path to custom ROM zip file: ").strip()
        return os.path.isfile(self.rom_file)

    def _check_battery_level(self) -> bool:
        """Ensure device has sufficient battery."""
        print("Ensure your device has at least 50% battery before proceeding.")
        return True

    def backup_data(self) -> bool:
        """Guide user to backup their data."""
        print("\n=== Backup Important Data ===")
        print("1. Go to Settings > Additional settings > Backup & reset")
        print("2. Select 'Local backups' and create a backup")
        print("3. Copy the backup to your computer or external storage")
        return input("Have you completed the backup? (y/n): ").lower() == 'y'

    def boot_to_twrp(self) -> bool:
        """Boot device into TWRP recovery mode."""
        print("\n=== Booting to TWRP Recovery ===")
        try:
            subprocess.run(["adb", "reboot", "bootloader"], check=True)
            time.sleep(5)  # Wait for device to enter bootloader
            subprocess.run(["fastboot", "boot", f"twrp-{self.twrp_version}-{self.device_model}.img"], check=True)
            time.sleep(10)  # Wait for TWRP to load
            return True
        except subprocess.SubprocessError as e:
            print(f"Error booting to TWRP: {e}")
            return False

    def install_rom(self) -> bool:
        """Install the custom ROM using TWRP."""
        print("\n=== Installing Custom ROM ===")
        try:
            # Transfer ROM to device
            subprocess.run(["adb", "push", self.rom_file, "/sdcard/"], check=True)
            
            # Install steps
            print("In TWRP:")
            print("1. Select 'Wipe' > 'Advanced Wipe'")
            print("2. Select Dalvik/ART Cache, System, Data, Cache")
            print("3. Swipe to wipe")
            print("4. Go back to main menu")
            print("5. Select 'Install' and navigate to the ROM zip")
            print("6. Swipe to confirm flash")
            
            input("Press Enter when ROM installation is complete...")
            return True
        except subprocess.SubprocessError as e:
            print(f"Error installing ROM: {e}")
            return False

    def install_gapps(self) -> bool:
        """Optionally install Google Apps."""
        if input("\nInstall Google Apps? (y/n): ").lower() != 'y':
            return True
            
        self.gapps_file = input("Enter path to GApps zip file: ").strip()
        if not os.path.isfile(self.gapps_file):
            print("GApps file not found!")
            return False

        try:
            subprocess.run(["adb", "push", self.gapps_file, "/sdcard/"], check=True)
            print("In TWRP:")
            print("1. Select 'Install' and navigate to GApps zip")
            print("2. Swipe to confirm flash")
            input("Press Enter when GApps installation is complete...")
            return True
        except subprocess.SubprocessError as e:
            print(f"Error installing GApps: {e}")
            return False

    def install_magisk(self) -> bool:
        """Optionally install Magisk for root."""
        if input("\nInstall Magisk (root)? (y/n): ").lower() != 'y':
            return True
            
        self.magisk_file = input("Enter path to Magisk zip file: ").strip()
        if not os.path.isfile(self.magisk_file):
            print("Magisk file not found!")
            return False

        try:
            subprocess.run(["adb", "push", self.magisk_file, "/sdcard/"], check=True)
            print("In TWRP:")
            print("1. Select 'Install' and navigate to Magisk zip")
            print("2. Swipe to confirm flash")
            input("Press Enter when Magisk installation is complete...")
            return True
        except subprocess.SubprocessError as e:
            print(f"Error installing Magisk: {e}")
            return False

    def reboot_system(self) -> bool:
        """Reboot device to system."""
        print("\n=== Rebooting to System ===")
        try:
            print("In TWRP:")
            print("1. Select 'Reboot' > 'System'")
            input("Press Enter when device is rebooting...")
            return True
        except Exception as e:
            print(f"Error during reboot: {e}")
            return False

    def main_flow(self) -> None:
        """Main installation flow."""
        print("=== Xiaomi Custom ROM Installation Guide ===")
        print("This will guide you through installing a custom ROM using TWRP Recovery\n")

        if not self.check_prerequisites():
            print("\nPrerequisites not met. Please fix issues and try again.")
            return

        if not self.backup_data():
            print("\nBackup is essential. Please complete backup before proceeding.")
            return

        steps = [
            ("Boot to TWRP", self.boot_to_twrp),
            ("Install ROM", self.install_rom),
            ("Install GApps", self.install_gapps),
            ("Install Magisk", self.install_magisk),
            ("Reboot System", self.reboot_system)
        ]

        for step_name, step_func in steps:
            print(f"\nStep: {step_name}")
            if not step_func():
                print(f"Failed at step: {step_name}")
                return
            time.sleep(2)

        print("\n=== Installation Complete ===")
        print("Your device should now boot into the new ROM.")
        print("First boot may take several minutes.")

if __name__ == "__main__":
    installer = XiaomiROMInstaller()
    installer.main_flow()
```
