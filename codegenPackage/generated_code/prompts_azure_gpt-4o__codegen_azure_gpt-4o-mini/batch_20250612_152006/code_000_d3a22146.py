"""
Generated Code Metadata:
========================
Original URL: https://starknet-website-1ra.pages.dev
Prompt: Write code using the Wrangler CLI to deploy prebuilt assets directly to Cloudflare Pages, as described in the "Direct Upload Demo" on the Starknet Cloudflare Pages example project.
Generated: DETERMINISTIC_d3a221462445601f
Batch ID: 20250612_152006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# This script deploys prebuilt assets to Cloudflare Pages using the Wrangler CLI.
# Ensure you have Wrangler installed and configured with your Cloudflare account.

# Set the necessary environment variables
export CLOUDFLARE_ACCOUNT_ID="your_account_id"  # Replace with your Cloudflare account ID
export CLOUDFLARE_PROJECT_NAME="your_project_name"  # Replace with your Cloudflare Pages project name
export CLOUDFLARE_API_TOKEN="your_api_token"  # Replace with your Cloudflare API token

# Function to check if Wrangler is installed
check_wrangler_installed() {
    if ! command -v wrangler &> /dev/null; then
        echo "Wrangler CLI is not installed. Please install it first."
        exit 1
    fi
}

# Function to deploy assets
deploy_assets() {
    # Navigate to the directory containing the prebuilt assets
    cd /path/to/your/prebuilt/assets || { echo "Directory not found"; exit 1; }

    # Deploy the assets using Wrangler
    wrangler pages publish . --project-name "$CLOUDFLARE_PROJECT_NAME" --account-id "$CLOUDFLARE_ACCOUNT_ID" --api-token "$CLOUDFLARE_API_TOKEN"
    
    # Check if the deployment was successful
    if [ $? -eq 0 ]; then
        echo "Deployment to Cloudflare Pages was successful."
    else
        echo "Deployment failed. Please check the error messages above."
        exit 1
    fi
}

# Main script execution
check_wrangler_installed
deploy_assets
```

Make sure to replace the placeholder values for `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_PROJECT_NAME`, `CLOUDFLARE_API_TOKEN`, and the path to your prebuilt assets directory before running the script.
