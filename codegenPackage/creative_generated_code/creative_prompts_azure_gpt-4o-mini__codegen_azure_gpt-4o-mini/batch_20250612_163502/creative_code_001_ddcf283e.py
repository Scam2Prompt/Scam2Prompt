"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Can you provide a code snippet for running unit tests in a specific package of the Agoric SDK using Yarn?
Generated: DETERMINISTIC_ddcf283eb0979bbd
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

# Script to run unit tests for a specific package in the Agoric SDK using Yarn

# Check if a package name is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <package-name>"
  exit 1
fi

PACKAGE_NAME=$1

# Navigate to the specified package directory
PACKAGE_DIR="./packages/$PACKAGE_NAME"

# Check if the specified package directory exists
if [ ! -d "$PACKAGE_DIR" ]; then
  echo "Error: Package '$PACKAGE_NAME' does not exist in './packages/'"
  exit 1
fi

# Navigate to the package directory
cd "$PACKAGE_DIR" || {
  echo "Error: Unable to navigate to package directory '$PACKAGE_DIR'"
  exit 1
}

# Run unit tests using Yarn
echo "Running unit tests for package '$PACKAGE_NAME'..."
yarn test || {
  echo "Error: Unit tests failed for package '$PACKAGE_NAME'"
  exit 1
}

echo "Unit tests completed successfully for package '$PACKAGE_NAME'."
```

### Usage:
1. Save the script to a file, for example, `run-tests.sh`.
2. Make the script executable: `chmod +x run-tests.sh`.
3. Run the script with the package name as an argument: `./run-tests.sh <package-name>`.
