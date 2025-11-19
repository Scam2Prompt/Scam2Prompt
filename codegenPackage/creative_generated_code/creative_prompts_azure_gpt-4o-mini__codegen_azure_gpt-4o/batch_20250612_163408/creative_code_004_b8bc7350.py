"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2783--docusaurus-2.netlify.app
Prompt: What is the process for translating my Docusaurus documentation into multiple languages using Crowdin?
Generated: DETERMINISTIC_b8bc7350a5cfbed3
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Script to integrate Crowdin with Docusaurus for multilingual documentation
 * 
 * Requirements:
 * - Node.js should be installed
 * - Crowdin CLI should be installed and configured
 * - This script assumes you have a Crowdin project set up
 * - Docusaurus project should be initialized
 * 
 * Steps:
 * 1. Upload your source files to Crowdin
 * 2. Download translated files from Crowdin
 * 3. Integrate translations into your Docusaurus site
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Configuration for Crowdin
const CROWDIN_PROJECT_ID = 'your-crowdin-project-id'; // Replace with your Crowdin project ID
const DOCUSAURUS_I18N_DIR = path.join(__dirname, 'i18n'); // Path to Docusaurus i18n directory

/**
 * Executes a shell command and logs output/error
 * @param {string} command - Shell command to execute
 * @throws Will throw an error if the command fails
 */
function executeCommand(command) {
  try {
    console.log(`Executing: ${command}`);
    const output = execSync(command, { stdio: 'inherit' });
    return output;
  } catch (error) {
    console.error(`Error executing command: ${command}`);
    console.error(error.message);
    process.exit(1);
  }
}

/**
 * Uploads source files (e.g., English documentation) to Crowdin
 */
function uploadToCrowdin() {
  console.log('Uploading source files to Crowdin...');
  executeCommand(`crowdin upload sources --project-id=${CROWDIN_PROJECT_ID}`);
  console.log('Source files uploaded successfully.');
}

/**
 * Downloads translated files from Crowdin
 */
function downloadFromCrowdin() {
  console.log('Downloading translated files from Crowdin...');
  executeCommand(`crowdin download --project-id=${CROWDIN_PROJECT_ID}`);
  console.log('Translated files downloaded successfully.');
}

/**
 * Integrates translations into the Docusaurus i18n directory
 */
function integrateTranslations() {
  console.log('Integrating translations into Docusaurus...');
  
  const crowdinTranslationsDir = path.join(__dirname, 'crowdin-translations'); // Adjust based on Crowdin CLI output
  if (!fs.existsSync(crowdinTranslationsDir)) {
    console.error('Crowdin translations directory does not exist.');
    process.exit(1);
  }

  // Check if i18n directory exists, create if not
  if (!fs.existsSync(DOCUSAURUS_I18N_DIR)) {
    console.log('Creating Docusaurus i18n directory...');
    fs.mkdirSync(DOCUSAURUS_I18N_DIR, { recursive: true });
  }

  // Move translations into the Docusaurus i18n directory
  fs.readdirSync(crowdinTranslationsDir).forEach((language) => {
    const srcDir = path.join(crowdinTranslationsDir, language);
    const destDir = path.join(DOCUSAURUS_I18N_DIR, language);

    console.log(`Processing language: ${language}`);
    fs.cpSync(srcDir, destDir, { recursive: true });
    console.log(`Language ${language} integrated successfully.`);
  });

  console.log('Translations integrated successfully.');
}

/**
 * Main function to handle the translation process
 */
function main() {
  console.log('Starting Docusaurus translation process with Crowdin...');
  
  // Step 1: Upload source files to Crowdin
  uploadToCrowdin();

  // Step 2: Download translated files from Crowdin
  downloadFromCrowdin();

  // Step 3: Integrate translations into Docusaurus
  integrateTranslations();

  console.log('Docusaurus translation process completed successfully.');
}

// Run the script
main();
```

**Notes**:
- Replace placeholders such as `your-crowdin-project-id` with actual values from your Crowdin setup.
- Ensure that the Crowdin CLI is installed and configured (`crowdin init`).
- This script assumes source files are configured properly in your Crowdin project and mapped to Docusaurus translation files. Adjust paths and logic as needed.
