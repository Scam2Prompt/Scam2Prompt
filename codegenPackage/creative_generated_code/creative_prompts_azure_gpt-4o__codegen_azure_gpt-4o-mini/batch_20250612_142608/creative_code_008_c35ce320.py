"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.gitbook.io
Prompt: Write code to automate the deployment of a GitBook documentation site using the Polymarket starter template's publishing tools.
Generated: DETERMINISTIC_c35ce320b5dd7ecb
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to automate the deployment of a GitBook documentation site using the Polymarket starter template's publishing tools

set -e  # Exit immediately if a command exits with a non-zero status

# Function to display usage information
usage() {
  echo "Usage: $0 [options]"
  echo "Options:"
  echo "  -h, --help       Show this help message and exit"
  echo "  -b, --build      Build the GitBook documentation"
  echo "  -d, --deploy     Deploy the GitBook documentation"
  echo "  -e, --environment Set the environment (production/staging)"
  exit 1
}

# Parse command-line arguments
BUILD=false
DEPLOY=false
ENVIRONMENT="production"

while [[ "$#" -gt 0 ]]; do
  case "$1" in
    -h|--help) usage ;;
    -b|--build) BUILD=true ;;
    -d|--deploy) DEPLOY=true ;;
    -e|--environment) ENVIRONMENT="$2"; shift ;;
    *) echo "Unknown option: $1"; usage ;;
  esac
  shift
done

# Check if at least one action is specified
if ! $BUILD && ! $DEPLOY; then
  echo "You must specify at least one action: --build or --deploy"
  usage
fi

# Build the GitBook documentation
if $BUILD; then
  echo "Building GitBook documentation..."
  # Check if GitBook CLI is installed
  if ! command -v gitbook &> /dev/null; then
    echo "Error: GitBook is not installed. Please install it first."
    exit 1
  fi

  # Build the documentation
  gitbook build ./docs ./_book

  if [ $? -ne 0 ]; then
    echo "Error: Failed to build the documentation."
    exit 1
  fi
  echo "Build completed successfully."
fi

# Deploy the GitBook documentation
if $DEPLOY; then
  echo "Deploying GitBook documentation to ${ENVIRONMENT} environment..."
  # Check if the deployment tool is installed
  if ! command -v gh &> /dev/null; then
    echo "Error: GitHub CLI (gh) is not installed. Please install it first."
    exit 1
  fi

  # Deploy the documentation to GitHub Pages
  gh repo set-default-branch gh-pages
  git add _book
  git commit -m "Deploy GitBook documentation"
  git push origin gh-pages

  if [ $? -ne 0 ]; then
    echo "Error: Failed to deploy the documentation."
    exit 1
  fi
  echo "Deployment completed successfully."
fi

echo "Script execution completed."
```

### Notes:
- Save this script as `deploy.sh` and make it executable with `chmod +x deploy.sh`.
- Ensure that you have GitBook and GitHub CLI installed to use this script.
- Place your GitBook source files in a `docs` directory in the same location as this script.
- This script assumes that the local repository is already set up for GitHub Pages and the `gh` CLI is configured properly.
