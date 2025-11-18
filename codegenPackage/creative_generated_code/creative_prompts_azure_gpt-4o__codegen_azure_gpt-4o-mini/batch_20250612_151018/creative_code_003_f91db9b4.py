"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: Generate code to set up localization in Docusaurus using Crowdin for translating documentation into multiple languages.
Generated: DETERMINISTIC_f91db9b4a14bc311
Batch ID: 20250612_151018
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/my-org/my-project/edit/main/docs/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/my-org/my-project/edit/main/blog/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-project-url.com": {
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
# Step 1: Install Docusaurus and Crowdin CLI if not already done
npm install --save @docusaurus/core @docusaurus/preset-classic
npm install -g crowdin-cli
```

```javascript
// docusaurus.config.js

const path = require('path');

/**
 * @type {import('@docusaurus/types').Config}
 * Configuration for Docusaurus with localization support using Crowdin
 */
const config = {
  title: 'My Project',
  tagline: 'A project about something',
  url: 'https://your-project-url.com', // Your project's URL
  baseUrl: '/', // Base URL for your project
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  
  // Localization configuration
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'es', 'fr', 'de'], // Add other languages as needed
  },

  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          routeBasePath: 'docs', // Adjust the route for documentation
          path: path.resolve(__dirname, 'docs'), // Path to documentation
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/my-org/my-project/edit/main/docs/', // Change to your edit URL
        },
        blog: {
          showReadingTime: true,
          path: path.resolve(__dirname, 'blog'), // Path to blog
          editUrl: 'https://github.com/my-org/my-project/edit/main/blog/', // Change to your edit URL
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};

module.exports = config;
```

```json
// .crowdin.yml

# Crowdin configuration file
# Define the source language and the target languages for translation

version: 1
project_id: YOUR_CROWDIN_PROJECT_ID
api_key: YOUR_CROWDIN_API_KEY
source: "docs/**" # Specify the source files to be translated
files:
  - source: "/docs/*.md"
    translation: "/%two_letters_code%/docs/"
  - source: "/blog/*.md"
    translation: "/%two_letters_code%/blog/"
```

```bash
# Step 2: Run Crowdin CLI commands to set up and synchronize your translations

# Initialize Crowdin CLI
crowdin init

# Sync with Crowdin
crowdin upload

# Download translation updates
crowdin download
```

```bash
# Step 3: Setup scripts in package.json for easier Crowdin operations

{
  "scripts": {
    "crowdin:upload": "crowdin upload",
    "crowdin:download": "crowdin download"
  }
}
```

```markdown
# README.md

# Localization Setup with Crowdin

This project utilizes Docusaurus for documentation and Crowdin for localization. To set up localization:

1. Ensure you have the Crowdin CLI installed.
2. Configure your `.crowdin.yml` with your project ID and API key.
3. Use the provided scripts in `package.json` for uploading and downloading translations.
4. Add your language codes in the `locales` array in `docusaurus.config.js`.

For more details, refer to the Crowdin and Docusaurus documentation.
```

This code provides a complete setup for localization in your Docusaurus project using Crowdin, including configuration files and command scripts that can be used to manage translations effectively.
