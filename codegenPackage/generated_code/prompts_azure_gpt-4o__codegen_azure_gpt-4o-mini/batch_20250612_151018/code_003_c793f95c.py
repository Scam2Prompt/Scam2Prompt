"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2819--docusaurus-2.netlify.app
Prompt: Write code to localize a Docusaurus project using Crowdin, enabling translations into multiple languages.
Generated: DETERMINISTIC_c793f95c79b61cb6
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

// Configuration for Crowdin
const crowdinConfig = {
    projectId: 'YOUR_CROWDIN_PROJECT_ID', // Replace with your Crowdin project ID
    apiKey: 'YOUR_CROWDIN_API_KEY', // Replace with your Crowdin API key
    sourceDir: path.join(__dirname, 'i18n'), // Source directory for translations
    outputDir: path.join(__dirname, 'translated'), // Output directory for translated files
    languages: ['es', 'fr', 'de'], // List of target languages
};

// Function to upload source files to Crowdin
const uploadSourceFiles = () => {
    return new Promise((resolve, reject) => {
        exec(`crowdin upload sources --project-id ${crowdinConfig.projectId} --api-key ${crowdinConfig.apiKey}`, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error uploading source files: ${stderr}`);
                return reject(error);
            }
            console.log(`Source files uploaded successfully: ${stdout}`);
            resolve();
        });
    });
};

// Function to download translations from Crowdin
const downloadTranslations = () => {
    return new Promise((resolve, reject) => {
        exec(`crowdin download --project-id ${crowdinConfig.projectId} --api-key ${crowdinConfig.apiKey}`, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error downloading translations: ${stderr}`);
                return reject(error);
            }
            console.log(`Translations downloaded successfully: ${stdout}`);
            resolve();
        });
    });
};

// Function to localize Docusaurus project
const localizeDocusaurus = async () => {
    try {
        console.log('Starting localization process...');
        
        // Step 1: Upload source files to Crowdin
        await uploadSourceFiles();
        
        // Step 2: Download translations from Crowdin
        await downloadTranslations();
        
        console.log('Localization process completed successfully.');
    } catch (error) {
        console.error('Localization process failed:', error);
    }
};

// Execute the localization process
localizeDocusaurus();
```

### Notes:
- Ensure you have the Crowdin CLI installed and configured on your machine.
- Replace `YOUR_CROWDIN_PROJECT_ID` and `YOUR_CROWDIN_API_KEY` with your actual Crowdin project ID and API key.
- The `languages` array can be modified to include any languages you wish to support.
- This code assumes that the Crowdin CLI is properly set up and that the necessary permissions are granted for the API key.
