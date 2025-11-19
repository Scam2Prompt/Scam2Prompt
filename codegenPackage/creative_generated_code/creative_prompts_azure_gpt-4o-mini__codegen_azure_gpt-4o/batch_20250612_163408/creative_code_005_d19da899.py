"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: Provide a guide on setting up localization in Docusaurus using Crowdin for a multi-language documentation site.
Generated: DETERMINISTIC_d19da8999177ef48
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.crowdin.com/api/v2/projects/${PROJECT_ID}/translations/${language}`;": {
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
// scripts/crowdinSync.js
// This script automates the synchronization of localization files between Docusaurus and Crowdin.
// Ensure that you have installed dependencies: 'dotenv', 'fs-extra', and 'axios'.

// Import necessary modules
const fs = require('fs-extra');
const path = require('path');
const axios = require('axios');
require('dotenv').config();

// Crowdin API credentials (store these in a .env file)
const CROWDIN_API_KEY = process.env.CROWDIN_API_KEY;
const PROJECT_ID = process.env.CROWDIN_PROJECT_ID;

// Paths to Docusaurus localization directories
const LOCALIZATION_DIR = path.join(__dirname, '..', 'i18n');

// Function to upload files to Crowdin
async function uploadToCrowdin(language, filePath) {
  const fileName = path.basename(filePath);

  try {
    const url = `https://api.crowdin.com/api/v2/projects/${PROJECT_ID}/translations/${language}`;
    const formData = new FormData();
    formData.append('file', fs.createReadStream(filePath));

    const response = await axios.post(url, formData, {
      headers: {
        Authorization: `Bearer ${CROWDIN_API_KEY}`,
        ...formData.getHeaders(),
      },
    });

    console.log(`Successfully uploaded ${fileName} for ${language}`);
  } catch (error) {
    console.error(`Failed to upload ${fileName} for ${language}:`, error.message);
  }
}

// Function to download files from Crowdin
async function downloadFromCrowdin(language, outputDir) {
  try {
    const url = `https://api.crowdin.com/api/v2/projects/${PROJECT_ID}/translations/${language}`;
    
    const response = await axios.get(url, {
      headers: {
        Authorization: `Bearer ${CROWDIN_API_KEY}`,
      },
      responseType: 'stream',
    });

    const filePath = path.join(outputDir, `${language}.json`);
    const writer = fs.createWriteStream(filePath);

    response.data.pipe(writer);

    writer.on('finish', () => {
      console.log(`Successfully downloaded translations for ${language} into ${filePath}`);
    });

    writer.on('error', (error) => {
      console.error(`Failed to download translations for ${language}:`, error.message);
    });
  } catch (error) {
    console.error(`Error fetching translations for ${language}:`, error.message);
  }
}

// Function to synchronize localization files
async function syncLocalization() {
  try {
    const languages = fs.readdirSync(LOCALIZATION_DIR);

    for (const language of languages) {
      const languageDir = path.join(LOCALIZATION_DIR, language);
      const translationFilePath = path.join(languageDir, 'translated.json');

      // Upload local translations to Crowdin
      if (fs.existsSync(translationFilePath)) {
        await uploadToCrowdin(language, translationFilePath);
      }

      // Download updated translations from Crowdin
      await downloadFromCrowdin(language, languageDir);
    }
  } catch (error) {
    console.error('Error in localization synchronization:', error.message);
  }
}

// Run the synchronization script
syncLocalization();
```

**Note:**
- Add a `.env` file with `CROWDIN_API_KEY` and `CROWDIN_PROJECT_ID` for authentication.
- Ensure the `i18n` directory exists and contains language subdirectories.
- Run the script with `node scripts/crowdinSync.js` to synchronize translations.
