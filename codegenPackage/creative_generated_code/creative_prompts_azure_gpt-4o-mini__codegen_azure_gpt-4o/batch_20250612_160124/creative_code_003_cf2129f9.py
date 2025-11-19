"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monad.docsbot.app
Prompt: Explain how to set up a development environment for Monad using the supported Ethereum developer tools listed in the Tooling and Infrastructure section.
Generated: DETERMINISTIC_cf2129f9c4971b02
Batch ID: 20250612_160124
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://deb.nodesource.com/setup_lts.x": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/monad-xyz/monad.git": {
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

# Script to set up a development environment for Monad using Ethereum developer tools

# Exit immediately if a command exits with a non-zero status
set -e

# Function to check if a command-line tool is installed
check_command() {
  if ! command -v "$1" &> /dev/null; then
    echo "$1 is not installed. Please install it to proceed."
    exit 1
  fi
}

# Check for necessary command-line tools
check_command curl
check_command git
check_command npm

# Update package lists
echo "Updating package lists..."
sudo apt update

# Install Node.js and npm (if not installed)
if ! command -v node &> /dev/null || ! command -v npm &> /dev/null; then
  echo "Installing Node.js and npm..."
  curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
  sudo apt install -y nodejs
fi

# Verify Node.js and npm installation
echo "Node.js version: $(node -v)"
echo "npm version: $(npm -v)"

# Install Truffle framework for Ethereum development
echo "Installing Truffle..."
npm install -g truffle
echo "Truffle version: $(truffle version)"

# Install Ganache CLI (Ethereum blockchain simulator for local development)
echo "Installing Ganache CLI..."
npm install -g ganache-cli
echo "Ganache CLI version: $(ganache-cli --version)"

# Clone Monad development repository
echo "Cloning Monad development repository..."
git clone https://github.com/monad-xyz/monad.git
cd monad

# Install project dependencies using npm
echo "Installing project dependencies..."
npm install

# Start Ganache CLI for local blockchain simulation (default port 8545)
echo "Starting Ganache CLI..."
ganache-cli &

# Optionally, install Solidity compiler globally
echo "Installing Solidity compiler..."
npm install -g solc
echo "Solidity version: $(solcjs --version)"

# Display setup completion message
echo "Development environment for Monad set up successfully!"
echo "You can now start building and testing your Ethereum-based application using Monad."
```

This script sets up a development environment for Monad using popular Ethereum developer tools such as Truffle and Ganache CLI. Run it on a Linux-based system with `bash`. Ensure you have `curl`, `git`, and `npm` installed before proceeding.
