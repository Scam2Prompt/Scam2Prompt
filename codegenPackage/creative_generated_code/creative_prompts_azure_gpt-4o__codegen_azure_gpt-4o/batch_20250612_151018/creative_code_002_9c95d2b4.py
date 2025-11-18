"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2783--docusaurus-2.netlify.app
Prompt: Generate a script to configure Algolia search for a Docusaurus 2.0 documentation website.
Generated: DETERMINISTIC_9c95d2b406d86728
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

// Configuration settings for Algolia search
const algoliaConfig = {
  apiKey: 'YOUR_ALGOLIA_API_KEY', // Replace with your actual API key
  indexName: 'YOUR_ALGOLIA_INDEX_NAME', // Replace with your actual index name
  appId: 'YOUR_ALGOLIA_APP_ID', // Replace with your actual App ID
};

// Path to Docusaurus configuration file
const docusaurusConfigPath = path.resolve(__dirname, 'docusaurus.config.js');

// Function to configure Algolia search in Docusaurus
function configureAlgoliaSearch() {
  if (!fs.existsSync(docusaurusConfigPath)) {
    console.error('Error: Docusaurus configuration file not found at', docusaurusConfigPath);
    return;
  }

  try {
    const docusaurusConfig = require(docusaurusConfigPath);

    // Check if the themeConfig object exists
    if (!docusaurusConfig.themeConfig) {
      docusaurusConfig.themeConfig = {};
    }

    // Configure Algolia search within themeConfig
    docusaurusConfig.themeConfig.algolia = {
      appId: algoliaConfig.appId,
      apiKey: algoliaConfig.apiKey,
      indexName: algoliaConfig.indexName,
    };

    // Save the updated configuration back to the file
    fs.writeFileSync(
      docusaurusConfigPath,
      `module.exports = ${JSON.stringify(docusaurusConfig, null, 2)};`,
      'utf8'
    );

    console.log('Algolia search configuration added successfully.');
  } catch (error) {
    console.error('Error while configuring Algolia search:', error.message);
  }
}

// Execute the configuration function
configureAlgoliaSearch();
```

Replace `YOUR_ALGOLIA_API_KEY`, `YOUR_ALGOLIA_INDEX_NAME`, and `YOUR_ALGOLIA_APP_ID` with your respective Algolia credentials before running the script.
