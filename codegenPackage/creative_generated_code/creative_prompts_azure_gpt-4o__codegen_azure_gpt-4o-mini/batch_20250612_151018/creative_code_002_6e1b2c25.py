"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3330--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Provide a script using Linode's CLI to configure NodeBalancers for load balancing across multiple web servers.
Generated: DETERMINISTIC_6e1b2c256fba7895
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

# This script configures NodeBalancers on Linode for load balancing across multiple web servers.

# Exit on any error
set -e

# Constants
NODEBALANCER_TYPE="lb2" # Modify as needed for your NodeBalancer type
REGION="us-east" # Modify to your desired region
NODEBALANCER_LABEL="my-nodebalancer" # Label for the NodeBalancer
BACKEND_SERVERS=("192.0.2.1" "192.0.2.2") # Replace with your backend server IPs
PORT=80 # Port for HTTP traffic

# Function to create a NodeBalancer
create_nodebalancer() {
    echo "Creating NodeBalancer..."
    linode-cli nodebalancers create --type $NODEBALANCER_TYPE --region $REGION --label $NODEBALANCER_LABEL
    
    echo "NodeBalancer created. Waiting for it to become active..."
    sleep 10
}

# Function to configure backend servers
configure_backends() {
    echo "Configuring backend servers..."
    NODEBALANCER_ID=$(linode-cli nodebalancers list | grep "$NODEBALANCER_LABEL" | awk '{print $2}')
    
    for server in "${BACKEND_SERVERS[@]}"; do
        linode-cli nodebalancers add-backend --nodebalancer-id $NODEBALANCER_ID --address $server --port $PORT
        echo "Added backend server: $server"
    done
}

# Function to set NodeBalancer configuration
configure_nodebalancer() {
    echo "Setting NodeBalancer configuration..."
    linode-cli nodebalancers update --id $NODEBALANCER_ID --check_interval 5 --check_timeout 5 --check_pass --check_fail 2
    echo "NodeBalancer configuration updated."
}

# Main script execution
main() {
    create_nodebalancer
    configure_backends
    configure_nodebalancer
    echo "NodeBalancer setup completed successfully."
}

# Run the main function
main
```

Make sure you have the `linode-cli` installed and configured with your API token before running this script. Also, replace the placeholder values with your actual configurations.
