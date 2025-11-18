"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-ebh.net
Prompt: Generate a script to deploy CentOS on a virtual machine, ensuring compatibility with Red Hat Enterprise Linux configurations.
Generated: DETERMINISTIC_894397143bdd37fa
Batch ID: 20250612_145427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to deploy CentOS on a virtual machine
# This script ensures compatibility with Red Hat Enterprise Linux configurations

# Function to display usage information
function usage() {
    echo "Usage: $0 <vm_name> <iso_path>"
    echo "  vm_name   : The name of the virtual machine to create"
    echo "  iso_path  : The path to the CentOS ISO file"
    exit 1
}

# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
    usage
fi

VM_NAME=$1
ISO_PATH=$2
VM_DIR="/var/lib/libvirt/images"
MEMORY="2048"  # Memory allocation in MB
CORES="2"      # Number of CPU cores

# Check if the provided ISO file exists
if [ ! -f "$ISO_PATH" ]; then
    echo "Error: ISO file not found at '$ISO_PATH'"
    exit 2
fi

# Check if the VM already exists
if virsh list --all | grep -q "$VM_NAME"; then
    echo "Error: A VM with the name '$VM_NAME' already exists."
    exit 3
fi

# Create a disk image for the VM
DISK_IMAGE="$VM_DIR/$VM_NAME.qcow2"
qemu-img create -f qcow2 "$DISK_IMAGE" 20G

# Check if the disk image creation was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to create disk image '$DISK_IMAGE'"
    exit 4
fi

# Create the VM using the specified ISO and configurations
virt-install \
    --name "$VM_NAME" \
    --ram "$MEMORY" \
    --vcpus="$CORES" \
    --disk path="$DISK_IMAGE",format=qcow2 \
    --cdrom "$ISO_PATH" \
    --os-type linux \
    --os-variant centos7.0 \
    --network bridge=virbr0 \
    --graphics none \
    --console pty,target_type=serial \
    --extra-args 'console=ttyS0,115200n8 serial' \
    --quiet

# Check if the VM installation was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to install VM '$VM_NAME'"
    exit 5
fi

echo "Success: VM '$VM_NAME' deployed successfully with CentOS."
exit 0
```

Make sure to run this script with appropriate permissions and ensure that `libvirt` and `virt-install` are installed and configured on your host system.
