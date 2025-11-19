"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2728--docusaurus-2.netlify.app
Prompt: Suggest a library or API for translating Docusaurus documentation into multiple languages, referencing Crowdin integration.
Generated: DETERMINISTIC_380b319a5464c4a3
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules
const { execSync } = require('child_process');
const fs = require('fs');

// Function to integrate Crowdin for translating Docusaurus documentation
function integrateCrowdin() {
  try {
    // Check if Crowdin CLI is installed
    const crowdinVersion = execSync('crowdin --version', { encoding: 'utf-8' });
    console.log(`Crowdin CLI version: ${crowdinVersion.trim()}`);

    // Ensure the Crowdin configuration file exists
    const configFilePath = './crowdin.yml';
    if (!fs.existsSync(configFilePath)) {
      throw new Error(
        `Crowdin configuration file not found at ${configFilePath}. Please create a 'crowdin.yml' file.`
      );
    }

    console.log('Crowdin configuration file found.');

    // Run Crowdin CLI to upload source files
    console.log('Uploading source files to Crowdin...');
    execSync('crowdin upload sources', { stdio: 'inherit' });

    // Run Crowdin CLI to download translations
    console.log('Downloading translations from Crowdin...');
    execSync('crowdin download', { stdio: 'inherit' });

    console.log('Translation process completed successfully.');
  } catch (error) {
    // Handle errors gracefully
    console.error('Error during Crowdin integration:', error.message);
    process.exit(1);
  }
}

// Execute the integration function
integrateCrowdin();
```

### Notes:
1. Ensure you have the Crowdin CLI installed (`npm install -g @crowdin/cli`).
2. Create a `crowdin.yml` configuration file in the root directory of your project. This file should define the source files and target languages for translation.
3. Run this script in the root directory of your Docusaurus project.
