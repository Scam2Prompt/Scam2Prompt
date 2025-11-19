"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3338--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Create a NodeBalancer configuration using Linode's CLI to distribute traffic across multiple backend nodes.
Generated: DETERMINISTIC_f977636b8815ca90
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# This script sets up a NodeBalancer configuration using Linode's CLI (linode-cli).
# It creates a NodeBalancer, configures it to distribute traffic across multiple backend nodes,
# and ensures proper error handling.

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display error messages and exit
error_exit() {
  echo "Error: $1" >&2
  exit 1
}

# Variables (replace these with your actual values)
API_TOKEN="your_linode_api_token" # Linode API token
REGION="us-east"                  # Region for the NodeBalancer
LABEL="my-nodebalancer"           # Label for the NodeBalancer
PROTOCOL="http"                   # Protocol (http, https, or tcp)
PORT=80                           # Port to listen on
ALGORITHM="roundrobin"            # Load balancing algorithm (roundrobin, leastconn, or source)
BACKEND_NODES=(                   # Backend nodes (IP:PORT format)
  "192.168.1.101:80"
  "192.168.1.102:80"
  "192.168.1.103:80"
)

# Check if linode-cli is installed
command -v linode-cli >/dev/null 2>&1 || error_exit "linode-cli is not installed. Please install it first."

# Authenticate linode-cli with the API token
linode-cli configure --token "$API_TOKEN" || error_exit "Failed to configure linode-cli with the API token."

# Create the NodeBalancer
NODEBALANCER_ID=$(linode-cli nodebalancers create --region "$REGION" --label "$LABEL" --json | jq -r '.[0].id') || error_exit "Failed to create NodeBalancer."

echo "NodeBalancer created with ID: $NODEBALANCER_ID"

# Create a configuration for the NodeBalancer
CONFIG_ID=$(linode-cli nodebalancers config-create "$NODEBALANCER_ID" \
  --protocol "$PROTOCOL" \
  --port "$PORT" \
  --algorithm "$ALGORITHM" \
  --json | jq -r '.[0].id') || error_exit "Failed to create NodeBalancer configuration."

echo "NodeBalancer configuration created with ID: $CONFIG_ID"

# Add backend nodes to the NodeBalancer configuration
for NODE in "${BACKEND_NODES[@]}"; do
  IFS=":" read -r IP PORT <<< "$NODE"
  linode-cli nodebalancers config-nodes-create "$NODEBALANCER_ID" "$CONFIG_ID" \
    --address "$IP" \
    --port "$PORT" \
    --mode "accept" || error_exit "Failed to add backend node $IP:$PORT."
  echo "Backend node $IP:$PORT added successfully."
done

echo "NodeBalancer setup complete."
```
T" \
        --weight 100 || error_exit "Failed to add backend node $IP:$PORT."
    echo "Backend node $IP:$PORT added successfully."
done

echo "NodeBalancer setup complete."
```
