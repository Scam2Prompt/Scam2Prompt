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

# Linode NodeBalancer Configuration Script
# Creates a NodeBalancer and configures it to distribute traffic across backend nodes.

# Ensure linode-cli is installed and configured with proper API token
if ! command -v linode-cli &> /dev/null; then
    echo "Error: linode-cli is not installed. Please install it first."
    exit 1
fi

# Configuration variables
NODEBALANCER_LABEL="my-nodebalancer"
REGION="us-east"
BACKEND_NODES=("192.0.2.1" "192.0.2.2" "192.0.2.3")
PORT=80
PROTOCOL="http"
HEALTH_CHECK_TYPE="http"
HEALTH_CHECK_PATH="/health"
HEALTH_CHECK_INTERVAL=10
HEALTH_CHECK_TIMEOUT=5
HEALTH_CHECK_ATTEMPTS=3
STICKY_SESSIONS="none"
ALGORITHM="roundrobin"

# Create NodeBalancer
echo "Creating NodeBalancer..."
NODEBALANCER_ID=$(linode-cli nodebalancers create \
    --label "$NODEBALANCER_LABEL" \
    --region "$REGION" \
    --json | jq -r '.[0].id')

if [ -z "$NODEBALANCER_ID" ]; then
    echo "Error: Failed to create NodeBalancer."
    exit 1
fi

echo "NodeBalancer created with ID: $NODEBALANCER_ID"

# Create Configuration
echo "Creating NodeBalancer configuration..."
CONFIG_ID=$(linode-cli nodebalancers config-create \
    --nodebalancer-id "$NODEBALANCER_ID" \
    --port "$PORT" \
    --protocol "$PROTOCOL" \
    --check "$HEALTH_CHECK_TYPE" \
    --check_path "$HEALTH_CHECK_PATH" \
    --check_interval "$HEALTH_CHECK_INTERVAL" \
    --check_timeout "$HEALTH_CHECK_TIMEOUT" \
    --check_attempts "$HEALTH_CHECK_ATTEMPTS" \
    --stickiness "$STICKY_SESSIONS" \
    --algorithm "$ALGORITHM" \
    --json | jq -r '.[0].id')

if [ -z "$CONFIG_ID" ]; then
    echo "Error: Failed to create NodeBalancer configuration."
    exit 1
fi

echo "Configuration created with ID: $CONFIG_ID"

# Add Backend Nodes
echo "Adding backend nodes..."
for NODE_IP in "${BACKEND_NODES[@]}"; do
    NODE_ID=$(linode-cli nodebalancers node-create \
        --nodebalancer-id "$NODEBALANCER_ID" \
        --config-id "$CONFIG_ID" \
        --address "$NODE_IP:$PORT" \
        --weight 100 \
        --mode "accept" \
        --json | jq -r '.[0].id')

    if [ -z "$NODE_ID" ]; then
        echo "Error: Failed to add node $NODE_IP"
    else
        echo "Node $NODE_IP added successfully"
    fi
done

echo "NodeBalancer setup complete."
echo "NodeBalancer ID: $NODEBALANCER_ID"
echo "Configuration ID: $CONFIG_ID"
```
:$PORT" \
        --label "backend-$node" \
        --weight 100 \
        --mode "accept"
    
    if [ $? -ne 0 ]; then
        echo "Error: Failed to add backend node $node"
        # Continue to next node instead of exiting
        continue
    fi
done

echo "NodeBalancer setup complete!"
echo "NodeBalancer ID: $nodebalancer_id"
echo "Config ID: $config_id"
echo "You can now access your service via the NodeBalancer's IP address"
```
