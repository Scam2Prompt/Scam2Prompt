"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2803--docusaurus-2.netlify.app
Prompt: What is the process for translating Docusaurus documentation into multiple languages using Crowdin?
Generated: DETERMINISTIC_9e1eb93386b7bccd
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# This script automates the process of translating Docusaurus documentation into multiple languages using Crowdin.

# Set the necessary environment variables
export CROWDIN_API_TOKEN="your_crowdin_api_token"
export CROWDIN_PROJECT_ID="your_crowdin_project_id"
export DOCS_DIR="path/to/your/docusaurus/docs"
export OUTPUT_DIR="path/to/output/directory"

# Function to check if a command was successful
check_command() {
    if [ $? -ne 0 ]; then
        echo "Error: $1 failed."
        exit 1
    fi
}

# Step 1: Install Crowdin CLI if not already installed
if ! command -v crowdin &> /dev/null; then
    echo "Crowdin CLI not found. Installing..."
    npm install -g crowdin-cli
    check_command "Crowdin CLI installation"
fi

# Step 2: Initialize Crowdin project
echo "Initializing Crowdin project..."
crowdin init --token $CROWDIN_API_TOKEN --project-id $CROWDIN_PROJECT_ID
check_command "Crowdin project initialization"

# Step 3: Upload Docusaurus documentation to Crowdin
echo "Uploading Docusaurus documentation to Crowdin..."
crowdin upload sources --files "$DOCS_DIR/**/*" --token $CROWDIN_API_TOKEN
check_command "Uploading documentation to Crowdin"

# Step 4: Start the translation process
echo "Starting translation process..."
crowdin translate --token $CROWDIN_API_TOKEN
check_command "Starting translation"

# Step 5: Download translated files
echo "Downloading translated files..."
crowdin download --token $CROWDIN_API_TOKEN --output-dir $OUTPUT_DIR
check_command "Downloading translated files"

# Step 6: Build Docusaurus with translated content
echo "Building Docusaurus with translated content..."
cd $OUTPUT_DIR
npm run build
check_command "Building Docusaurus"

echo "Translation process completed successfully!"
```

### Notes:
- Replace `your_crowdin_api_token`, `your_crowdin_project_id`, `path/to/your/docusaurus/docs`, and `path/to/output/directory` with actual values.
- Ensure that the Crowdin CLI is compatible with your system and that Node.js is installed for the npm commands to work.
