"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: Create a localization setup for a Docusaurus project using Crowdin to translate documentation into multiple languages.
Generated: DETERMINISTIC_164086f4c1e82052
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// localization-setup.js
// This script sets up localization for a Docusaurus project using Crowdin.
// Ensure prerequisites such as the Crowdin CLI are installed and the project is initialized in Crowdin.

// Import required modules
const fs = require('fs');
const path = require('path');

// Configuration constants
const DOCUSAURUS_CONFIG_PATH = './docusaurus.config.js'; // Path to the Docusaurus configuration file
const CROWDIN_CLI_CONFIG_PATH = './crowdin.yml'; // Path to the Crowdin CLI configuration file
const SUPPORTED_LANGUAGES = ['en', 'es', 'fr', 'de']; // List of supported languages

/**
 * Adds supported languages to Docusaurus config file.
 */
function updateDocusaurusConfig() {
  try {
    const config = require(DOCUSAURUS_CONFIG_PATH);

    if (!config.i18n) {
      config.i18n = {};
    }

    config.i18n.defaultLocale = 'en'; // Default language
    config.i18n.locales = SUPPORTED_LANGUAGES; // Add supported languages
    config.i18n.localeConfigs = {
      en: {
        label: 'English',
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
    };

    // Write updated configuration back to file
    const updatedConfig = `module.exports = ${JSON.stringify(config, null, 2)};`;
    fs.writeFileSync(DOCUSAURUS_CONFIG_PATH, updatedConfig);
    console.log('Docusaurus configuration updated successfully.');
  } catch (error) {
    console.error(`Failed to update Docusaurus configuration: ${error.message}`);
  }
}

/**
 * Generates a Crowdin CLI configuration file.
 */
function generateCrowdinConfig() {
  const crowdinConfig = `
project_id: your_project_id  # Replace with your Crowdin project ID
api_token: your_api_token    # Replace with your Crowdin API token
base_path: ./
preserve_hierarchy: true
files:
  - source: docs/**/*.md
    translation: translations/%two_letters_code%/docs/%original_file_name%
  - source: src/**/*.json
    translation: translations/%two_letters_code%/src/%original_file_name%
  `;

  try {
    fs.writeFileSync(CROWDIN_CLI_CONFIG_PATH, crowdinConfig.trim());
    console.log('Crowdin CLI configuration file generated successfully.');
  } catch (error) {
    console.error(`Failed to generate Crowdin CLI configuration file: ${error.message}`);
  }
}

/**
 * Main function to initialize localization setup.
 */
function setupLocalization() {
  console.log('Starting localization setup...');
  updateDocusaurusConfig();
  generateCrowdinConfig();
  console.log('Localization setup completed successfully.');
}

// Execute the setup
setupLocalization();
```
