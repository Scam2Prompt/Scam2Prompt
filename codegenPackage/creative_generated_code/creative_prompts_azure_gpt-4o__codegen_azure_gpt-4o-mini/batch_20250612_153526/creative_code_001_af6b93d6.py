"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stonegarden.dev
Prompt: Generate code that integrates Stonegarden.dev tools with GitHub Actions for CI/CD workflows.
Generated: DETERMINISTIC_af6b93d684741545
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      # Step 1: Checkout the code from the repository
      - name: Checkout Code
        uses: actions/checkout@v2

      # Step 2: Set up Node.js environment for the build
      - name: Setup Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14'  # Specify the Node.js version to use

      # Step 3: Install dependencies
      - name: Install Dependencies
        run: npm install

      # Step 4: Run tests
      - name: Run Tests
        run: npm test
        continue-on-error: false # Fail the workflow if tests fail

      # Step 5: Build the application
      - name: Build Application
        run: npm run build

      # Step 6: Deploy using Stonegarden.dev tools
      - name: Deploy to Stonegarden
        env:
          STONEGARDEN_API_TOKEN: ${{ secrets.STONEGARDEN_API_TOKEN }}
        run: |
          # Check if the required environment variable is set
          if [ -z "$STONEGARDEN_API_TOKEN" ]; then
            echo "Error: STONEGARDEN_API_TOKEN is not set."
            exit 1
          fi

          # Deploy the application using Stonegarden.dev CLI
          stonegarden deploy --token $STONEGARDEN_API_TOKEN --project MY_PROJECT_NAME --env production

      # Step 7: Notify on success
      - name: Notify Success
        if: success()
        run: echo "Deployment to Stonegarden was successful!"

      # Step 8: Notify on failure
      - name: Notify Failure
        if: failure()
        run: echo "Deployment to Stonegarden failed."
```

```bash
# Example script for Stonegarden CLI commands (stonegarden.sh)
#!/bin/bash

# Stonegarden deployment script
# Usage: ./stonegarden.sh deploy --token <API_TOKEN> --project <PROJECT_NAME> --env <ENVIRONMENT>

# Function to show help
show_help() {
  echo "Usage: $0 deploy --token <API_TOKEN> --project <PROJECT_NAME> --env <ENVIRONMENT>"
  exit 1
}

# Parse command-line arguments
if [[ $# -lt 6 ]]; then
  show_help
fi

# Get arguments
while [[ "$1" != "" ]]; do
  case $1 in
    --token )         shift
                      TOKEN=$1
                      ;;
    --project )       shift
                      PROJECT_NAME=$1
                      ;;
    --env )           shift
                      ENVIRONMENT=$1
                      ;;
    * )               show_help
                      ;;
  esac
  shift
done

# Error handling for missing variables
if [[ -z "$TOKEN" || -z "$PROJECT_NAME" || -z "$ENVIRONMENT" ]]; then
  echo "Error: Missing required arguments."
  show_help
fi

# Deploy command (mocked for illustration)
echo "Deploying project '$PROJECT_NAME' to environment '$ENVIRONMENT' with token '$TOKEN'..."
# Add actual deployment logic here
```
