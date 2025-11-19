"""
Generated Code Metadata:
========================
Original URL: https://thuthuatxiaomi.com
Prompt: "Provide a tutorial on how to unlock a Xiaomi device's bootloader and install a custom ROM like MiRoom or EU ROM."
Generated: DETERMINISTIC_2812de8267edcd14
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

# Xiaomi Bootloader Unlock and Custom ROM Installation Script
# This script provides a step-by-step guide to unlock the bootloader of a Xiaomi device
# and install a custom ROM like MiRoom or EU ROM.

# Ensure the script is run with root privileges
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

# Function to check if ADB and Fastboot are installed
check_tools() {
    command -v adb >/dev/null 2>&1 || { echo >&2 "ADB is not installed. Please install it first."; exit 1; }
    command -v fastboot >/dev/null 2>&1 || { echo >&2 "Fastboot is not installed. Please install it first."; exit 1; }
}

# Function to unlock the bootloader
unlock_bootloader() {
    echo "Unlocking bootloader..."
    adb reboot bootloader
    sleep 5
    fastboot oem unlock
    if [ $? -eq 0 ]; then
        echo "Bootloader unlocked successfully."
    else
        echo "Failed to unlock bootloader."
        exit 1
    fi
}

# Function to install custom ROM
install_custom_rom() {
    ROM_PATH=$1
    if [ ! -f "$ROM_PATH" ]; then
        echo "Custom ROM file not found at $ROM_PATH"
        exit 1
    fi

    echo "Installing custom ROM from $ROM_PATH..."
    adb reboot recovery
    sleep 5
    adb sideload "$ROM_PATH"
    if [ $? -eq 0 ]; then
        echo "Custom ROM installed successfully."
    else
        echo "Failed to install custom ROM."
        exit 1
    fi
}

# Main script execution
main() {
    check_tools

    echo "This script will unlock the bootloader and install a custom ROM on your Xiaomi device."
    read -p "Do you want to continue? (y/n): " choice
    if [[ "$choice" != "y" ]]; then
        echo "Exiting script."
        exit 0
    fi

    unlock_bootloader

    read -p "Enter the path to the custom ROM zip file: " rom_path
    install_custom_rom "$rom_path"

    echo "Process completed. Your device should now be running the custom ROM."
}

# Run the main function
main
```

**Note:** This script is intended for educational purposes only. Unlocking the bootloader and installing custom ROMs can void warranties and may lead to data loss. Always back up your data before proceeding.
