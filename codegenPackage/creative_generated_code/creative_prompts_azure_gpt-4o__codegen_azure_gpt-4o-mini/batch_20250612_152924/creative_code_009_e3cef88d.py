"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maglcedan-claim.web.app
Prompt: Create a script that uses the Firebase CLI to deploy multiple sites to Firebase Hosting under the same Firebase project.
Generated: DETERMINISTIC_e3cef88d01136621
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# A script to deploy multiple sites to Firebase Hosting under the same Firebase project.

# Define an array with the names of the sites to deploy.
SITES=("site1" "site2" "site3") # Replace with your actual site names

# Check if Firebase CLI is installed
if ! command -v firebase &> /dev/null; then
    echo "Firebase CLI could not be found. Please install it first."
    exit 1
fi

# Loop through each site and deploy
for SITE in "${SITES[@]}"; do
    # Check if the site directory exists
    if [ ! -d "$SITE" ]; then
        echo "Directory $SITE does not exist. Skipping deployment for this site."
        continue
    fi
    
    # Change to the site directory
    cd "$SITE" || { echo "Failed to change directory to $SITE. Skipping."; continue; }

    # Initialize Firebase for the site if not already initialized
    if [ ! -f ".firebaserc" ]; then
        echo "Initializing Firebase for $SITE..."
        firebase init hosting --non-interactive --project <your-project-id>
    fi

    # Deploy the site
    echo "Deploying $SITE..."
    if firebase deploy --only hosting; then
        echo "$SITE deployed successfully!"
    else
        echo "Failed to deploy $SITE. Please check the logs for more details."
    fi

    # Go back to the parent directory
    cd ..

done

echo "Deployment process completed for all sites."
```

**Note:** Replace `<your-project-id>` with the actual Firebase project ID. Ensure you have the appropriate permissions and configurations set up in your Firebase project before running this script.
