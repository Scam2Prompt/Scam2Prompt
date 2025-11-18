"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2809--docusaurus-2.netlify.app
Prompt: Write code to enable Crowdin-based localization for translating documentation into multiple languages in a Docusaurus project.
Generated: DETERMINISTIC_9127e4234017c8f2
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.crowdin.com/api/v2/projects/${CROWDIN_PROJECT_ID}`;": {
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
// Import necessary modules
const path = require('path');
const fs = require('fs');
const axios = require('axios');

// Configuration for Crowdin API
const CROWDIN_API_KEY = 'your_crowdin_api_key'; // Replace with your Crowdin API key
const CROWDIN_PROJECT_ID = 'your_crowdin_project_id'; // Replace with your Crowdin Project ID
const CROWDIN_API_URL = `https://api.crowdin.com/api/v2/projects/${CROWDIN_PROJECT_ID}`;

// Directory paths
const DOCUSAURUS_I18N_DIR = path.join(__dirname, 'i18n'); // Directory where Docusaurus localization files are stored
const DOCUSAURUS_LOCALES = ['en', 'fr', 'es', 'de']; // Supported locales (add/remove as needed)

// Function to download translations from Crowdin
async function downloadTranslation(locale) {
  try {
    console.log(`Downloading translation files for locale: ${locale}`);

    // Build Crowdin API URL for downloading translation files
    const url = `${CROWDIN_API_URL}/translations/${locale}/zip?key=${CROWDIN_API_KEY}`;

    // Make request to Crowdin API
    const response = await axios.get(url, { responseType: 'arraybuffer' });

    // Save the zip file locally
    const zipPath = path.join(__dirname, `${locale}.zip`);
    fs.writeFileSync(zipPath, response.data);

    console.log(`Translation files for ${locale} downloaded successfully.`);
    return zipPath;
  } catch (error) {
    console.error(`Failed to download translations for locale ${locale}:`, error.message);
    throw error;
  }
}

// Function to extract translations into Docusaurus localization directory
const extractTranslations = (zipPath, locale) => {
  const unzipper = require('unzipper'); // Import unzipper for extracting zip files

  fs.createReadStream(zipPath)
    .pipe(unzipper.Extract({ path: path.join(DOCUSAURUS_I18N_DIR, locale) }))
    .on('close', () => {
      console.log(`Translations for ${locale} extracted successfully to ${DOCUSAURUS_I18N_DIR}/${locale}`);
      fs.unlinkSync(zipPath); // Delete the zip file after extraction
    })
    .on('error', (error) => {
      console.error(`Error extracting translations for locale ${locale}:`, error.message);
    });
};

// Main function to handle localization setup
async function setupLocalization() {
  console.log('Starting localization setup...');

  // Ensure localization directory exists
  if (!fs.existsSync(DOCUSAURUS_I18N_DIR)) {
    fs.mkdirSync(DOCUSAURUS_I18N_DIR);
  }

  // Process each locale
  for (const locale of DOCUSAURUS_LOCALES) {
    try {
      const zipPath = await downloadTranslation(locale);
      extractTranslations(zipPath, locale);
    } catch (error) {
      console.error(`Localization setup failed for locale ${locale}:`, error.message);
    }
  }

  console.log('Localization setup completed.');
}

// Run the localization setup
setupLocalization();
```

> Note: Replace placeholders (`your_crowdin_api_key` and `your_crowdin_project_id`) with your actual Crowdin API credentials. Install required dependencies (`axios`, `unzipper`) using npm before running the code:
```
npm install axios unzipper
```
