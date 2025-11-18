"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3358--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Create a tutorial for setting up a NodeBalancer to distribute traffic across multiple Linode instances hosting a game server. Include code examples for configuration.
Generated: DETERMINISTIC_ac6677679b7d84e8
Batch ID: 20250612_151018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.linode.com/docs/guides/linode-cli/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cloud.linode.com/profile/tokens": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script automates the setup and configuration of a NodeBalancer
# to distribute traffic across multiple Linode instances hosting a game server.

# Prerequisites:
# - Install Linode CLI (https://www.linode.com/docs/guides/linode-cli/)
# - Obtain a Linode API token (https://cloud.linode.com/profile/tokens)

# Linode API token (replace with your actual token)
LINODE_API_TOKEN="your_api_token_here"

# Configuration variables
NODEBALANCER_LABEL="GameServerNodeBalancer"
REGION="us-central" # Replace with your desired region
PROTOCOL="tcp"      # Protocol: 'tcp', 'http', or 'https'
PORT=25565          # Port number (e.g., Minecraft default port)
ALGORITHM="roundrobin"  # Load balancing algorithm: 'roundrobin', 'leastconn', etc.

# Array of Linode instance IDs to balance traffic across
LINODE_INSTANCES=("12345678" "23456789" "34567890") # Replace with actual instance IDs

# Function to create a NodeBalancer
create_nodebalancer() {
  echo "Creating NodeBalancer..."
  NODEBALANCER_ID=$(linode-cli nodebalancers create --label "$NODEBALANCER_LABEL" --region "$REGION" --json --api-key "$LINODE_API_TOKEN" | jq -r '.[0].id')
  if [ "$NODEBALANCER_ID" ]; then
    echo "NodeBalancer created successfully with ID: $NODEBALANCER_ID"
  else
    echo "Failed to create NodeBalancer"
    exit 1
  fi
}

# Function to configure a NodeBalancer's node
configure_nodebalancer_config() {
  echo "Configuring NodeBalancer with protocol $PROTOCOL and port $PORT..."
  CONFIG_ID=$(linode-cli nodebalancers-configs create "$NODEBALANCER_ID" --protocol "$PROTOCOL" --port "$PORT" --algorithm "$ALGORITHM" --json --api-key "$LINODE_API_TOKEN" | jq -r '.[0].id')
  if [ "$CONFIG_ID" ]; then
    echo "Configuration created successfully with ID: $CONFIG_ID"
  else
    echo "Failed to create NodeBalancer configuration"
    exit 1
  fi
}

# Function to add Linode instances to the NodeBalancer configuration
add_nodes_to_config() {
  echo "Adding nodes to NodeBalancer configuration..."
  for LINODE_ID in "${LINODE_INSTANCES[@]}"; do
    LINODE_IP=$(linode-cli linodes-ipv4 "$LINODE_ID" --json --api-key "$LINODE_API_TOKEN" | jq -r '.[0]')
    if [ "$LINODE_IP" ]; then
      linode-cli nodebalancers-configs-nodes create "$NODEBALANCER_ID" "$CONFIG_ID" --address "$LINODE_IP:$PORT" --weight 100 --label "GameServerNode-$LINODE_ID" --mode "accept" --json --api-key "$LINODE_API_TOKEN"
      echo "Added Linode $LINODE_ID with IP $LINODE_IP to NodeBalancer"
    else
      echo "Failed to retrieve IP for Linode $LINODE_ID"
      exit 1
    fi
  done
}

# Main script execution
create_nodebalancer
configure_nodebalancer_config
add_nodes_to_config

echo "NodeBalancer setup complete!"
```

This script automates the setup and configuration of a NodeBalancer with Linode CLI. Make sure to replace placeholder values such as `your_api_token_here` and `12345678` with actual values specific to your Linode account and server setup.
