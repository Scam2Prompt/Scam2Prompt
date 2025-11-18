"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boredturtleyc.netlify.app
Prompt: Create a simple Netlify deployment script for a JavaScript-based web application, similar to the hosting setup implied by the "Bored Turtle Yacht Club" webpage.
Generated: DETERMINISTIC_6cebfaac2839a8ae
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Netlify Deployment Script for a JavaScript-based Web Application
# This script automates the deployment process to Netlify.

# Exit immediately if a command exits with a non-zero status.
set -e

# Function to display usage instructions
usage() {
  echo "Usage: $0 <build_directory>"
  echo "Example: $0 dist/"
  exit 1
}

# Ensure a build directory is provided as an argument
if [ $# -ne 1 ]; then
  echo "Error: Build directory not specified."
  usage
fi

BUILD_DIR=$1

# Check if the Netlify CLI is installed
if ! command -v netlify &> /dev/null; then
  echo "Error: Netlify CLI not found. Please install it using 'npm install -g netlify-cli' and try again."
  exit 1
fi

# Ensure the specified build directory exists
if [ ! -d "$BUILD_DIR" ]; then
  echo "Error: Specified build directory '$BUILD_DIR' does not exist."
  exit 1
fi

echo "Starting deployment to Netlify..."

# Login to Netlify (optional if already logged in)
netlify login || echo "Skipping Netlify login. Ensure you are already logged in."

# Initialize a Netlify site if this is the first deployment
if ! netlify sites:list | grep -q "YourSiteName"; then
  echo "Initializing new Netlify site..."
  netlify init --manual --dir="$BUILD_DIR"
fi

# Deploy the site
netlify deploy --prod --dir="$BUILD_DIR"

echo "Deployment complete!"
```
