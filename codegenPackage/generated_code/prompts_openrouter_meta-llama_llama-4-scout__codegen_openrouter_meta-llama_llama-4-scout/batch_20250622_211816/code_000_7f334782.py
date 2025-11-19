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

```markdown
# Installing Custom ROM on Xiaomi Device using TWRP Recovery
## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Step 1: Unlock Bootloader](#step-1-unlock-bootloader)
3. [Step 2: Install TWRP Recovery](#step-2-install-twrp-recovery)
4. [Step 3: Backup Existing Data](#step-3-backup-existing-data)
5. [Step 4: Download Custom ROM](#step-4-download-custom-rom)
6. [Step 5: Install Custom ROM](#step-5-install-custom-rom)
7. [Step 6: Post-Installation](#step-6-post-installation)

## Prerequisites
- A Xiaomi device compatible with MIUI 12
- A computer with ADB and Fastboot installed
- USB cable
- Custom ROM file (e.g., based on MIUI 12)
- TWRP Recovery image compatible with your device

### Code for Automating Some Steps
```python
import os
import subprocess

def unlock_bootloader():
    # Example command to unlock bootloader, adjust according to your needs
    command = "fastboot oem unlock"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to unlock bootloader: {e}")

def install_twrp(recovery_image_path):
    # Example command to flash TWRP, adjust according to your needs
    command = f"fastboot flash recovery {recovery_image_path}"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install TWRP: {e}")

def backup_data():
    # Backup using TWRP, manual step recommended

def install_custom_rom(rom_path):
    # Example command to flash custom ROM, adjust according to your needs
    command = f"adb shell twrp install {rom_path}"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install custom ROM: {e}")

if __name__ == "__main__":
    # Example usage
    recovery_image_path = "path/to/twrp.img"
    rom_path = "path/to/rom.zip"
    
    # Manual steps recommended for safety and compatibility
    # unlock_bootloader()
    # install_twrp(recovery_image_path)
    # install_custom_rom(rom_path)
```

## Steps Manual Guide

### Step 1: Unlock Bootloader
1. Enable Developer Options on your device.
2. Go to Developer Options > OEM Unlock and toggle it on.
3. Connect your device to the computer.
4. Use Fastboot to unlock the bootloader.

### Step 2: Install TWRP Recovery
1. Download TWRP image for your device.
2. Connect your device to the computer.
3. Boot into Fastboot mode.
4. Flash TWRP using the command: `fastboot flash recovery twrp.img`

### Step 3: Backup Existing Data
1. Boot into TWRP Recovery.
2. Go to Backup > select data to backup > swipe to backup.

### Step 4: Download Custom ROM
1. Find a custom ROM based on MIUI 12 for your device.
2. Download it to your computer or device.

### Step 5: Install Custom ROM
1. Transfer the ROM to your device if necessary.
2. Boot into TWRP Recovery.
3. Go to Install > select ROM > swipe to install.

### Step 6: Post-Installation
1. Reboot to system.
2. Configure your device.
```

### ADB and Fastboot Commands for Reference
```bash
# Check if device is connected
adb devices

# Reboot to bootloader
adb reboot bootloader

# Unlock bootloader (OEM Unlock)
fastboot oem unlock

# Flash TWRP
fastboot flash recovery twrp.img

# Install custom ROM via ADB (ensure in TWRP)
adb push rom.zip /sdcard/
```
Please adjust commands according to your specific device and files. Manual intervention is recommended for safety. 
```python
# Ensure to handle exceptions and adjust paths
```
