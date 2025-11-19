"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: What are the steps to initialize a new Agoric project and start the development server?
Generated: DETERMINISTIC_b876edccf3e360a5
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Initialize a new Agoric project and start the development server

# Step 1: Ensure Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Node.js is not installed. Please install Node.js version 14 or higher."
    exit 1
fi

# Step 2: Install the Agoric CLI globally
echo "Installing Agoric CLI..."
npm install -g @agoric/cli

# Step 3: Create a new Agoric project
PROJECT_NAME="my-agoric-project"
echo "Creating a new Agoric project: $PROJECT_NAME"
agoric init $PROJECT_NAME || { echo "Failed to initialize Agoric project."; exit 1; }

# Step 4: Navigate into the project directory
cd $PROJECT_NAME || { echo "Failed to enter directory: $PROJECT_NAME."; exit 1; }

# Step 5: Install project dependencies
echo "Installing project dependencies..."
npm install || { echo "Failed to install dependencies."; exit 1; }

# Step 6: Start the development server
echo "Starting the Agoric development server..."
agoric start || { echo "Failed to start the development server."; exit 1; }

echo "Agoric project initialized and development server is running!"
```
