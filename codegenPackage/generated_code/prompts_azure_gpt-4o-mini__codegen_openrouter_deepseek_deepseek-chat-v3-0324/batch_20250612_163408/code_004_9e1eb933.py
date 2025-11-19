"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: What is the process for translating Docusaurus documentation into multiple languages using Crowdin?
Generated: DETERMINISTIC_9e1eb93386b7bccd
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready script to automate Docusaurus documentation translation using Crowdin:

```javascript
const fs = require('fs');
const path = require('path');
const { CrowdinApi } = require('@crowdin/crowdin-api-client');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Configuration
const CONFIG = {
    CROWDIN_PROJECT_ID: process.env.CROWDIN_PROJECT_ID,
    CROWDIN_TOKEN: process.env.CROWDIN_TOKEN,
    DOCUSAURUS_I18N_DIR: path.join(process.cwd(), 'i18n'),
    SUPPORTED_LOCALES: ['es-ES', 'fr-FR', 'de-DE', 'ja-JP'], // Add your target languages
    SOURCE_LOCALE: 'en',
    FILE_PATTERNS: [
        'docs/**/*.md',
        'src/pages/**/*.md'
    ]
};

// Initialize Crowdin client
const { sourceFilesApi, translationsApi } = new CrowdinApi({
    token: CONFIG.CROWDIN_TOKEN
});

/**
 * Upload source files to Crowdin
 */
async function uploadSourceFiles() {
    try {
        for (const pattern of CONFIG.FILE_PATTERNS) {
            const files = await glob(pattern);
            for (const file of files) {
                const fileContent = fs.readFileSync(file, 'utf-8');
                const crowdinPath = file.replace(/^docs\//, '').replace(/^src\/pages\//, '');
                
                await sourceFilesApi.createOrUpdateFile(
                    CONFIG.CROWDIN_PROJECT_ID,
                    crowdinPath,
                    {
                        content: fileContent,
                        importOptions: {
                            cleanTags: true,
                            translateHiddenText: false
                        }
                    }
                );
                console.log(`Uploaded: ${file}`);
            }
        }
    } catch (error) {
        console.error('Error uploading source files:', error);
        throw error;
    }
}

/**
 * Download translations from Crowdin
 */
async function downloadTranslations() {
    try {
        const buildId = await translationsApi.buildProject(CONFIG.CROWDIN_PROJECT_ID);
        const buildStatus = await translationsApi.checkBuildStatus(CONFIG.CROWDIN_PROJECT_ID, buildId.data.id);
        
        if (buildStatus.data.status === 'finished') {
            const downloadUrl = await translationsApi.downloadTranslations(CONFIG.CROWDIN_PROJECT_ID, buildId.data.id);
            
            // Extract and save translations to i18n directory
            const translations = await fetch(downloadUrl.data.url).then(res => res.json());
            for (const locale of CONFIG.SUPPORTED_LOCALES) {
                const localeDir = path.join(CONFIG.DOCUSAURUS_I18N_DIR, locale);
                if (!fs.existsSync(localeDir)) {
                    fs.mkdirSync(localeDir, { recursive: true });
                }
                
                // Process each translated file
                for (const [filePath, content] of Object.entries(translations[locale])) {
                    const fullPath = path.join(localeDir, filePath);
                    fs.writeFileSync(fullPath, content);
                    console.log(`Saved translation: ${fullPath}`);
                }
            }
        }
    } catch (error) {
        console.error('Error downloading translations:', error);
        throw error;
    }
}

/**
 * Main workflow
 */
async function main() {
    try {
        console.log('Starting translation process...');
        await uploadSourceFiles();
        await downloadTranslations();
        console.log('Translation process completed successfully!');
    } catch (error) {
        console.error('Translation process failed:', error);
        process.exit(1);
    }
}

// Helper function to glob files
function glob(pattern) {
    return new Promise((resolve, reject) => {
        require('glob')(pattern, (err, files) => {
            if (err) reject(err);
            resolve(files);
        });
    });
}

// Run the script
main();
```

Sample `.env` file:

```ini
CROWDIN_PROJECT_ID=your_project_id
CROWDIN_TOKEN=your_crowdin_token
```

Sample `package.json` dependencies:

```json
{
  "dependencies": {
    "@crowdin/crowdin-api-client": "^1.0.0",
    "dotenv": "^16.0.0",
    "glob": "^8.0.0"
  }
}
```
mple usage
(async () => {
  const translator = new DocusaurusCrowdinTranslator();
  
  // Initialize setup (run once)
  // await translator.setup();
  
  // Regular sync process
  await translator.syncTranslations();
})();
```

Sample `.env` file:

```ini
# Crowdin API Configuration
CROWDIN_PROJECT_ID=your_project_id
CROWDIN_API_KEY=your_api_key

# Docusaurus Configuration
DOCUSAURUS_BASE_DIR=./website
SUPPORTED_LOCALES=es,fr,de,ja
```

Sample `package.json` dependencies:

```json
{
  "dependencies": {
    "axios": "^1.6.2",
    "dotenv": "^16.3.1"
  }
}
```
