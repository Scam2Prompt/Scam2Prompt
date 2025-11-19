"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-website-1ra.pages.dev
Prompt: How can I use the Wrangler CLI to deploy prebuilt assets to Cloudflare Pages?
Generated: DETERMINISTIC_dcfa69342c06b29a
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Cloudflare Pages deployment script using the Wrangler CLI.
# Ensure Wrangler CLI is installed and authenticated with your Cloudflare account.

#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Constants
CLOUDFLARE_ACCOUNT_ID="your_cloudflare_account_id" # Replace with your Cloudflare account ID
PROJECT_NAME="your_project_name"                  # Replace with your Cloudflare Pages project name
ASSET_DIR="./dist"                                # Directory containing prebuilt assets
BRANCH="main"                                     # Branch to deploy (default is 'main')
DEPLOY_ENVIRONMENT="production"                   # Environment to deploy to ('production' or 'preview')

# Error handling for missing variables
if [[ -z "$CLOUDFLARE_ACCOUNT_ID" ]]; then
  echo "Error: CLOUDFLARE_ACCOUNT_ID is not set."
  exit 1
fi

if [[ -z "$PROJECT_NAME" ]]; then
  echo "Error: PROJECT_NAME is not set."
  exit 1
fi

if [[ ! -d "$ASSET_DIR" ]]; then
  echo "Error: Asset directory $ASSET_DIR does not exist."
  exit 1
fi

# Display deployment information
echo "Starting deployment with Wrangler CLI..."
echo "Account ID: $CLOUDFLARE_ACCOUNT_ID"
echo "Project Name: $PROJECT_NAME"
echo "Deploying assets from: $ASSET_DIR"
echo "Branch: $BRANCH"
echo "Environment: $DEPLOY_ENVIRONMENT"

# Authenticate Wrangler (requires Wrangler CLI installed)
wrangler login

# Deploy prebuilt assets to Cloudflare Pages
wrangler pages deploy \
  $ASSET_DIR \
  --project-name $PROJECT_NAME \
  --branch $BRANCH \
  --environment $DEPLOY_ENVIRONMENT

# Successful deployment message
echo "Deployment successful! Your assets have been published to Cloudflare Pages."
```
