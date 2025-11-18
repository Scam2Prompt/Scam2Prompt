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

# Define variables for bucket creation
BUCKET_NAME="my-object-storage-bucket"
REGION="us-east-1" # Change to your desired region
PROFILE_NAME="my-linode-profile" # Change to your Linode CLI profile name

# Function to create a Linode Object Storage bucket
create_bucket() {
    echo "Creating Object Storage bucket: $BUCKET_NAME in region: $REGION"

    # Create the bucket using Linode CLI
    linode-cli object-storage buckets-create --label "$BUCKET_NAME" --region "$REGION" --profile "$PROFILE_NAME"

    # Check if the bucket was created successfully
    if [[ $? -ne 0 ]]; then
        echo "Error: Bucket creation failed."
        exit 1
    fi

    echo "Bucket '$BUCKET_NAME' created successfully."
}

# Function to configure S3-compatible storage access
configure_s3_access() {
    echo "Configuring S3-compatible access for bucket: $BUCKET_NAME"

    # Fetch S3 access keys (assuming keys are already generated)
    ACCESS_KEY=$(linode-cli object-storage list-keys --profile "$PROFILE_NAME" | jq -r '.[0].access_key')
    SECRET_KEY=$(linode-cli object-storage list-keys --profile "$PROFILE_NAME" | jq -r '.[0].secret_key')

    if [[ -z "$ACCESS_KEY" || -z "$SECRET_KEY" ]]; then
        echo "Error: Unable to fetch access keys."
        exit 1
    fi

    echo "S3-compatible access configured with Access Key: $ACCESS_KEY"
    echo "Keep your Secret Key secure and do not share it."
}

# Main execution block
main() {
    create_bucket
    configure_s3_access
}

# Execute the main function
main
```
