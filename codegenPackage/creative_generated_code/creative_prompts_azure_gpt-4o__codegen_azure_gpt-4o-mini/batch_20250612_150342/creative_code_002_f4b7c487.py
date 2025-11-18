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

# This script demonstrates how to compile and deploy a StarkNet smart contract using StarkWare CLI tools.

# Define variables
CONTRACT_NAME="MySmartContract"  # Name of the smart contract file without extension
CONTRACT_FILE="${CONTRACT_NAME}.cairo"  # Path to the contract file
NETWORK="alpha"  # Specify the StarkNet network (e.g., alpha, testnet)
DEPLOYER_ACCOUNT="YOUR_DEPLOYER_ACCOUNT"  # Replace with your deployer account address

# Step 1: Compile the smart contract
echo "Compiling the smart contract..."
starknet-compile $CONTRACT_FILE --output "${CONTRACT_NAME}_compiled.json" --abi "${CONTRACT_NAME}_abi.json"

# Check if the compilation was successful
if [ $? -ne 0 ]; then
    echo "Error: Compilation failed."
    exit 1
fi

echo "Compilation successful. Compiled contract saved as ${CONTRACT_NAME}_compiled.json."

# Step 2: Deploy the smart contract
echo "Deploying the smart contract..."
DEPLOYED_CONTRACT_ADDRESS=$(starknet deploy --contract "${CONTRACT_NAME}_compiled.json" --network $NETWORK --account "$DEPLOYER_ACCOUNT" --wait)

# Check if the deployment was successful
if [ $? -ne 0 ]; then
    echo "Error: Deployment failed."
    exit 1
fi

echo "Deployment successful. Contract deployed at address: $DEPLOYED_CONTRACT_ADDRESS"

# Step 3: Output the ABI for reference
echo "ABI has been saved as ${CONTRACT_NAME}_abi.json"

# Step 4: Clean up if necessary (optional)
# Uncomment the line below if you want to remove compiled files after deployment
# rm "${CONTRACT_NAME}_compiled.json" "${CONTRACT_NAME}_abi.json"

echo "Deployment process complete."
```

### Instructions to Run the Script
1. Ensure you have the StarkNet CLI tools installed and configured properly.
2. Replace `YOUR_DEPLOYER_ACCOUNT` with your actual deployer account address.
3. Save this script as `deploy_starknet.sh`.
4. Make the script executable: `chmod +x deploy_starknet.sh`.
5. Run the script: `./deploy_starknet.sh`.
