"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: What commands are needed to build the "contract facet bundle" for Zoe contracts in the Agoric SDK?
Generated: DETERMINISTIC_372370a25b49adfa
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

# This script builds the "contract facet bundle" for Zoe contracts in the Agoric SDK.

# Ensure the script exits on error
set -e

# Define the SDK directory and output directory
AGORIC_SDK_DIR="./agoric-sdk"
OUTPUT_DIR="./contract-facet-bundle"

# Check if Agoric SDK directory exists
if [ ! -d "$AGORIC_SDK_DIR" ]; then
    echo "Error: Agoric SDK directory not found at $AGORIC_SDK_DIR"
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Navigate to the Agoric SDK directory
cd "$AGORIC_SDK_DIR"

# Build the Zoe contracts
echo "Building Zoe contracts..."
agoric build zoe-contracts --output "$OUTPUT_DIR" || {
    echo "Error: Failed to build Zoe contracts"
    exit 1
}

# Verify the built output
if [ ! -d "$OUTPUT_DIR" ]; then
    echo "Error: Output directory $OUTPUT_DIR not created."
    exit 1
fi

echo "Zoe contracts successfully built into $OUTPUT_DIR"
```
