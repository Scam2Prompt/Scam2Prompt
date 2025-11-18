"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-website-1ra.pages.dev
Prompt: Write code using the Wrangler CLI to deploy prebuilt assets directly to Cloudflare Pages, as described in the "Direct Upload Demo" on the Starknet Cloudflare Pages example project.
Generated: DETERMINISTIC_d3a221462445601f
Batch ID: 20250612_152006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script uses Wrangler CLI to deploy prebuilt assets directly to Cloudflare Pages.
# Ensure Wrangler is installed and authenticated before running this script.
# Prerequisites:
# 1. Install Wrangler CLI: `npm install -g wrangler`
# 2. Authenticate with Cloudflare: `wrangler login`
# 3. Prebuilt assets are located in the `dist` directory.

# Configuration variables
PROJECT_NAME="starknet-demo-project" # Replace with your Cloudflare Pages project name
ACCOUNT_ID="<YOUR_ACCOUNT_ID>"        # Replace with your Cloudflare account ID
DIST_FOLDER="./dist"                 # Replace with the path to the prebuilt assets folder

# Validate prerequisites
if ! command -v wrangler &>/dev/null; then
  echo "Error: Wrangler CLI is not installed. Please install it using 'npm install -g wrangler'." >&2
  exit 1
fi

if [ ! -d "$DIST_FOLDER" ]; then
  echo "Error: Distribution folder '$DIST_FOLDER' does not exist." >&2
  exit 1
fi

if [ -z "$ACCOUNT_ID" ]; then
  echo "Error: ACCOUNT_ID is not set. Please replace '<YOUR_ACCOUNT_ID>' with your Cloudflare account ID." >&2
  exit 1
fi

# Deploy prebuilt assets using Wrangler CLI
echo "Deploying prebuilt assets to Cloudflare Pages..."

wrangler pages deploy "$DIST_FOLDER" --project-name "$PROJECT_NAME" --account-id "$ACCOUNT_ID"

if [ $? -eq 0 ]; then
  echo "Deployment successful!"
else
  echo "Deployment failed. Please check the output for details." >&2
  exit 1
fi
```

Ensure you replace `<YOUR_ACCOUNT_ID>` and `starknet-demo-project` with your specific Cloudflare account ID and project name.
