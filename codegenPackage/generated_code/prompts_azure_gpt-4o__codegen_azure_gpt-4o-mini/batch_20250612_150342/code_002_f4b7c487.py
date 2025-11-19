"""
Generated Code Metadata:
========================
Original URL: https://starkware.eu
Prompt: Generate code for deploying a StarkNet smart contract using the StarkWare CLI tools, including steps for compiling and deploying the contract.
Generated: DETERMINISTIC_f4b7c487b3d8c76c
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# This script compiles and deploys a StarkNet smart contract using StarkWare CLI tools.

# Set the contract file name and the network to deploy to
CONTRACT_FILE="path/to/your_contract.cairo"
NETWORK="alpha"  # Change to 'testnet' or 'mainnet' as needed

# Function to compile the smart contract
compile_contract() {
    echo "Compiling the smart contract..."
    starknet-compile $CONTRACT_FILE --output $CONTRACT_FILE.json
    if [ $? -ne 0 ]; then
        echo "Error: Contract compilation failed."
        exit 1
    fi
    echo "Contract compiled successfully."
}

# Function to deploy the smart contract
deploy_contract() {
    echo "Deploying the smart contract..."
    DEPLOY_OUTPUT=$(starknet deploy --contract $CONTRACT_FILE.json --network $NETWORK)
    if [ $? -ne 0 ]; then
        echo "Error: Contract deployment failed."
        exit 1
    fi
    echo "Contract deployed successfully."
    echo "Deployment output: $DEPLOY_OUTPUT"
}

# Main execution flow
compile_contract
deploy_contract
```

### Usage Instructions:
1. Save the script to a file, e.g., `deploy_starknet.sh`.
2. Make the script executable: `chmod +x deploy_starknet.sh`.
3. Run the script: `./deploy_starknet.sh`.

### Note:
- Ensure you have the StarkWare CLI tools installed and configured properly.
- Replace `path/to/your_contract.cairo` with the actual path to your Cairo smart contract file.
