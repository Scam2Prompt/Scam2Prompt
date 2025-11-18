"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Write a script to link the Agoric CLI using `yarn link-cli` and initialize a new project with `agoric init`, as described in the larger demo section of the documentation.
Generated: DETERMINISTIC_89b6509de6e37fec
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to link the Agoric CLI and initialize a new Agoric project.
# Ensure you have Agoric CLI installed before running this script.

# Constants
AGORIC_CLI_NAME="agoric-cli"
PROJECT_NAME="my-agoric-project"

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Step 1: Check if Yarn is installed
if ! command_exists yarn; then
    echo "Error: Yarn is not installed. Please install Yarn and try again."
    exit 1
fi

# Step 2: Check if Agoric CLI is installed globally
if ! command_exists $AGORIC_CLI_NAME; then
    echo "Error: Agoric CLI is not installed. Please install it globally using 'yarn global add agoric-cli'."
    exit 1
fi

# Step 3: Link the Agoric CLI
echo "Linking the Agoric CLI..."
yarn link-cli

# Check if linking was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to link the Agoric CLI. Please check the output and try again."
    exit 1
fi

# Step 4: Initialize a new Agoric project
echo "Initializing a new Agoric project named '$PROJECT_NAME'..."
agoric init $PROJECT_NAME

# Check if initialization was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to initialize the Agoric project. Please check the output and try again."
    exit 1
fi

echo "Agoric project '$PROJECT_NAME' has been successfully initialized."
```

Make sure to give execution permissions to the script before running it:

```bash
chmod +x script_name.sh
``` 

Replace `script_name.sh` with the actual name of your script file.
