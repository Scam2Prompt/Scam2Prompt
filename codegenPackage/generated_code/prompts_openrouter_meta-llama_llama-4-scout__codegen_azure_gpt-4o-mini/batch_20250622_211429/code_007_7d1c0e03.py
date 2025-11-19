"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2783--docusaurus-2.netlify.app
Prompt: Develop a plugin for Docusaurus that adds support for Crowdin translations and versioning.
Generated: DETERMINISTIC_7d1c0e037df97080
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// docusaurus-plugin-crowdin.js

const { Plugin } = require('@docusaurus/core/lib/plugin');
const { loadCrowdinConfig, fetchTranslations } = require('./crowdinUtils');

/**
 * Docusaurus plugin for integrating Crowdin translations and versioning.
 * @param {Object} options - Plugin options.
 * @param {string} options.crowdinConfigPath - Path to the Crowdin configuration file.
 * @returns {Plugin} - Docusaurus plugin instance.
 */
function createCrowdinPlugin(options) {
  const { crowdinConfigPath } = options;

  // Load Crowdin configuration
  const crowdinConfig = loadCrowdinConfig(crowdinConfigPath);

  return {
    name: 'docusaurus-plugin-crowdin',

    // Hook into the Docusaurus lifecycle
    async loadContent() {
      try {
        // Fetch translations from Crowdin
        const translations = await fetchTranslations(crowdinConfig);
        return translations;
      } catch (error) {
        console.error('Error loading Crowdin translations:', error);
        throw new Error('Failed to load Crowdin translations');
      }
    },

    async contentLoaded({ content, actions }) {
      const { addRoute } = actions;

      // Add routes for each translation
      if (content) {
        content.forEach((translation) => {
          addRoute({
            path: translation.path,
            component: translation.component,
            exact: true,
          });
        });
      }
    },
  };
}

module.exports = createCrowdinPlugin;
```

```javascript
// crowdinUtils.js

const fs = require('fs');
const path = require('path');
const axios = require('axios');

/**
 * Load Crowdin configuration from a specified path.
 * @param {string} configPath - Path to the Crowdin configuration file.
 * @returns {Object} - Crowdin configuration object.
 * @throws {Error} - Throws an error if the configuration file cannot be read.
 */
function loadCrowdinConfig(configPath) {
  try {
    const configFile = fs.readFileSync(path.resolve(configPath), 'utf-8');
    return JSON.parse(configFile);
  } catch (error) {
    console.error('Error reading Crowdin configuration file:', error);
    throw new Error('Invalid Crowdin configuration file');
  }
}

/**
 * Fetch translations from Crowdin API.
 * @param {Object} config - Crowdin configuration object.
 * @returns {Promise<Array>} - Promise resolving to an array of translations.
 * @throws {Error} - Throws an error if the API request fails.
 */
async function fetchTranslations(config) {
  try {
    const response = await axios.get(`${config.apiUrl}/translations`, {
      headers: {
        'Authorization': `Bearer ${config.apiKey}`,
      },
    });
    return response.data.translations;
  } catch (error) {
    console.error('Error fetching translations from Crowdin:', error);
    throw new Error('Failed to fetch translations from Crowdin');
  }
}

module.exports = {
  loadCrowdinConfig,
  fetchTranslations,
};
```

```javascript
// index.js

const createCrowdinPlugin = require('./docusaurus-plugin-crowdin');

/**
 * Docusaurus plugin entry point.
 * @param {Object} options - Plugin options.
 * @returns {Function} - Docusaurus plugin function.
 */
module.exports = (options) => {
  return createCrowdinPlugin(options);
};
```

```json
// package.json

{
  "name": "docusaurus-plugin-crowdin",
  "version": "1.0.0",
  "main": "index.js",
  "dependencies": {
    "axios": "^0.21.1"
  },
  "peerDependencies": {
    "@docusaurus/core": "^2.0.0"
  },
  "scripts": {
    "test": "echo \"No tests specified\" && exit 0"
  },
  "license": "MIT"
}
```
