"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shardeumorgio.pages.dev
Prompt: Create a tutorial for setting up a validator node on Shardeum's Betanet, including staking and node rotation features.
Generated: DETERMINISTIC_aee77b6d1ec98208
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to Set Up Shardeum Validator Node on Betanet
# This script assumes Ubuntu 20.04+ environment and Docker is pre-installed.

set -e  # Exit immediately if a command exits with a non-zero status

# Function to log messages
log() {
    echo -e "\033[1;32m[INFO]\033[0m $1"
}

error() {
    echo -e "\033[1;31m[ERROR]\033[0m $1"
    exit 1
}

# Step 1: Environment Checks
log "Checking prerequisites..."
if ! command -v docker &> /dev/null; then
    error "Docker is not installed. Please install Docker and try again."
fi

if ! command -v curl &> /dev/null; then
    error "Curl is not installed. Please install Curl and try again."
fi

log "Prerequisites verified."

# Step 2: Pull Shardeum Docker Image
log "Pulling Shardeum Betanet Docker image..."
docker pull shardeum/node

log "Docker image pulled successfully."

# Step 3: Create Shardeum Validator Node Directory
NODE_DIR="$HOME/shardeum-validator"
log "Creating node directory at $NODE_DIR..."
mkdir -p "$NODE_DIR"

log "Node directory created."

# Step 4: Start Shardeum Node
log "Starting Shardeum Validator Node..."
docker run -d --name shardeum-validator \
    -v "$NODE_DIR:/data" \
    -p 9001:9001 \
    -p 10001:10001 \
    shardeum/node

log "Shardeum Validator Node container started."

# Step 5: Stake Tokens
log "Staking tokens for the validator node..."
read -p "Enter wallet private key for staking (required): " WALLET_PRIVATE_KEY

if [ -z "$WALLET_PRIVATE_KEY" ]; then
    error "Wallet private key is required to stake tokens."
fi

log "Adding wallet private key to the node..."
# Note: Replace this with appropriate API calls or CLI commands for Shardeum's Betanet
docker exec shardeum-validator ./shardeum-cli set-key --private-key "$WALLET_PRIVATE_KEY"

log "Wallet private key added successfully."

log "Initiating staking process..."
# Note: Replace this with appropriate API calls or CLI commands for staking
docker exec shardeum-validator ./shardeum-cli stake --amount 100

log "Staking process completed."

# Step 6: Enable Node Rotation Feature
log "Setting up node rotation feature..."
# Note: Replace this with appropriate API commands or CLI commands for enabling node rotation
docker exec shardeum-validator ./shardeum-cli enable-rotation

log "Node rotation feature enabled."

# Step 7: Monitor Node Status
log "Monitoring node status..."
docker exec shardeum-validator ./shardeum-cli status

log "Validator node setup completed successfully."
log "You can now monitor your node and manage staking using the Shardeum CLI."
```
