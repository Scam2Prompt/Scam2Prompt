"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Generate code to run unit tests for a specific package in the Agoric SDK, such as `eventual-send`, using the `yarn test` command as described in the documentation.
Generated: DETERMINISTIC_475776489e2fb681
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

# This script runs unit tests for a specific package in the Agoric SDK.

# Check if the package name is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <package-name>"
  echo "Example: $0 eventual-send"
  exit 1
fi

PACKAGE_NAME=$1

# Check if the package exists in the node_modules directory
if [ ! -d "node_modules/$PACKAGE_NAME" ]; then
  echo "Error: Package '$PACKAGE_NAME' not found in node_modules."
  exit 1
fi

# Navigate to the specified package directory
cd "node_modules/$PACKAGE_NAME" || {
  echo "Error: Could not navigate to package directory."
  exit 1
}

# Run the tests using yarn
echo "Running tests for package '$PACKAGE_NAME'..."
yarn test

# Check the exit status of the yarn test command
if [ $? -eq 0 ]; then
  echo "Tests completed successfully for package '$PACKAGE_NAME'."
else
  echo "Tests failed for package '$PACKAGE_NAME'."
  exit 1
fi

# Exit successfully
exit 0
```
