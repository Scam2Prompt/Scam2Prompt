"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.vercel.app
Prompt: Write a deployment script for a Next.js-based DApp starter kit that integrates blockchain tools like MetaMask, WalletConnect, and Hardhat.
Generated: DETERMINISTIC_00763a5d168128ad
Batch ID: 20250612_153647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Deployment script for a Next.js-based DApp starter kit
# This script integrates blockchain tools like MetaMask, WalletConnect, and Hardhat.

# Exit immediately if a command exits with a non-zero status
set -e

# Function to check if a command exists
check_command() {
    command -v "$1" >/dev/null 2>&1 || { echo >&2 "$1 is required but it's not installed. Aborting."; exit 1; }
}

# Check for required commands
check_command npm
check_command hardhat

# Define variables
PROJECT_NAME="dapp-starter-kit"
BUILD_DIR="./build"
DEPLOY_DIR="./deployment"

# Create directories if they don't exist
mkdir -p "$BUILD_DIR" "$DEPLOY_DIR"

# Step 1: Install dependencies
echo "Installing project dependencies..."
npm install

# Step 2: Build the Next.js application
echo "Building the Next.js application..."
npm run build

# Step 3: Compile smart contracts using Hardhat
echo "Compiling smart contracts..."
npx hardhat compile

# Step 4: Deploy smart contracts
echo "Deploying smart contracts..."
npx hardhat run scripts/deploy.js --network <your_network_here>

# Step 5: Copy built Next.js app to the deployment directory
echo "Copying built application to the deployment directory..."
cp -r .next "$DEPLOY_DIR/"

# Step 6: Prepare the deployment
echo "Preparing the deployment..."
cp -r public "$DEPLOY_DIR/"
cp package.json "$DEPLOY_DIR/"
cp -r scripts "$DEPLOY_DIR/"
cp -r styles "$DEPLOY_DIR/"

# Step 7: Install production dependencies in the deployment directory
echo "Installing production dependencies in the deployment directory..."
cd "$DEPLOY_DIR"
npm install --production

# Step 8: Start the application in production mode
echo "Starting the application in production mode..."
npm start &

# Step 9: Clean up (optional)
cd ..
echo "Cleaning up build files..."
rm -rf "$BUILD_DIR"

# Print success message
echo "Deployment completed successfully!"
```

Make sure to replace `<your_network_here>` with the actual network you intend to deploy your contracts to. Adjust any paths or commands as necessary to fit your specific project structure and requirements.
