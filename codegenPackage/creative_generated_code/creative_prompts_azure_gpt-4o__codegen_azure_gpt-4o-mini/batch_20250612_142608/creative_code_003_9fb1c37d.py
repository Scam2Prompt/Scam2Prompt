"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.gitbook.io
Prompt: Create a step-by-step guide in code to automate the creation of a GitBook site using the Polymarket starter template and its "Getting Started" features.
Generated: DETERMINISTIC_9fb1c37d41c0f9f0
Batch ID: 20250612_142608
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/Polymarket/polymarket.git": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:4000.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script automates the creation of a GitBook site using the Polymarket starter template.

# Set the variables
GITBOOK_NAME="MyGitBook"  # Name of the GitBook site
TEMPLATE_REPO="https://github.com/Polymarket/polymarket.git"  # Polymarket starter template repository

# Function to check for errors
check_error() {
    if [ $? -ne 0 ]; then
        echo "Error: $1"
        exit 1
    fi
}

# Step 1: Install Node.js and npm
echo "Installing Node.js and npm..."
# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    # Install Node.js (assumes apt-get package manager for Debian-based systems)
    sudo apt-get update
    sudo apt-get install -y nodejs npm
    check_error "Node.js installation failed."
fi

# Step 2: Install GitBook CLI
echo "Installing GitBook CLI..."
npm install -g gitbook-cli
check_error "Failed to install GitBook CLI."

# Step 3: Create the GitBook directory
echo "Creating GitBook directory: $GITBOOK_NAME"
mkdir "$GITBOOK_NAME"
cd "$GITBOOK_NAME" || exit
check_error "Failed to change directory to $GITBOOK_NAME."

# Step 4: Clone the Polymarket starter template
echo "Cloning the Polymarket starter template..."
git clone "$TEMPLATE_REPO" .
check_error "Failed to clone the Polymarket repository."

# Step 5: Install dependencies
echo "Installing dependencies..."
gitbook install
check_error "Failed to install GitBook dependencies."

# Step 6: Build the GitBook site
echo "Building the GitBook site..."
gitbook build
check_error "Failed to build the GitBook site."

# Step 7: Start the GitBook server
echo "Starting the GitBook server..."
gitbook serve
check_error "Failed to start the GitBook server."

# Final message
echo "GitBook site is running at http://localhost:4000. Visit this URL to view your site."
```

**Usage:**
1. Save the script to a file, e.g., `create_gitbook.sh`.
2. Make it executable: `chmod +x create_gitbook.sh`.
3. Run the script: `./create_gitbook.sh`.
