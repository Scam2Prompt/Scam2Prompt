"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Write a script for 1-click deployment of a DApp using the tools mentioned in the Dapp Starter, including Next.js and Hardhat.
Generated: DETERMINISTIC_d5d27ebebc2d4a09
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# DApp Deployment Script
# This script automates the deployment of a decentralized application (DApp)
# using Next.js for the frontend and Hardhat for the Ethereum smart contracts.

# Exit immediately if a command exits with a non-zero status
set -e

# Function to install dependencies
install_dependencies() {
    echo "Installing dependencies..."
    npm install
}

# Function to compile smart contracts
compile_contracts() {
    echo "Compiling smart contracts..."
    npx hardhat compile
}

# Function to deploy smart contracts
deploy_contracts() {
    echo "Deploying smart contracts..."
    npx hardhat run scripts/deploy.js --network localhost
}

# Function to start the Next.js application
start_next_app() {
    echo "Starting Next.js application..."
    npm run dev
}

# Function to check if Hardhat is installed
check_hardhat() {
    if ! command -v npx &> /dev/null; then
        echo "npx could not be found. Please install Node.js and npm."
        exit 1
    fi
}

# Function to check if Next.js is installed
check_next() {
    if ! npm list next &> /dev/null; then
        echo "Next.js is not installed. Please run 'npm install next'."
        exit 1
    fi
}

# Main script execution
main() {
    check_hardhat
    check_next

    install_dependencies
    compile_contracts
    deploy_contracts
    start_next_app

    echo "DApp deployment completed successfully!"
}

# Run the main function
main
```

### Instructions to Use:
1. Save the script as `deploy_dapp.sh`.
2. Make the script executable: `chmod +x deploy_dapp.sh`.
3. Run the script: `./deploy_dapp.sh`.

### Note:
- Ensure that you have Node.js, npm, Hardhat, and Next.js installed before running the script.
- Modify the `deploy_contracts` function to specify the correct deployment script and network as needed.
