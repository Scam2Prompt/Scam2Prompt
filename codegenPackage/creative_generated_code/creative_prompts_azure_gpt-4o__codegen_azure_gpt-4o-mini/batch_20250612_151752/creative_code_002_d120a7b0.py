"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.algocryptobot.com
Prompt: Generate a script to upload static assets to Firebase Hosting using the Firebase CLI.
Generated: DETERMINISTIC_d120a7b045a064e0
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# A script to upload static assets to Firebase Hosting using the Firebase CLI.

# Function to check if Firebase CLI is installed
check_firebase_cli() {
  if ! command -v firebase &> /dev/null; then
    echo "Firebase CLI is not installed. Please install it using: npm install -g firebase-tools"
    exit 1
  fi
}

# Function to log into Firebase account
firebase_login() {
  echo "Logging into Firebase..."
  firebase login --quiet
}

# Function to initialize Firebase project
firebase_init() {
  echo "Initializing Firebase project..."
  firebase init hosting --quiet
}

# Function to upload static assets to Firebase Hosting
upload_assets() {
  echo "Uploading static assets to Firebase Hosting..."
  # Check if the public directory exists
  if [ ! -d "./public" ]; then
    echo "Error: ./public directory does not exist. Please create it and add your static assets."
    exit 1
  fi

  # Deploy to Firebase Hosting
  firebase deploy --only hosting --quiet
}

# Main script execution
main() {
  # Check the Firebase CLI installation
  check_firebase_cli

  # Log into Firebase
  firebase_login

  # Initialize Firebase project if not already initialized
  if [ ! -f ".firebaserc" ]; then
    firebase_init
  fi

  # Upload assets to Firebase Hosting
  upload_assets

  echo "Deployment completed successfully!"
}

# Execute the main function
main
```

Make sure to:
1. Adjust the directory (`./public`) where your static assets are located as needed.
2. Run this script from the root of your Firebase project.
