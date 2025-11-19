"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3346--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: What are the steps to set up a NodeBalancer on Linode for my web application?
Generated: DETERMINISTIC_f763c8ae492b8c40
Batch ID: 20250612_163408
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.linode.com/v4/nodebalancers/$nb_id/configs": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.linode.com/v4/nodebalancers": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.linode.com/v4/nodebalancers/$nb_id/configs/$config_id/nodes": {
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

# Script to set up a NodeBalancer on Linode for a web application.
# Ensure you have the Linode CLI installed and API token configured before running.

# Variables
LINODE_API_TOKEN="your_api_token_here"  # Replace with your Linode API token
REGION="us-central"                    # Specify the desired Linode region (e.g., "us-central")
LABEL="my-nodebalancer"                # Label for the NodeBalancer
PORT=80                                # Port to listen on
PROTOCOL="http"                        # Protocol (http or https)
ALGORITHM="roundrobin"                 # Load balancing algorithm (roundrobin, leastconn, or source)
BACKEND_NODES=("192.168.1.1:80" "192.168.1.2:80")  # Backend nodes with IP:PORT format

# Function to create NodeBalancer
create_nodebalancer() {
  echo "Creating NodeBalancer..."
  local nb_id=$(curl -s \
    -H "Authorization: Bearer $LINODE_API_TOKEN" \
    -H "Content-Type: application/json" \
    -X POST \
    -d "{\"region\": \"$REGION\", \"label\": \"$LABEL\"}" \
    https://api.linode.com/v4/nodebalancers | jq -r '.id')

  if [[ -z "$nb_id" || "$nb_id" == "null" ]]; then
    echo "Error: Failed to create NodeBalancer"
    exit 1
  fi

  echo "NodeBalancer created with ID: $nb_id"
  echo "Configuring NodeBalancer port and protocol..."
  local config_id=$(curl -s \
    -H "Authorization: Bearer $LINODE_API_TOKEN" \
    -H "Content-Type: application/json" \
    -X POST \
    -d "{\"port\": $PORT, \"protocol\": \"$PROTOCOL\", \"algorithm\": \"$ALGORITHM\"}" \
    https://api.linode.com/v4/nodebalancers/$nb_id/configs | jq -r '.id')

  if [[ -z "$config_id" || "$config_id" == "null" ]]; then
    echo "Error: Failed to configure NodeBalancer"
    exit 1
  fi

  echo "NodeBalancer configuration created with ID: $config_id"
  echo "Adding backend nodes..."
  for node in "${BACKEND_NODES[@]}"; do
    local ip=$(echo $node | cut -d':' -f1)
    local port=$(echo $node | cut -d':' -f2)

    curl -s \
      -H "Authorization: Bearer $LINODE_API_TOKEN" \
      -H "Content-Type: application/json" \
      -X POST \
      -d "{\"address\": \"$ip:$port\", \"mode\": \"accept\"}" \
      https://api.linode.com/v4/nodebalancers/$nb_id/configs/$config_id/nodes > /dev/null

    echo "Backend node $ip:$port added successfully."
  done

  echo "NodeBalancer setup complete!"
}

# Main script execution
create_nodebalancer
```
