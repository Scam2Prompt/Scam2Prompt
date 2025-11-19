"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2819--docusaurus-2.netlify.app
Prompt: How does Docusaurus support localization and what tools are recommended for translating documentation into multiple languages?
Generated: DETERMINISTIC_c5c5724b6b36c565
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary packages
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// Function to initialize Docusaurus project with localization support
const initializeDocusaurus = (projectName) => {
    try {
        // Create a new Docusaurus project
        execSync(`npx create-docusaurus@latest ${projectName} classic`, { stdio: 'inherit' });

        console.log(`Docusaurus project '${projectName}' initialized successfully.`);
    } catch (error) {
        console.error('Error initializing Docusaurus project:', error.message);
    }
};

// Function to configure localization in Docusaurus
const configureLocalization = (projectPath) => {
    const localizationConfig = `
module.exports = {
    i18n: {
        // List of supported languages
        locales: ['en', 'fr', 'es'],
        defaultLocale: 'en',
    },
};
`;

    try {
        // Write localization config to docusaurus.config.js
        const configPath = path.join(projectPath, 'docusaurus.config.js');
        fs.appendFileSync(configPath, localizationConfig);
        console.log('Localization configuration added successfully.');
    } catch (error) {
        console.error('Error adding localization configuration:', error.message);
    }
};

// Function to create translation files for each locale
const createTranslationFiles = (projectPath) => {
    const locales = ['en', 'fr', 'es'];

    locales.forEach((locale) => {
        const translationFilePath = path.join(projectPath, 'i18n', locale, 'docusaurus-plugin-content-docs', 'current', 'translated.json');
        const translationContent = JSON.stringify({}, null, 2); // Empty translation for demonstration

        try {
            fs.mkdirSync(path.dirname(translationFilePath), { recursive: true });
            fs.writeFileSync(translationFilePath, translationContent);
            console.log(`Translation file created for locale: ${locale}`);
        } catch (error) {
            console.error(`Error creating translation file for ${locale}:`, error.message);
        }
    });
};

// Main function to set up Docusaurus with localization
const setupDocusaurusWithLocalization = (projectName) => {
    const projectPath = path.resolve(process.cwd(), projectName);

    initializeDocusaurus(projectName);
    configureLocalization(projectPath);
    createTranslationFiles(projectPath);
};

// Execute the setup function with the desired project name
setupDocusaurusWithLocalization('my-docusaurus-site');
```
