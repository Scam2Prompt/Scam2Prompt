"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wow-art-mint.web.app
Prompt: Write a script to automate the deployment of a web app to Firebase Hosting using the Firebase CLI.
Generated: DETERMINISTIC_903020c6a481a84a
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# deploy_to_firebase.sh
# Script to automate the deployment of a web app to Firebase Hosting using the Firebase CLI.

# Exit immediately if a command exits with a non-zero status.
set -e

# Print commands and their arguments as they are executed (useful for debugging).
set -x

# Function to display usage information.
usage() {
    echo "Usage: $0 -p <project_id> -d <directory>"
    echo "  -p <project_id>   Firebase project ID"
    echo "  -d <directory>    Path to the directory containing the web app files"
    exit 1
}

# Validate input arguments.
while getopts ":p:d:" opt; do
    case $opt in
        p)
            PROJECT_ID=$OPTARG
            ;;
        d)
            DIRECTORY=$OPTARG
            ;;
        *)
            usage
            ;;
    esac
done

# Ensure both arguments are provided.
if [[ -z "$PROJECT_ID" || -z "$DIRECTORY" ]]; then
    usage
fi

# Check if Firebase CLI is installed.
if ! command -v firebase &> /dev/null; then
    echo "Error: Firebase CLI is not installed. Please install it using 'npm install -g firebase-tools'." >&2
    exit 1
fi

# Verify the web app directory exists.
if [[ ! -d "$DIRECTORY" ]]; then
    echo "Error: Directory '$DIRECTORY' does not exist." >&2
    exit 1
fi

# Navigate to the web app directory.
cd "$DIRECTORY"

# Initialize Firebase project if not already initialized.
if [[ ! -f ".firebaserc" || ! -f "firebase.json" ]]; then
    echo "Firebase project is not initialized in this directory. Initializing now..."
    firebase init hosting --project "$PROJECT_ID" --force
fi

# Deploy to Firebase Hosting.
echo "Deploying web app to Firebase Hosting..."
firebase deploy --only hosting --project "$PROJECT_ID"

echo "Deployment successful!"
```
