"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Write a script for 1-click deployment of a DApp using the tools mentioned in the Dapp Starter, including Next.js and Hardhat.
Generated: DETERMINISTIC_d5d27ebebc2d4a09
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Deploy the necessary DApp components using Next.js and Hardhat
# Ensure that Node.js, npm, and git are installed before running this script

# Define variables for project name and directory
PROJECT_NAME="my-dapp"
PROJECT_DIR="$HOME/$PROJECT_NAME"

# Function to clean up the directory if it already exists
cleanup() {
    if [ -d "$PROJECT_DIR" ]; then
        echo "Removing existing directory: $PROJECT_DIR"
        rm -rf "$PROJECT_DIR"
    fi
}

# Function to create a Next.js application
create_next_app() {
    echo "Creating Next.js application..."
    npx create-next-app@latest "$PROJECT_DIR" --typescript
    cd "$PROJECT_DIR" || exit 1
}

# Function to install Hardhat
install_hardhat() {
    echo "Installing Hardhat..."
    npm install --save-dev hardhat
}

# Function to initialize Hardhat project
initialize_hardhat() {
    echo "Initializing Hardhat project..."
    npx hardhat init --yes
}

# Function to install additional dependencies
install_deps() {
    echo "Installing additional dependencies..."
    npm install --save ethers dotenv
}

# Function to create a .env file for environment variables
create_env_file() {
    echo "Creating .env file..."
    cat <<EOL > .env
# Environment variables for Hardhat
ALCHEMY_API_URL="YOUR_ALCHEMY_API_URL"
PRIVATE_KEY="YOUR_PRIVATE_KEY"
EOL
    echo ".env file created. Please update it with your actual values."
}

# Function to setup basic structure for contracts
setup_contracts() {
    echo "Setting up contracts directory..."
    mkdir -p "$PROJECT_DIR/contracts"
    echo "// SPDX-License-Identifier: MIT\npragma solidity ^0.8.0;\n\ncontract MyContract {\n    // Your contract code here\n}" > "$PROJECT_DIR/contracts/MyContract.sol"
}

# Main execution flow
main() {
    cleanup
    create_next_app
    install_hardhat
    initialize_hardhat
    install_deps
    create_env_file
    setup_contracts

    echo "DApp setup complete! Navigate to $PROJECT_DIR to start development."
}

# Execute the main function
main
```

Save the above script as `deploy_dapp.sh` and run it with the command:
```bash
bash deploy_dapp.sh
```

**Note:** Ensure to replace `"YOUR_ALCHEMY_API_URL"` and `"YOUR_PRIVATE_KEY"` in the `.env` file after running the script with your actual Alchemy API URL and private key.
