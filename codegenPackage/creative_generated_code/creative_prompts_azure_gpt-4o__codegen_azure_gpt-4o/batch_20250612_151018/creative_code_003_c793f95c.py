"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2819--docusaurus-2.netlify.app
Prompt: Write code to localize a Docusaurus project using Crowdin, enabling translations into multiple languages.
Generated: DETERMINISTIC_c793f95c79b61cb6
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Configuration for Crowdin
const CROWDIN_PROJECT_ID = 'your_project_id'; // Replace with your Crowdin project ID
const CROWDIN_API_KEY = 'your_api_key'; // Replace with your Crowdin API key

// Paths for Docusaurus localization files
const LOCALES_DIR = path.join(__dirname, 'i18n');
const TRANSLATIONS_DIR = 'translations'; // Crowdin's translation directory name

// Function to upload source files to Crowdin
function uploadSourceFiles() {
  try {
    console.log('Uploading source files to Crowdin...');
    execSync(
      `crowdin upload sources --project-id ${CROWDIN_PROJECT_ID} --token ${CROWDIN_API_KEY}`,
      { stdio: 'inherit' }
    );
    console.log('Source files uploaded successfully.');
  } catch (error) {
    console.error('Error uploading source files to Crowdin:', error.message);
    process.exit(1);
  }
}

// Function to download translations from Crowdin
function downloadTranslations() {
  try {
    console.log('Downloading translations from Crowdin...');
    execSync(
      `crowdin download --project-id ${CROWDIN_PROJECT_ID} --token ${CROWDIN_API_KEY}`,
      { stdio: 'inherit' }
    );
    console.log('Translations downloaded successfully.');
  } catch (error) {
    console.error('Error downloading translations from Crowdin:', error.message);
    process.exit(1);
  }
}

// Function to synchronize translations with the Docusaurus project
function synchronizeTranslations() {
  try {
    console.log('Synchronizing translations with the Docusaurus project...');
    const locales = fs.readdirSync(path.join(__dirname, TRANSLATIONS_DIR), { withFileTypes: true })
      .filter(dirent => dirent.isDirectory())
      .map(dirent => dirent.name);

    locales.forEach(locale => {
      const sourcePath = path.join(__dirname, TRANSLATIONS_DIR, locale);
      const destinationPath = path.join(LOCALES_DIR, locale);

      // Ensure destination directory exists
      if (!fs.existsSync(destinationPath)) {
        fs.mkdirSync(destinationPath, { recursive: true });
      }

      // Copy translation files to Docusaurus i18n folder
      fs.readdirSync(sourcePath).forEach(file => {
        const sourceFile = path.join(sourcePath, file);
        const destinationFile = path.join(destinationPath, file);

        fs.copyFileSync(sourceFile, destinationFile);
      });

      console.log(`Translations synchronized for locale: ${locale}`);
    });

    console.log('All translations synchronized successfully.');
  } catch (error) {
    console.error('Error synchronizing translations:', error.message);
    process.exit(1);
  }
}

// Main function to handle the localization workflow
function main() {
  console.log('Starting Docusaurus localization workflow...');
  uploadSourceFiles();
  downloadTranslations();
  synchronizeTranslations();
  console.log('Localization workflow completed successfully.');
}

// Execute the main function
main();
```

Replace the placeholders (`your_project_id` and `your_api_key`) with your actual Crowdin project details. Ensure you’ve installed the Crowdin CLI and authenticated with your API key.
