"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dependabot-npm-and-yarn-sola-321x.carbon-app-csq.pages.dev
Prompt: Write a script using Yarn to install dependencies required for integrating Cloudflare Access authentication into a web app.
Generated: DETERMINISTIC_b37f4a62aa9ee4ed
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script installs the necessary dependencies for integrating Cloudflare Access authentication into a web application using Yarn.

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display usage information
usage() {
    echo "Usage: $0 [project-directory]"
    exit 1
}

# Check if a project directory is provided
if [ "$#" -ne 1 ]; then
    usage
fi

# Change to the specified project directory
PROJECT_DIR="$1"
if [ ! -d "$PROJECT_DIR" ]; then
    echo "Error: Directory '$PROJECT_DIR' does not exist."
    exit 1
fi

cd "$PROJECT_DIR"

# Initialize Yarn if not already initialized
if [ ! -f "package.json" ]; then
    echo "Initializing Yarn in the project directory..."
    yarn init -y
fi

# Install Cloudflare Access dependencies
echo "Installing Cloudflare Access authentication dependencies..."

# List of dependencies to install
DEPENDENCIES=(
    "@cloudflare/access-token"    # Cloudflare Access Token management
    "@cloudflare/worker-types"     # Types for Cloudflare Workers
    "axios"                         # Promise-based HTTP client
    "dotenv"                       # Environment variable management
)

# Install dependencies using Yarn
for DEPENDENCY in "${DEPENDENCIES[@]}"; do
    echo "Installing $DEPENDENCY..."
    yarn add "$DEPENDENCY" || { echo "Failed to install $DEPENDENCY"; exit 1; }
done

echo "All dependencies installed successfully."

# Inform the user of what to do next
echo "Please configure your Cloudflare Access settings in your application."
```

Make sure to give the script executable permissions before running it:

```bash
chmod +x install-cloudflare-access.sh
``` 

Run the script by specifying your project directory:

```bash
./install-cloudflare-access.sh /path/to/your/project
```
