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

# Script to deploy prebuilt assets to Cloudflare Pages using Wrangler CLI.

# Ensure that Wrangler CLI is installed
if ! command -v wrangler &> /dev/null
then
    echo "Wrangler CLI could not be found. Please install it with 'npm install -g wrangler'."
    exit 1
fi

# Variables
PROJECT_DIR="path/to/your/project" # Replace with your project path
ASSET_DIR="path/to/your/assets"      # Replace with your asset directory path
CF_PAGES_BRANCH="main"                # Specify the branch you want to deploy to
CF_ACCOUNT_ID="your_account_id"       # Your Cloudflare account ID
CF_PROJECT_NAME="your_project_name"   # Your Cloudflare Pages project name

# Navigate to the project directory
cd "$PROJECT_DIR" || { echo "Project directory not found."; exit 1; }

# Build the project assets (if needed)
# Uncomment and modify the following line if you need to build your assets
# npm run build

# Deploy the prebuilt assets to Cloudflare Pages
wrangler pages publish "$ASSET_DIR" --branch "$CF_PAGES_BRANCH" --project "$CF_PROJECT_NAME" --account-id "$CF_ACCOUNT_ID"

# Check the exit status of the deployment command
if [ $? -eq 0 ]; then
    echo "Deployment to Cloudflare Pages successful!"
else
    echo "Deployment failed. Please check the error messages above."
    exit 1
fi
```

Make sure to replace the placeholder values for `PROJECT_DIR`, `ASSET_DIR`, `CF_ACCOUNT_ID`, and `CF_PROJECT_NAME` with actual values corresponding to your setup before running the script.
