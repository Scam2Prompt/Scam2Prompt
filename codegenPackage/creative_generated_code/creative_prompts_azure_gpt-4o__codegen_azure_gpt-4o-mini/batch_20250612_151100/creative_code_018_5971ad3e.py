"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Provide code examples for implementing DevOps pipelines, referencing APTRON Gurgaon’s DevOps training.
Generated: DETERMINISTIC_5971ad3ef35276ac
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# Sample YAML configuration for a CI/CD pipeline using GitHub Actions
# This pipeline builds a Docker image, runs tests, and deploys to a production environment.

name: CI/CD Pipeline

on:
  push:
    branches: 
      - main  # Trigger the pipeline on pushes to the main branch

jobs:
  build:
    runs-on: ubuntu-latest  # Use the latest Ubuntu image for the build environment

    steps:
      - name: Checkout code
        uses: actions/checkout@v2  # Checkout the repository code

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1  # Set up Docker Buildx for multi-platform builds

      - name: Log in to Docker Hub
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKER_HUB_USERNAME }}  # Fetch username from secrets
          password: ${{ secrets.DOCKER_HUB_TOKEN }}  # Fetch token from secrets

      - name: Build Docker image
        run: |
          docker build -t my-app:${{ github.sha }} .  # Build the Docker image with the commit SHA as the tag
        continue-on-error: false  # Fail the pipeline if the build fails

      - name: Run tests
        run: |
          docker run --rm my-app:${{ github.sha }} pytest tests/  # Run tests in the Docker container
        continue-on-error: false  # Fail the pipeline if tests fail

  deploy:
    runs-on: ubuntu-latest  # Use the latest Ubuntu image for deployment

    needs: build  # Ensure the build job completes successfully before deploying
    steps:
      - name: Deploy to production
        run: |
          # Assume we're using a deployment script for a cloud provider
          ./deploy.sh  # Custom script to handle deployment
        env:
          PRODUCTION_SERVER: ${{ secrets.PRODUCTION_SERVER }}  # Fetch server details from secrets
          API_KEY: ${{ secrets.API_KEY }}  # Fetch API key from secrets
        continue-on-error: false  # Fail the pipeline if deployment fails
```

```bash
# Sample Bash script for deployment (deploy.sh)
#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

# Function to handle errors
error_exit() {
    echo "Error: $1"
    exit 1
}

# Check if production server is set
if [ -z "$PRODUCTION_SERVER" ]; then
    error_exit "PRODUCTION_SERVER is not set."
fi

# Deploy the application
echo "Deploying to $PRODUCTION_SERVER..."
# (Add commands to deploy your application here, e.g., using SSH or an API call)

echo "Deployment successful!"
```

```yaml
# Sample Terraform configuration for creating a simple AWS infrastructure
# Ensure AWS CLI is configured properly with access keys and region

provider "aws" {
  region = "us-east-1"  # Specify the AWS region
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"  # AMI ID for the instance
  instance_type = "t2.micro"  # Instance type

  tags = {
    Name = "MyWebServer"  # Tag for the instance
  }
}

output "instance_ip" {
  value = aws_instance.web.public_ip  # Output the public IP of the instance
}
```
