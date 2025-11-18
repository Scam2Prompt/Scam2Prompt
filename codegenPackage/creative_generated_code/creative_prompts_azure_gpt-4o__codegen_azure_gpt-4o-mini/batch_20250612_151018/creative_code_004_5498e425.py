"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2735--docusaurus-2.netlify.app
Prompt: Demonstrate how to use Crowdin with Docusaurus to localize documentation into multiple languages.
Generated: DETERMINISTIC_5498e425ae84834a
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Install Crowdin CLI
# Ensure you have Node.js installed before running this command
npm install -g crowdin-cli

# Step 2: Initialize your Docusaurus project (if not already created)
npx create-docusaurus@latest my-website classic
cd my-website

# Step 3: Install necessary dependencies for localization
# Install the Crowdin integration for Docusaurus
npm install @docusaurus/plugin-content-docs @docusaurus/plugin-content-blog

# Step 4: Set up Crowdin configuration
# Create a .crowdin.yaml file in the root of your Docusaurus project

cat <<EOL > .crowdin.yaml
# Crowdin configuration for Docusaurus localization
files:
  - source: /docs/**/*
    destination: /%locale%/docs/
  - source: /blog/**/* 
    destination: /%locale%/blog/
EOL

# Step 5: Create a Crowdin project
# Run the command to create your project on Crowdin
crowdin init

# Step 6: Push your source files to Crowdin
# This command will upload the files defined in .crowdin.yaml to Crowdin
crowdin upload

# Step 7: Pull translations from Crowdin
# This command will download the translated files back to your project
crowdin download

# Step 8: Update your Docusaurus config for localization
# In docusaurus.config.js, configure the i18n settings

cat <<EOL >> docusaurus.config.js
module.exports = {
  // ... other configurations
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'es', 'fr', 'de'], // Add the languages you are localizing to
  },
};
EOL

# Step 9: Build your Docusaurus site
npm run build

# Step 10: Serve your localized documentation
npm run serve
```

This script outlines the necessary steps to set up Crowdin with Docusaurus for localization into multiple languages, ensuring that the documentation is correctly configured for internationalization.
