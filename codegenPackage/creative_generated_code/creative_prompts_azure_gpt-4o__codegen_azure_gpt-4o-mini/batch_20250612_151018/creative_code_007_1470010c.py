"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3352--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Provide an example of how to use Linode's CLI to monitor resource usage (CPU, memory, and disk) across multiple Linode instances.
Generated: DETERMINISTIC_1470010c5cb5e8b5
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script monitors CPU, memory, and disk usage across multiple Linode instances
# Usage: ./monitor_linodes.sh <API_TOKEN>

# Check if the API token is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <API_TOKEN>"
    exit 1
fi

API_TOKEN=$1

# Function to fetch and display resource usage of a Linode instance
monitor_linode() {
    local linode_id=$1
    
    # Fetch Linode details using Linode CLI
    linode-cli linodes show $linode_id --json | jq -r '[
        .label,
        .status,
        .specs.cpu,
        .specs.memory,
        .specs.disk,
        .uptime,
        .networking[0].ingress,
        .networking[0].egress
    ] | @csv' | sed 's/"//g'
}

# Fetch the list of Linode instances
linodes=$(linode-cli linodes list --json)

# Check if the Linode CLI command was successful
if [ $? -ne 0 ]; then
    echo "Error fetching Linode instances. Please check your API token and Linode CLI installation."
    exit 1
fi

# Print header
echo "Linode Monitor - Resource Usage"
echo "---------------------------------"
echo "Label,Status,CPU,Memory (MB),Disk (MB),Uptime,Ingress (MB),Egress (MB)"

# Loop through each Linode instance and display resource usage
echo "$linodes" | jq -c '.[]' | while IFS= read -r linode; do
    linode_id=$(echo "$linode" | jq -r '.id')
    monitor_linode $linode_id
done

# End of script
```

**Note**: Ensure that `jq` is installed on your system to process JSON outputs. You can install it via your package manager (e.g., `apt-get install jq` for Debian-based systems, or `brew install jq` for macOS). Additionally, you must have the Linode CLI installed and configured properly to use this script.
