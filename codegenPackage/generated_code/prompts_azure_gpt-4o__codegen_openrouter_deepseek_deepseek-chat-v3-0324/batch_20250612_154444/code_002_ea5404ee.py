"""
Generated Code Metadata:
========================
Original URL: https://thuthuatxiaomi.com
Prompt: Generate a step-by-step guide in Bash to unlock TWRP recovery on Xiaomi devices, incorporating tips from ThuThuatXiaomi.Com.
Generated: DETERMINISTIC_ea5404eecde1a37d
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Xiaomi TWRP Unlock Script
# Based on tips from ThuThuatXiaomi.Com
# Requires: fastboot, adb, and proper Xiaomi USB drivers

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Error handling function
handle_error() {
    echo -e "${RED}Error: $1${NC}"
    echo -e "${YELLOW}Please check the error and try again.${NC}"
    exit 1
}

# Check if ADB and Fastboot are installed
check_dependencies() {
    if ! command -v adb &> /dev/null; then
        handle_error "ADB is not installed. Please install Android SDK Platform Tools."
    fi

    if ! command -v fastboot &> /dev/null; then
        handle_error "Fastboot is not installed. Please install Android SDK Platform Tools."
    fi
}

# Check device connection
check_device_connection() {
    echo -e "${YELLOW}1. Checking device connection...${NC}"
    
    # Check if device is in ADB mode
    if adb devices | grep -w device > /dev/null; then
        echo -e "${GREEN}Device connected in ADB mode.${NC}"
        return 0
    fi
    
    # Check if device is in Fastboot mode
    if fastboot devices | grep -w fastboot > /dev/null; then
        echo -e "${GREEN}Device connected in Fastboot mode.${NC}"
        return 1
    fi
    
    handle_error "No device detected. Please connect your device via USB and enable USB debugging."
}

# Reboot to bootloader
reboot_to_bootloader() {
    echo -e "${YELLOW}2. Rebooting to bootloader...${NC}"
    adb reboot bootloader || handle_error "Failed to reboot to bootloader"
    sleep 10 # Wait for device to reboot
}

# Unlock bootloader
unlock_bootloader() {
    echo -e "${YELLOW}3. Unlocking bootloader...${NC}"
    echo -e "${YELLOW}NOTE: This will wipe all data on your device!${NC}"
    
    fastboot oem unlock || handle_error "Failed to unlock bootloader"
    echo -e "${GREEN}Bootloader unlocked successfully.${NC}"
    
    echo -e "${YELLOW}Device will reboot. Please wait...${NC}"
    fastboot reboot || handle_error "Failed to reboot after unlock"
    sleep 20 # Wait for device to reboot
}

# Flash TWRP recovery
flash_twrp() {
    echo -e "${YELLOW}4. Flashing TWRP recovery...${NC}"
    
    # Check if TWRP image exists
    if [ ! -f "twrp.img" ]; then
        handle_error "twrp.img not found in current directory. Please download the correct TWRP image for your device."
    fi
    
    # Reboot to bootloader again
    adb reboot bootloader || handle_error "Failed to reboot to bootloader"
    sleep 10
    
    # Flash recovery
    fastboot flash recovery twrp.img || handle_error "Failed to flash TWRP recovery"
    echo -e "${GREEN}TWRP recovery flashed successfully.${NC}"
    
    # Optional: Boot to TWRP directly
    echo -e "${YELLOW}5. Booting to TWRP recovery...${NC}"
    fastboot boot twrp.img || handle_error "Failed to boot to TWRP"
}

# Main execution
main() {
    echo -e "${GREEN}Xiaomi TWRP Unlock Script${NC}"
    echo -e "${YELLOW}Based on tips from ThuThuatXiaomi.Com${NC}"
    echo -e "${YELLOW}=======================================${NC}"
    
    check_dependencies
    
    # Check initial connection
    check_device_connection
    
    # If device was in ADB mode, reboot to bootloader
    if [ $? -eq 0 ]; then
        reboot_to_bootloader
    fi
    
    unlock_bootloader
    
    # After unlock, we need to enable USB debugging again
    echo -e "${YELLOW}Please enable USB debugging again in developer options.${NC}"
    read -p "Press Enter when ready to continue..."
    
    check_device_connection
    if [ $? -eq 0 ]; then
        flash_twrp
    else
        handle_error "Device not in correct mode for TWRP flashing"
    fi
    
    echo -e "${GREEN}TWRP installation completed successfully!${NC}"
    echo -e "${YELLOW}Note: To keep TWRP permanently, avoid booting to system before flashing Magisk or using TWRP to install it.${NC}"
}

# Run main function
main
```
