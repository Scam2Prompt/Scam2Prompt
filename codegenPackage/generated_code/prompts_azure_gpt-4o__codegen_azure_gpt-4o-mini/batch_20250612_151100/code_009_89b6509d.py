"""
Generated Code Metadata:
========================
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Write a script to link the Agoric CLI using `yarn link-cli` and initialize a new project with `agoric init`, as described in the larger demo section of the documentation.
Generated: DETERMINISTIC_89b6509de6e37fec
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# This script links the Agoric CLI using `yarn link-cli` and initializes a new Agoric project.

# Function to print usage information
usage() {
    echo "Usage: $0 [project-name]"
    echo "  project-name: The name of the new Agoric project to initialize."
    exit 1
}

# Check if a project name is provided
if [ "$#" -ne 1 ]; then
    usage
fi

PROJECT_NAME=$1

# Function to link the Agoric CLI
link_agoric_cli() {
    echo "Linking Agoric CLI..."
    yarn link-cli
    if [ $? -ne 0 ]; then
        echo "Error: Failed to link Agoric CLI."
        exit 1
    fi
    echo "Agoric CLI linked successfully."
}

# Function to initialize a new Agoric project
init_agoric_project() {
    echo "Initializing new Agoric project: $PROJECT_NAME..."
    agoric init "$PROJECT_NAME"
    if [ $? -ne 0 ]; then
        echo "Error: Failed to initialize Agoric project."
        exit 1
    fi
    echo "Agoric project '$PROJECT_NAME' initialized successfully."
}

# Main script execution
link_agoric_cli
init_agoric_project

echo "Agoric CLI linked and project initialized successfully."
```

Make sure to give the script executable permissions before running it:

```bash
chmod +x script_name.sh
```

Replace `script_name.sh` with the actual name of your script file.
