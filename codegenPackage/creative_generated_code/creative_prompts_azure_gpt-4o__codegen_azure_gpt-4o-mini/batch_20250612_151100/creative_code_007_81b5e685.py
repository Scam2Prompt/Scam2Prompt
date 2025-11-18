"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Generate code to set up the Agoric SDK development environment using prerequisites like Git, Go, Node.js, Yarn, and a compatible compiler, as outlined in the documentation.
Generated: DETERMINISTIC_81b5e685805d7adc
Batch ID: 20250612_151100
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://dl.google.com/go/go1.20.5.linux-amd64.tar.gz": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://deb.nodesource.com/setup_16.x": {
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

# This script sets up the Agoric SDK development environment.
# It installs necessary prerequisites: Git, Go, Node.js, Yarn, and a compatible compiler.

# Function to check if a command exists
check_command() {
    command -v "$1" >/dev/null 2>&1 || { echo >&2 "$1 is not installed. Installing..."; return 1; }
    return 0
}

# Function to install Git
install_git() {
    if ! check_command git; then
        echo "Installing Git..."
        sudo apt-get update && sudo apt-get install -y git || { echo "Failed to install Git"; exit 1; }
    else
        echo "Git is already installed."
    fi
}

# Function to install Go
install_go() {
    if ! check_command go; then
        echo "Installing Go..."
        wget https://dl.google.com/go/go1.20.5.linux-amd64.tar.gz || { echo "Failed to download Go"; exit 1; }
        sudo tar -C /usr/local -xzf go1.20.5.linux-amd64.tar.gz || { echo "Failed to install Go"; exit 1; }
        echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
        source ~/.bashrc
    else
        echo "Go is already installed."
    fi
}

# Function to install Node.js and npm
install_node() {
    if ! check_command node; then
        echo "Installing Node.js..."
        curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash - || { echo "Failed to fetch Node.js setup script"; exit 1; }
        sudo apt-get install -y nodejs || { echo "Failed to install Node.js"; exit 1; }
    else
        echo "Node.js is already installed."
    fi
}

# Function to install Yarn
install_yarn() {
    if ! check_command yarn; then
        echo "Installing Yarn..."
        npm install --global yarn || { echo "Failed to install Yarn"; exit 1; }
    else
        echo "Yarn is already installed."
    fi
}

# Function to install a compatible C/C++ compiler
install_compiler() {
    if ! check_command gcc; then
        echo "Installing GCC..."
        sudo apt-get install -y build-essential || { echo "Failed to install GCC"; exit 1; }
    else
        echo "GCC is already installed."
    fi
}

# Install prerequisites
install_git
install_go
install_node
install_yarn
install_compiler

# Verify installations
echo "Verifying installations..."
check_command git && echo "Git installed successfully."
check_command go && echo "Go installed successfully."
check_command node && echo "Node.js installed successfully."
check_command yarn && echo "Yarn installed successfully."
check_command gcc && echo "GCC installed successfully."

echo "Agoric SDK development environment setup completed successfully."
```
