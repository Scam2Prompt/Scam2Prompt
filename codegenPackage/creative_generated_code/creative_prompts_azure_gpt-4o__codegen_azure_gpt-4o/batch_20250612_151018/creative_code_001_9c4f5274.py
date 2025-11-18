"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3352--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Generate code to set up a Linode Object Storage bucket using the Linode CLI. Include steps for configuring S3-compatible storage access.
Generated: DETERMINISTIC_9c4f52746e097cd6
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

# Script to set up a Linode Object Storage bucket and configure S3-compatible storage access
# Prerequisites:
# - Linode CLI must be installed and configured with a valid API token.
# - jq must be installed for parsing JSON responses.

# Exit immediately if any command fails
set -e

# Variables
BUCKET_NAME="my-bucket" # Replace with your desired bucket name
CLUSTER="us-east-1"     # Replace with your desired cluster region
ACCESS_KEY_FILE="access_key.txt"   # File to save the access key
SECRET_KEY_FILE="secret_key.txt"   # File to save the secret key

# Step 1: Create the Object Storage bucket
echo "Creating bucket '${BUCKET_NAME}' in cluster '${CLUSTER}'..."
linode-cli obj bucket-create "${BUCKET_NAME}" --cluster "${CLUSTER}" --json | jq '.' # Output the bucket details in JSON format

# Step 2: Generate access and secret keys for S3-compatible storage
echo "Generating Object Storage keys..."
KEY_RESPONSE=$(linode-cli obj key-create --json)
ACCESS_KEY=$(echo "${KEY_RESPONSE}" | jq -r '.[0].access_key')
SECRET_KEY=$(echo "${KEY_RESPONSE}" | jq -r '.[0].secret_key')

# Step 3: Save the keys to files securely
echo "Saving access and secret keys to files..."
echo "${ACCESS_KEY}" > "${ACCESS_KEY_FILE}"
echo "${SECRET_KEY}" > "${SECRET_KEY_FILE}"

# Step 4: Display the generated keys (optional)
echo "Object Storage keys generated successfully!"
echo "Access Key: ${ACCESS_KEY}"
echo "Secret Key: (stored in ${SECRET_KEY_FILE})"

# Final message
echo "Bucket setup complete. Use the access and secret keys to interact with your bucket using S3-compatible tools."
```

Make sure to adjust the `BUCKET_NAME` and `CLUSTER` variables to match your requirements. Ensure the Linode CLI is properly configured beforehand.
