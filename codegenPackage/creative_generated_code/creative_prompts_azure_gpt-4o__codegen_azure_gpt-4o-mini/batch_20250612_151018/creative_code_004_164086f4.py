"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: Create a localization setup for a Docusaurus project using Crowdin to translate documentation into multiple languages.
Generated: DETERMINISTIC_164086f4c1e82052
Batch ID: 20250612_151018
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/your-github-repo/edit/main/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-domain.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-github-repo/edit/main/blog/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
# Create a new Docusaurus project (if not already created)
npx create-docusaurus@latest my-website classic
cd my-website

# Install Crowdin CLI for managing translations
npm install --save-dev @crowdin/cli
```

```yaml
# .crowdin.yaml - Configuration file for Crowdin integration

# Project settings
project_id: YOUR_CROWDIN_PROJECT_ID
api_token: YOUR_CROWDIN_API_TOKEN

# Define source files to be uploaded to Crowdin
files:
  - source: /docs/*.md
    translation: /%two_letters_code%/docs/

# Define supported languages
languages:
  - en
  - es
  - fr
  - de

# Specify the default language
default_language: en

# Define the upload and download structure
upload:
  - source: /docs/*.md
    translation: /%two_letters_code%/docs/

download:
  - source: /%two_letters_code%/docs/*.md
    translation: /docs/
```

```javascript
// docusaurus.config.js - Docusaurus configuration file

const { i18n } = require('docusaurus-plugin-i18n');

module.exports = {
  title: 'My Documentation',
  tagline: 'Documentation made easy',
  url: 'https://your-domain.com', // Your website URL
  baseUrl: '/',

  // Configure localization
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'es', 'fr', 'de'], // Add your supported languages
  },

  // Other configurations...
  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/your-github-repo/edit/main/',
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/your-github-repo/edit/main/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
  
  // Error handling for missing translations
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
};
```

```bash
# Crowdin CLI commands to manage translations

# Upload source files to Crowdin
npx crowdin upload sources

# Download translations from Crowdin
npx crowdin download
```

```bash
# Add the following scripts to your package.json for easy access

"scripts": {
  "crowdin:upload": "crowdin upload sources",
  "crowdin:download": "crowdin download"
}
```

```plaintext
# Ensure to run the following commands to upload and download translations

# Upload source files after making changes
npm run crowdin:upload

# Download translations to keep your local files updated
npm run crowdin:download
```

```plaintext
# Remember to replace YOUR_CROWDIN_PROJECT_ID and YOUR_CROWDIN_API_TOKEN 
# with actual values from your Crowdin account.
```
