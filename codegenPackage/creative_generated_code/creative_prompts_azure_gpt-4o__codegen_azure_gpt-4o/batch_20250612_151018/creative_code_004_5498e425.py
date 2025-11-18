"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2735--docusaurus-2.netlify.app
Prompt: Demonstrate how to use Crowdin with Docusaurus to localize documentation into multiple languages.
Generated: DETERMINISTIC_5498e425ae84834a
Batch ID: 20250612_151018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://docusaurus.io/docs/installation": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://support.crowdin.com/cli-tool/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// This script demonstrates integrating Crowdin with Docusaurus to localize documentation.
// It assumes you have already set up your Crowdin project and the Docusaurus site.

// Requirements:
// - Node.js installed
// - Crowdin CLI installed: https://support.crowdin.com/cli-tool/
// - A Docusaurus project initialized: https://docusaurus.io/docs/installation

const fs = require('fs');
const path = require('path');
const execSync = require('child_process').execSync;

// Crowdin configuration file path
const CROWDIN_CONFIG_PATH = path.resolve(__dirname, 'crowdin.yml');

// Docusaurus localization folders
const DOCUSAURUS_I18N_DIR = path.resolve(__dirname, 'i18n');

// Ensure directories exist
if (!fs.existsSync(CROWDIN_CONFIG_PATH)) {
  throw new Error(`Crowdin configuration file not found at: ${CROWDIN_CONFIG_PATH}`);
}

if (!fs.existsSync(DOCUSAURUS_I18N_DIR)) {
  fs.mkdirSync(DOCUSAURUS_I18N_DIR, { recursive: true });
}

// Function to pull translated files from Crowdin
function pullTranslations() {
  try {
    console.log('Pulling translations from Crowdin...');
    execSync('crowdin download', { stdio: 'inherit' });
    console.log('Translations successfully pulled.');
  } catch (error) {
    console.error('Error pulling translations from Crowdin:', error.message);
    process.exit(1);
  }
}

// Function to push source files to Crowdin
function pushSourceFiles() {
  try {
    console.log('Pushing source files to Crowdin...');
    execSync('crowdin upload sources', { stdio: 'inherit' });
    console.log('Source files successfully pushed.');
  } catch (error) {
    console.error('Error pushing source files to Crowdin:', error.message);
    process.exit(1);
  }
}

// Function to map translations into Docusaurus i18n structure
function mapTranslations() {
  const crowdinTranslationsDir = path.resolve(__dirname, 'crowdin-translations');

  if (!fs.existsSync(crowdinTranslationsDir)) {
    throw new Error('No Crowdin translations directory found.');
  }

  console.log('Mapping translations into Docusaurus i18n structure...');
  const languages = fs.readdirSync(crowdinTranslationsDir);

  languages.forEach((lang) => {
    const langDir = path.join(DOCUSAURUS_I18N_DIR, lang);
    if (!fs.existsSync(langDir)) {
      fs.mkdirSync(langDir, { recursive: true });
    }

    const translationFiles = fs.readdirSync(path.join(crowdinTranslationsDir, lang));
    translationFiles.forEach((file) => {
      const srcFilePath = path.join(crowdinTranslationsDir, lang, file);
      const destFilePath = path.join(langDir, file);
      fs.copyFileSync(srcFilePath, destFilePath);
    });
  });

  console.log('Translations mapped successfully.');
}

// Main script execution
try {
  console.log('Starting Crowdin integration with Docusaurus...');
  pushSourceFiles(); // Push source files to Crowdin
  pullTranslations(); // Pull translated files from Crowdin
  mapTranslations(); // Map translations to Docusaurus
  console.log('Crowdin integration completed successfully.');
} catch (error) {
  console.error('Error during Crowdin integration:', error.message);
  process.exit(1);
}
```
