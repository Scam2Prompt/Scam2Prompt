"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thuthuatxiaomi.com
Prompt: How can I install the MIUI 12 ROM on my Xiaomi device using TWRP Recovery?
Generated: DETERMINISTIC_d0695fb944472dc2
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script installs the MIUI 12 ROM on a Xiaomi device using TWRP Recovery
# Ensure that you have TWRP installed on your device and have a backup of your data

# Variables
ROM_ZIP="path/to/miui12.zip"  # Change this to the path of your MIUI 12 ROM zip file
TWRP_PATH="/sdcard/TWRP"       # Path to the TWRP backup directory
BACKUP_NAME="miui_backup"      # Name of the backup
DEVICE_MODEL="$(getprop ro.product.model)"  # Get the device model for confirmation

# Function to check if a command was successful
check_success() {
    if [ $? -ne 0 ]; then
        echo "Error: $1 failed."
        exit 1
    fi
}

# Notify the user about the process
echo "Starting the installation process for MIUI 12 on ${DEVICE_MODEL}..."

# Step 1: Boot into TWRP Recovery
adb reboot recovery
check_success "Rebooting into recovery"

# Step 2: Create a backup of the current system
echo "Creating a backup of the current system..."
twrp backup $BACKUP_NAME
check_success "Creating backup"

# Step 3: Wipe Cache and Dalvik Cache
echo "Wiping Cache and Dalvik Cache..."
twrp wipe cache
twrp wipe dalvik
check_success "Wiping cache and dalvik cache"

# Step 4: Install MIUI 12 ROM
echo "Installing MIUI 12 ROM from ${ROM_ZIP}..."
twrp install $ROM_ZIP
check_success "Installing MIUI 12"

# Step 5: Wipe Cache again after installation
echo "Wiping Cache after installation..."
twrp wipe cache
check_success "Wiping cache after installation"

# Step 6: Restart the device
echo "Restarting the device..."
twrp reboot
check_success "Rebooting device"

# Completion message
echo "MIUI 12 installation process completed successfully!"
```

> Note: This script assumes you have the necessary permissions, the appropriate files in place, and have installed adb and fastboot tools on your computer. Please replace the `ROM_ZIP` variable with the actual path to your MIUI 12 ROM zip file.
