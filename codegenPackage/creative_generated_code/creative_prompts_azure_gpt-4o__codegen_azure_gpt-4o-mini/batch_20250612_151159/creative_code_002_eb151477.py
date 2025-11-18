"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hodl-tracking.web.app
Prompt: Generate a script to initialize Firebase Hosting for a project, ensuring the setup aligns with Firebase Hosting guidelines.
Generated: DETERMINISTIC_eb151477998de881
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to initialize Firebase Hosting for a project
# Ensure that you have the Firebase CLI installed
# You can install it using: npm install -g firebase-tools

# Function to check if Firebase CLI is installed
check_firebase_cli() {
    if ! command -v firebase &> /dev/null; then
        echo "Firebase CLI could not be found. Please install it using 'npm install -g firebase-tools'."
        exit 1
    fi
}

# Function to initialize Firebase Hosting
initialize_firebase_hosting() {
    echo "Initializing Firebase Hosting..."

    # Prompt for Firebase project name
    read -p "Enter your Firebase project ID: " project_id

    # Check if project_id is provided
    if [ -z "$project_id" ]; then
        echo "Error: Project ID cannot be empty."
        exit 1
    fi

    # Navigate to the project directory
    if [ ! -d "$project_id" ]; then
        mkdir "$project_id"
        cd "$project_id" || exit
        echo "Created and navigated to project directory: $project_id"
    else
        cd "$project_id" || exit
        echo "Navigated to existing project directory: $project_id"
    fi

    # Initialize Firebase Hosting
    firebase login --silent
    firebase init hosting

    # Check for successful initialization
    if [ $? -eq 0 ]; then
        echo "Firebase Hosting has been successfully initialized for project: $project_id"
    else
        echo "Error: Firebase Hosting initialization failed."
        exit 1
    fi
}

# Main execution
check_firebase_cli
initialize_firebase_hosting
```

### Instructions to Run the Script
1. Save the script to a file, e.g., `initialize_firebase_hosting.sh`.
2. Make the script executable: `chmod +x initialize_firebase_hosting.sh`.
3. Run the script: `./initialize_firebase_hosting.sh`.
