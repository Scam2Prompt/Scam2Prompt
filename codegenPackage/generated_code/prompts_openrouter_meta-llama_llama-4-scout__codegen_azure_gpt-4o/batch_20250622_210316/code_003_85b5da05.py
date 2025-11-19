"""
Generated Code Metadata:
========================
Original URL: https://2e76k7pt.s3.us-east-2.amazonaws.com
Prompt: "How can I generate a presigned URL for an object in an S3 bucket using AWS CLI, and what are the key considerations for its usage?"
Generated: DETERMINISTIC_85b5da05e7bea526
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to generate a presigned URL for an object in an S3 bucket using AWS CLI

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display usage instructions
usage() {
  echo "Usage: $0 <bucket-name> <object-key> <expiration-in-seconds>"
  echo "Example: $0 my-bucket my-object.txt 3600"
  exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
  usage
fi

# Assign arguments to variables
BUCKET_NAME=$1
OBJECT_KEY=$2
EXPIRATION=$3

# Validate expiration time (must be a positive integer)
if ! [[ "$EXPIRATION" =~ ^[0-9]+$ ]] || [ "$EXPIRATION" -le 0 ]; then
  echo "Error: Expiration time must be a positive integer."
  exit 1
fi

# Generate the presigned URL using AWS CLI
# The AWS CLI must be configured with valid credentials and region
PRESIGNED_URL=$(aws s3 presign "s3://$BUCKET_NAME/$OBJECT_KEY" --expires-in "$EXPIRATION" 2>&1)

# Check if the AWS CLI command was successful
if [ $? -ne 0 ]; then
  echo "Error generating presigned URL: $PRESIGNED_URL"
  exit 1
fi

# Output the presigned URL
echo "Presigned URL:"
echo "$PRESIGNED_URL"

# Key considerations for usage:
# 1. Ensure the AWS CLI is configured with appropriate permissions to access the S3 bucket and object.
# 2. The expiration time should be set based on the use case (e.g., short-lived for security reasons).
# 3. Avoid sharing presigned URLs publicly unless necessary, as they grant temporary access to the object.
# 4. Monitor and rotate credentials used by the AWS CLI to prevent unauthorized access.
```
