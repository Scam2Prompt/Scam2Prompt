"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2803--docusaurus-2.netlify.app
Prompt: What is the process for translating Docusaurus documentation into multiple languages using Crowdin?
Generated: DETERMINISTIC_9e1eb93386b7bccd
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Define the directory where your Docusaurus project is located
DOCUSAURUS_DIR="path/to/your/docusaurus-project"

# Define the Crowdin project ID and API key
CROWDIN_PROJECT_ID="your_crowdin_project_id"
CROWDIN_API_KEY="your_crowdin_api_key"

# Step 1: Install Crowdin CLI if not already installed
if ! command -v crowdin &> /dev/null
then
    echo "Crowdin CLI not found. Installing..."
    npm install -g crowdin-cli
fi

# Step 2: Initialize Crowdin
# This will create a crowdin.yml file if it does not exist
crowdin init --project-id $CROWDIN_PROJECT_ID --token $CROWDIN_API_KEY

# Step 3: Configure the crowdin.yml for Docusaurus
cat <<EOL > $DOCUSAURUS_DIR/crowdin.yml
# Crowdin configuration file for Docusaurus documentation translation

# This section specifies the path to the files to be translated
files:
  - source: "$DOCUSAURUS_DIR/docs/*.md"
    translation: "translations/{lang}/docs"

# Specify the languages you want to support
languages:
  - "en"  # English
  - "es"  # Spanish
  - "fr"  # French
  - "de"  # German
EOL

# Step 4: Upload source files to Crowdin
crowdin upload sources

# Step 5: Download translations from Crowdin
crowdin download

# Step 6: Build the Docusaurus site with translations
cd $DOCUSAURUS_DIR
npm run build

# Step 7: Serve the Docusaurus site (optional)
npm run serve

# Error handling
if [ $? -ne 0 ]; then
    echo "An error occurred during the process. Please check the logs."
    exit 1
fi

echo "Translation process completed successfully."
```
nslated files from Crowdin..."
crowdin download -c "$CROWDIN_CONFIG_FILE"

if [ $? -ne 0 ]; then
  echo "Error: Failed to download translated files from Crowdin."
  exit 1
fi

echo "Translation process completed successfully!"
```
