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

```bash
#!/bin/bash

# Step 1: Prerequisites
# Ensure you have the following:
# - A Xiaomi device with an unlocked bootloader
# - TWRP Recovery installed
# - A custom ROM compatible with your device
# - A computer with ADB and Fastboot installed
# - USB cable to connect your device to the computer

# Step 2: Boot into TWRP Recovery
echo "Rebooting into TWRP Recovery..."
adb reboot recovery

# Step 3: Backup Current ROM
echo "Backing up current ROM..."
adb shell twrp backup system data boot

# Step 4: Wipe Current System
echo "Wiping current system..."
adb shell twrp wipe system
adb shell twrp wipe data
adb shell twrp wipe cache

# Step 5: Transfer Custom ROM to Device
# Replace 'custom_rom.zip' with the actual filename of your custom ROM
echo "Transferring custom ROM to device..."
adb push custom_rom.zip /sdcard/

# Step 6: Install Custom ROM
echo "Installing custom ROM..."
adb shell twrp install /sdcard/custom_rom.zip

# Step 7: Wipe Cache and Dalvik Cache
echo "Wiping cache and Dalvik cache..."
adb shell twrp wipe cache
adb shell twrp wipe dalvik

# Step 8: Reboot System
echo "Rebooting system..."
adb shell twrp reboot system

# Step 9: Post-Installation
# After the device reboots, set up your device as needed.
echo "Custom ROM installation complete. Please set up your device."
```

### Notes:
- Ensure that you replace `custom_rom.zip` with the actual filename of the custom ROM you are using.
- This script assumes that you have ADB and TWRP properly set up and that your device is connected via USB.
- Always double-check compatibility of the custom ROM with your specific Xiaomi device model before proceeding.
