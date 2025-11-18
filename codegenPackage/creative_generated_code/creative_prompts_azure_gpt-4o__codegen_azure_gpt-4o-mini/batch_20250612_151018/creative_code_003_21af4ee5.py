"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: Provide code to integrate Crowdin for translating Docusaurus documentation into multiple languages.
Generated: DETERMINISTIC_21af4ee54c1ca37c
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.crowdin.com/api/v2": {
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
const CROWDIN_API_URL = 'https://api.crowdin.com/api/v2';
const PROJECT_ID = 'YOUR_PROJECT_ID'; // Replace with your Crowdin project ID
const API_KEY = 'YOUR_API_KEY'; // Replace with your Crowdin API key

/**
 * Uploads the Docusaurus documentation files to Crowdin for translation.
 * @param {string} filePath - The path to the documentation file to upload.
 * @returns {Promise<void>}
 */
async function uploadFileToCrowdin(filePath) {
    try {
        const fileName = path.basename(filePath);
        const response = await axios.post(`${CROWDIN_API_URL}/projects/${PROJECT_ID}/files`, {
            name: fileName,
            path: `docs/${fileName}` // Path in Crowdin
        }, {
            headers: {
                'Authorization': `Bearer ${API_KEY}`,
                'Content-Type': 'application/json'
            }
        });

        // Upload the file to Crowdin
        const uploadResponse = await axios.post(`${CROWDIN_API_URL}/projects/${PROJECT_ID}/files/${response.data.data.id}/content`, fs.readFileSync(filePath), {
            headers: {
                'Authorization': `Bearer ${API_KEY}`,
                'Content-Type': 'application/octet-stream'
            }
        });

        console.log(`Successfully uploaded: ${fileName}`);
    } catch (error) {
        console.error(`Error uploading file ${filePath}:`, error.response ? error.response.data : error.message);
    }
}

/**
 * Uploads all markdown files from the Docusaurus documentation directory to Crowdin.
 * @param {string} docsDir - The directory containing the Docusaurus documentation.
 * @returns {Promise<void>}
 */
async function uploadDocsDirectory(docsDir) {
    try {
        const files = fs.readdirSync(docsDir).filter(file => file.endsWith('.md'));

        for (const file of files) {
            const filePath = path.join(docsDir, file);
            await uploadFileToCrowdin(filePath);
        }
    } catch (error) {
        console.error(`Error reading directory ${docsDir}:`, error.message);
    }
}

// Main function to initiate the upload process
(async () => {
    const docsDir = path.join(__dirname, 'docs'); // Adjust the path to your docs directory

    console.log('Starting upload of Docusaurus documentation to Crowdin...');
    await uploadDocsDirectory(docsDir);
    console.log('Upload process completed.');
})();
```

**Note:** Remember to replace `YOUR_PROJECT_ID` and `YOUR_API_KEY` with the actual values from your Crowdin account. Ensure that the `axios` library is installed in your project by running `npm install axios`. Place this code in a JavaScript file and execute it in an environment that has access to your Crowdin API. Adjust the path to the documentation directory as necessary.
