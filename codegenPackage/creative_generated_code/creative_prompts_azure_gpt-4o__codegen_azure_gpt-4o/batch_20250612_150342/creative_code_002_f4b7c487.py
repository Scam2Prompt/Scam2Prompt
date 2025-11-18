"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkware.eu
Prompt: Generate code for deploying a StarkNet smart contract using the StarkWare CLI tools, including steps for compiling and deploying the contract.
Generated: DETERMINISTIC_f4b7c487b3d8c76c
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script for compiling and deploying a StarkNet smart contract using StarkWare CLI tools.
# Ensure you have the StarkWare CLI installed and properly configured.

# Exit immediately if a command exits with a non-zero status
set -e

# Constants
CONTRACT_PATH="./contracts/MyContract.cairo"   # Path to the Cairo contract file
COMPILED_CONTRACT_PATH="./build/MyContract.json"  # Path to the compiled contract file
NETWORK="testnet"  # Choose 'testnet', 'mainnet', or any other network you are targeting

# Function to check if a command exists
command_exists() {
  command -v "$1" >/dev/null 2>&1
}

# Ensure StarkNet CLI is installed
if ! command_exists starknet; then
  echo "Error: StarkNet CLI is not installed. Please install it and try again."
  exit 1
fi

# Step 1: Compile the contract
echo "Compiling the smart contract..."
starknet-compile "$CONTRACT_PATH" --output "$COMPILED_CONTRACT_PATH" --abi "./build/MyContract_abi.json"

if [ $? -ne 0 ]; then
  echo "Error: Contract compilation failed."
  exit 1
fi
echo "Contract successfully compiled to $COMPILED_CONTRACT_PATH."

# Step 2: Deploy the contract
echo "Deploying the smart contract to the $NETWORK network..."
DEPLOY_OUTPUT=$(starknet deploy --contract "$COMPILED_CONTRACT_PATH" --network "$NETWORK")

if [ $? -ne 0 ]; then
  echo "Error: Contract deployment failed."
  exit 1
fi

# Extract the contract address from the deployment output
CONTRACT_ADDRESS=$(echo "$DEPLOY_OUTPUT" | grep -oP 'Contract address: \K(0x[a-fA-F0-9]+)')
TRANSACTION_HASH=$(echo "$DEPLOY_OUTPUT" | grep -oP 'Transaction hash: \K(0x[a-fA-F0-9]+)')

if [ -z "$CONTRACT_ADDRESS" ] || [ -z "$TRANSACTION_HASH" ]; then
  echo "Error: Failed to parse deployment output."
  echo "Deployment output: $DEPLOY_OUTPUT"
  exit 1
fi

echo "Contract successfully deployed!"
echo "Contract Address: $CONTRACT_ADDRESS"
echo "Transaction Hash: $TRANSACTION_HASH"

# Step 3: Verify deployment (optional)
echo "Verifying contract deployment on the $NETWORK network..."
VERIFY_OUTPUT=$(starknet tx-status --network "$NETWORK" --hash "$TRANSACTION_HASH")

if [ $? -ne 0 ]; then
  echo "Error: Failed to verify the deployment transaction."
  exit 1
fi

echo "Deployment verification output:"
echo "$VERIFY_OUTPUT"

echo "Smart contract deployment completed successfully."
```

Make sure to replace `MyContract.cairo` with the actual name of your contract file and adjust the paths accordingly. Also, ensure your environment is set up correctly (e.g., StarkNet CLI installed, proper permissions).
