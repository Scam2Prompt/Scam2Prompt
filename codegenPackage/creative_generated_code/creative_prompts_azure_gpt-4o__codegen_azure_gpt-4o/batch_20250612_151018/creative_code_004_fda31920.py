"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2794--docusaurus-2.netlify.app
Prompt: Provide code to set up localization in Docusaurus using Crowdin for translating documentation into multiple languages.
Generated: DETERMINISTIC_fda319204b80285a
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// docusaurus.config.js

// Docusaurus configuration file
module.exports = {
  i18n: {
    // Default locale for the documentation
    defaultLocale: 'en',
    // Supported locales for localization
    locales: ['en', 'es', 'fr', 'de'], // Add more languages as needed
    // Locale detection via subpaths or domain
    localeConfigs: {
      en: {
        label: 'English', // Label displayed in the language dropdown
      },
      es: {
        label: 'Español',
      },
      fr: {
        label: 'Français',
      },
      de: {
        label: 'Deutsch',
      },
    },
  },
};

// crowdin-config.yml

# Crowdin configuration file for integration with Docusaurus

project_id: your_project_id_here # Replace with your Crowdin project ID
api_token: your_api_token_here # Replace with your Crowdin API token

files:
  - source: /i18n/en/**/*.json
    translation: /i18n/%locale%/%original_path% # Structure to store translations
    languages_mapping:
      locale: # Mapping Crowdin languages to Docusaurus locales
        es-ES: es
        fr-FR: fr
        de-DE: de # Add more mappings as needed

# Installation Script

// install-crowdin.js
// Script to install and configure Crowdin CLI for localization
const { exec } = require('child_process');

const installCrowdinCLI = () => {
  console.log('Starting Crowdin CLI installation...');
  exec('npm install -g @crowdin/cli', (error, stdout, stderr) => {
    if (error) {
      console.error('Error installing Crowdin CLI:', error.message);
      return;
    }
    if (stderr) {
      console.error('Installation warnings:', stderr);
    }
    console.log(stdout);
    console.log('Crowdin CLI installed successfully.');
  });
};

installCrowdinCLI();

// Usage Instructions in README.md
// Add the following to your project's README.md
/*
Localization Using Crowdin
==========================

1. Install Crowdin CLI:
   ```
   npm install -g @crowdin/cli
   ```

2. Configure Crowdin:
   - Add your `crowdin-config.yml` file with the appropriate project ID and API token.

3. Sync source files with Crowdin:
   ```
   crowdin upload sources
   ```

4. Download translations:
   ```
   crowdin download
   ```

5. Test translations locally by running your Docusaurus instance:
   ```
   npm start
   ```
*/
```
