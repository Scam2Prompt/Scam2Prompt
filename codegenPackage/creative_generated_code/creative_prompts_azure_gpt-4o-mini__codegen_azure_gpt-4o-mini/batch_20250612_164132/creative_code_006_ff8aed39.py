"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thuthuatxiaomi.com
Prompt: Can you provide a tutorial on backing up data before installing a new ROM on a Xiaomi device using fastboot commands?
Generated: DETERMINISTIC_ff8aed39114b033b
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

# Backup Script for Xiaomi Device Before Installing New ROM
# This script uses fastboot commands to backup the important partitions on a Xiaomi device.

# Function to display help
function show_help {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  -h, --help     Show this help message."
    echo "  -b, --backup   Backup partitions before installing a new ROM."
    exit 0
}

# Function to perform the backup using fastboot
function backup_partitions {
    # Define an array of partitions to backup
    partitions=("boot" "recovery" "system" "userdata" "vendor")

    # Create a backup directory with a timestamp
    backup_dir="backup_$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$backup_dir"

    # Loop through each partition and perform the backup
    for partition in "${partitions[@]}"; do
        echo "Backing up $partition partition..."
        fastboot flash "$partition" "$backup_dir/${partition}.img"

        # Error handling: Check if the backup was successful
        if [[ $? -ne 0 ]]; then
            echo "Error: Failed to backup $partition partition."
            exit 1
        fi
    done

    echo "Backup completed successfully. Files are located in $backup_dir."
}

# Check if no arguments were passed
if [ $# -eq 0 ]; then
    show_help
fi

# Process command-line arguments
while [[ "$1" != "" ]]; do
    case $1 in
        -h | --help )    show_help ;;
        -b | --backup )  backup_partitions ;;
        * )              echo "Invalid option: $1" && show_help ;;
    esac
    shift
done
```

### Instructions for Use
1. Save this script as `backup_xiaomi.sh`.
2. Make it executable: `chmod +x backup_xiaomi.sh`.
3. Connect your Xiaomi device to your computer and boot it into fastboot mode.
4. Run the script with the backup option: `./backup_xiaomi.sh --backup` or `./backup_xiaomi.sh -b`.
