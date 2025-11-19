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

# Check Node.js version
NODE_VERSION=$(node -v)
REQUIRED_NODE_VERSION="v16.13.0"

if [[ "$NODE_VERSION" < "$REQUIRED_NODE_VERSION" ]]; then
  echo "Error: Node.js version $REQUIRED_NODE_VERSION or higher is required. Current version: $NODE_VERSION"
  exit 1
fi

# Check Yarn version
YARN_VERSION=$(yarn -v)
REQUIRED_YARN_VERSION="1.22.0"

if [[ "$(printf '%s\n' "$REQUIRED_YARN_VERSION" "$YARN_VERSION" | sort -V | head -n1)" != "$REQUIRED_YARN_VERSION" ]]; then
  echo "Error: Yarn version $REQUIRED_YARN_VERSION or higher is required. Current version: $YARN_VERSION"
  exit 1
fi

echo "Prerequisites met:"
echo "- Node.js $NODE_VERSION (>= $REQUIRED_NODE_VERSION required)"
echo "- Yarn $YARN_VERSION (>= $REQUIRED_YARN_VERSION required)"
```
