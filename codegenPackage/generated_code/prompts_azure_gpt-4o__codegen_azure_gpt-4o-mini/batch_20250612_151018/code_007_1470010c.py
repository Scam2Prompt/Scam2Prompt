"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3352--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Provide an example of how to use Linode's CLI to monitor resource usage (CPU, memory, and disk) across multiple Linode instances.
Generated: DETERMINISTIC_1470010c5cb5e8b5
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# This script monitors CPU, memory, and disk usage across multiple Linode instances
# using Linode's CLI. Ensure you have the Linode CLI installed and configured.

# Function to check if Linode CLI is installed
check_linode_cli() {
    if ! command -v linode &> /dev/null; then
        echo "Linode CLI is not installed. Please install it and configure your API token."
        exit 1
    fi
}

# Function to fetch and display resource usage for a given Linode ID
monitor_linode() {
    local linode_id=$1

    # Fetch Linode details using the Linode CLI
    linode_info=$(linode-cli linodes view "$linode_id" --json)

    # Check if the command was successful
    if [ $? -ne 0 ]; then
        echo "Error fetching details for Linode ID: $linode_id"
        return
    fi

    # Extract relevant information
    linode_label=$(echo "$linode_info" | jq -r '.label')
    cpu_usage=$(echo "$linode_info" | jq -r '.cpu')
    memory_usage=$(echo "$linode_info" | jq -r '.memory')
    disk_usage=$(echo "$linode_info" | jq -r '.disk')

    # Display the resource usage
    echo "Linode ID: $linode_id"
    echo "Label: $linode_label"
    echo "CPU Usage: $cpu_usage%"
    echo "Memory Usage: $memory_usage MB"
    echo "Disk Usage: $disk_usage MB"
    echo "-----------------------------------"
}

# Main script execution
check_linode_cli

# List of Linode IDs to monitor (replace with your actual Linode IDs)
linode_ids=("123456" "234567" "345678")

# Loop through each Linode ID and monitor its resource usage
for linode_id in "${linode_ids[@]}"; do
    monitor_linode "$linode_id"
done
```

**Note:** Replace the `linode_ids` array with your actual Linode instance IDs. Ensure you have `jq` installed for JSON parsing.
