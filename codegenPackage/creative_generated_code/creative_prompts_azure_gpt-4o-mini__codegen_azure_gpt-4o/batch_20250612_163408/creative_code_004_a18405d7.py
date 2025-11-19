"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2794--docusaurus-2.netlify.app
Prompt: How do I set up localization in Docusaurus to translate documentation into multiple languages using Crowdin?
Generated: DETERMINISTIC_a18405d7fd8be12b
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// siteConfig.js
// Docusaurus configuration file for enabling localization with Crowdin

module.exports = {
  i18n: {
    // Define the default language
    defaultLocale: 'en',
    // List all supported locales
    locales: ['en', 'fr', 'es', 'de'], // Add all desired languages here
    localeConfigs: {
      en: {
        label: 'English', // Display name for the language
      },
      fr: {
        label: 'Français', // Display name for the language
      },
      es: {
        label: 'Español', // Display name for the language
      },
      de: {
        label: 'Deutsch', // Display name for the language
      },
    },
  },
};

// Crowdin sync script: scripts/crowdinSync.js
// Script for syncing translations between Crowdin and Docusaurus
const { execSync } = require('child_process');
const path = require('path');

try {
  // Path to the Crowdin CLI configuration file
  const crowdinConfigPath = path.resolve(__dirname, '../crowdin.yml');

  // Sync translations from Crowdin to the local project
  console.log('Syncing translations from Crowdin...');
  execSync(`crowdin download -c ${crowdinConfigPath}`, { stdio: 'inherit' });

  console.log('Translations synced successfully!');
} catch (error) {
  console.error('Failed to sync translations from Crowdin:', error.message);
  process.exit(1); // Exit with an error code
}
```

```yaml
# crowdin.yml
# Crowdin configuration file

project_id: your_project_id_here
api_token: your_crowdin_api_token_here

files:
  # Map source files to target files for translation
  - source: /i18n/en/**/*.json
    translation: /i18n/%locale%/**/%file_name%
    languages_mapping:
      fr: fr
      es: es
      de: de
```

```bash
# Install Crowdin CLI if not already installed
npm install -g @crowdin/cli

# Run Crowdin sync script
node scripts/crowdinSync.js
```

```bash
# Command to initialize Crowdin CLI (run once)
crowdin init --api-token your_crowdin_api_token_here --project-id your_project_id_here
```

```json
// Example translation file: i18n/fr/docusaurus-theme-common/footer.json
{
  "footer": {
    "copyright": "Copyright © 2023 Votre Organisation. Tous droits réservés."
  }
}
```

```json
// Example translation file: i18n/es/docusaurus-theme-common/footer.json
{
  "footer": {
    "copyright": "Copyright © 2023 Su Organización. Todos los derechos reservados."
  }
}
```
