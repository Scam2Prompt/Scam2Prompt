"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: Provide a guide on setting up localization in Docusaurus using Crowdin for a multi-language documentation site.
Generated: DETERMINISTIC_d19da8999177ef48
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# Step 1: Install Docusaurus
npx create-docusaurus@latest my-website classic
cd my-website

# Step 2: Install Crowdin CLI
npm install --save-dev @crowdin/cli

# Step 3: Initialize Crowdin
npx crowdin init

# Step 4: Configure Crowdin
# Create a `crowdin.yml` file in the root of your project with the following content:

cat <<EOL > crowdin.yml
# Crowdin configuration file for Docusaurus localization

# Project settings
project_id: YOUR_CROWDIN_PROJECT_ID
api_token: YOUR_CROWDIN_API_TOKEN

# Source files
files:
  - source: /docs/*.md
    translation: /locales/{LANGUAGE}/{FILENAME}

# Languages
languages:
  - en
  - es
  - fr
  - de
EOL

# Step 5: Add localization support in Docusaurus
# Update `docusaurus.config.js` to include localization settings

cat <<EOL >> docusaurus.config.js
module.exports = {
  // Other configurations...
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'es', 'fr', 'de'],
  },
};
EOL

# Step 6: Create locale directories
mkdir -p locales/en locales/es locales/fr locales/de

# Step 7: Add Crowdin commands to package.json
# Update your package.json scripts section

npm set-script crowdin:upload "crowdin upload"
npm set-script crowdin:download "crowdin download"

# Step 8: Upload source files to Crowdin
npm run crowdin:upload

# Step 9: Download translations from Crowdin
npm run crowdin:download

# Step 10: Build and serve your Docusaurus site
npm run build
npm run serve
```

```javascript
// docusaurus.config.js
module.exports = {
  // Other configurations...
  i18n: {
    defaultLocale: 'en', // Default language
    locales: ['en', 'es', 'fr', 'de'], // Supported languages
  },
  // Additional configurations...
};
```

```yaml
# crowdin.yml
# Crowdin configuration file for Docusaurus localization

project_id: YOUR_CROWDIN_PROJECT_ID # Replace with your Crowdin project ID
api_token: YOUR_CROWDIN_API_TOKEN # Replace with your Crowdin API token

files:
  - source: /docs/*.md # Source files to be translated
    translation: /locales/{LANGUAGE}/{FILENAME} # Translation output path

languages:
  - en # English
  - es # Spanish
  - fr # French
  - de # German
```
