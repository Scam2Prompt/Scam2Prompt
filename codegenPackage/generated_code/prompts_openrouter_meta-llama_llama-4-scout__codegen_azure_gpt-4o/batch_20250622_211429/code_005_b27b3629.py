"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3352--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Generate a Linode CLI command to create a new NodeBalancer for load balancing web traffic.
Generated: DETERMINISTIC_b27b36295af40d2b
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

# This script creates a new NodeBalancer on Linode using the Linode CLI.
# Ensure you have the Linode CLI installed and configured with your API token before running this script.

# Variables
NODEBALANCER_LABEL="web-traffic-balancer"  # Label for the NodeBalancer
REGION="us-east"                          # Region where the NodeBalancer will be created
PORT=80                                   # Port to listen for HTTP traffic
PROTOCOL="http"                           # Protocol for the NodeBalancer
ALGORITHM="roundrobin"                    # Load balancing algorithm (roundrobin, leastconn, etc.)
STICKINESS="none"                         # Session stickiness (none, table, http_cookie)

# Create the NodeBalancer
create_nodebalancer() {
  echo "Creating NodeBalancer with label: $NODEBALANCER_LABEL in region: $REGION..."
  
  # Create the NodeBalancer
  NODEBALANCER_ID=$(linode-cli nodebalancers create \
    --label "$NODEBALANCER_LABEL" \
    --region "$REGION" \
    --json | jq -r '.[0].id')

  if [ -z "$NODEBALANCER_ID" ]; then
    echo "Error: Failed to create NodeBalancer."
    exit 1
  fi

  echo "NodeBalancer created successfully with ID: $NODEBALANCER_ID"

  # Configure the NodeBalancer port
  echo "Configuring NodeBalancer port $PORT for protocol $PROTOCOL..."
  linode-cli nodebalancers create-config \
    --nodebalancer-id "$NODEBALANCER_ID" \
    --port "$PORT" \
    --protocol "$PROTOCOL" \
    --algorithm "$ALGORITHM" \
    --stickiness "$STICKINESS" \
    --check "http" \
    --check-path "/" \
    --check-interval 10 \
    --check-timeout 5 \
    --check-attempts 3

  if [ $? -ne 0 ]; then
    echo "Error: Failed to configure NodeBalancer port."
    exit 1
  fi

  echo "NodeBalancer port $PORT configured successfully."
}

# Main execution
create_nodebalancer
```
