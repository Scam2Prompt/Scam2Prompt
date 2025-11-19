"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2758--docusaurus-2.netlify.app
Prompt: Write a script to migrate a Docusaurus v1 project to v2, including steps for setting up localization with Crowdin.
Generated: DETERMINISTIC_66752ddd063f69a1
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Docusaurus v1 to v2 Migration Script with Crowdin Localization Setup

# Check if Docusaurus v1 project directory is provided
if [ $# -eq 0 ]; then
  echo "Please provide the path to your Docusaurus v1 project directory."
  exit 1
fi

PROJECT_DIR=$1

# Check if project directory exists
if [ ! -d "$PROJECT_DIR" ]; then
  echo "Project directory does not exist."
  exit 1
fi

# Step 1: Update Docusaurus version
echo "Updating Docusaurus version to v2..."
cd "$PROJECT_DIR"
npm uninstall docusaurus
npm install @docusaurus/core @docusaurus/preset-classic

# Step 2: Migrate configuration files
echo "Migrating configuration files..."
mv docusaurus.config.js docusaurus.config.js.v1
cp node_modules/@docusaurus/core/docusaurus.config.js .

# Step 3: Update sidebars and docs
echo "Updating sidebars and docs..."
find docs -name "*.md" -exec sed -i 's/^## /### /g' {} \;
find sidebars.json -type f -exec cp /dev/null {} \;

# Step 4: Set up Crowdin localization
echo "Setting up Crowdin localization..."
CROWDIN_API_TOKEN=$2
CROWDIN_PROJECT_ID=$3

if [ -z "$CROWDIN_API_TOKEN" ] || [ -z "$CROWDIN_PROJECT_ID" ]; then
  echo "Please provide Crowdin API token and project ID."
  exit 1
fi

crowdin-cli --token $CROWDIN_API_TOKEN --project-id $CROWDIN_PROJECT_ID init

# Step 5: Configure Crowdin for Docusaurus v2
echo "Configuring Crowdin for Docusaurus v2..."
cat <<EOF > crowdin.yml
file: $PROJECT_DIR/docs/\*.md
  translation: $PROJECT_DIR/i18n/\{locale\}/docs/\*.md
  type: markdown
EOF

crowdin-cli --token $CROWDIN_API_TOKEN --project-id $CROWDIN_PROJECT_ID upload

# Step 6: Integrate Crowdin with Docusaurus v2
echo "Integrating Crowdin with Docusaurus v2..."
cat <<EOF >> docusaurus.config.js
module.exports = {
  //...
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'fr'],
  },
  //...
};
EOF

# Step 7: Add i18n support to Docusaurus v2
echo "Adding i18n support to Docusaurus v2..."
npm install @docusaurus/translation

# Final step: Start Docusaurus v2 development server
echo "Starting Docusaurus v2 development server..."
npm run start
```
