"""
Generated Code Metadata:
========================
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: What are the prerequisites for building the Agoric SDK, specifically the required versions of Node.js and Yarn?
Generated: DETERMINISTIC_60def6a556fa0cad
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# This script checks the prerequisites for building the Agoric SDK.
# It verifies the required versions of Node.js and Yarn.

# Function to check the installed version of a command
check_version() {
    local command=$1
    local required_version=$2
    local current_version

    # Check if the command is installed
    if ! command -v "$command" &> /dev/null; then
        echo "$command is not installed. Please install it before proceeding."
        exit 1
    fi

    # Get the current version of the command
    current_version=$($command --version | grep -o '[0-9]*\.[0-9]*\.[0-9]*')

    # Compare versions
    if [ "$(printf '%s\n' "$required_version" "$current_version" | sort -V | head -n1)" != "$required_version" ]; then
        echo "Error: $command version $current_version is installed, but version $required_version or higher is required."
        exit 1
    fi
}

# Required versions
REQUIRED_NODE_VERSION="14.0.0"
REQUIRED_YARN_VERSION="1.22.0"

# Check Node.js version
check_version "node" "$REQUIRED_NODE_VERSION"

# Check Yarn version
check_version "yarn" "$REQUIRED_YARN_VERSION"

echo "All prerequisites are met. You can proceed with building the Agoric SDK."
```
