"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: Write a script to configure Algolia search for a Docusaurus-powered documentation site.
Generated: DETERMINISTIC_8f0a7f228bd8e026
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// algoliaConfig.js

/**
 * Configures Algolia search for a Docusaurus-powered documentation site.
 * This script should be placed in the `scripts` directory of your Docusaurus project.
 */

const fs = require('fs');
const path = require('path');

// Validate environment variables
const validateEnvVars = () => {
  const requiredVars = [
    'ALGOLIA_APP_ID',
    'ALGOLIA_API_KEY',
    'ALGOLIA_INDEX_NAME'
  ];

  const missingVars = requiredVars.filter(varName => !process.env[varName]);
  if (missingVars.length > 0) {
    throw new Error(
      `Missing required environment variables: ${missingVars.join(', ')}`
    );
  }
};

// Generate Algolia configuration for Docusaurus
const generateAlgoliaConfig = () => {
  validateEnvVars();

  const config = {
    appId: process.env.ALGOLIA_APP_ID,
    apiKey: process.env.ALGOLIA_API_KEY,
    indexName: process.env.ALGOLIA_INDEX_NAME,
    contextualSearch: true,
    searchParameters: {},
    searchPagePath: 'search',
  };

  return config;
};

// Write configuration to docusaurus.config.js
const updateDocusaurusConfig = (algoliaConfig) => {
  const configPath = path.join(process.cwd(), 'docusaurus.config.js');
  
  if (!fs.existsSync(configPath)) {
    throw new Error('docusaurus.config.js not found in current directory');
  }

  let configContent = fs.readFileSync(configPath, 'utf8');
  
  // Check if themeConfig exists
  if (!configContent.includes('themeConfig:')) {
    throw new Error('themeConfig not found in docusaurus.config.js');
  }

  // Check if algolia configuration already exists
  if (configContent.includes('algolia:')) {
    configContent = configContent.replace(
      /algolia:[\s\S]*?}(?=,|\n|$)/,
      `algolia: ${JSON.stringify(algoliaConfig, null, 2)}`
    );
  } else {
    // Insert algolia config into themeConfig
    configContent = configContent.replace(
      /themeConfig:\s*{/,
      `themeConfig: {\n      algolia: ${JSON.stringify(algoliaConfig, null, 2)},`
    );
  }

  fs.writeFileSync(configPath, configContent);
  console.log('Successfully updated docusaurus.config.js with Algolia configuration');
};

// Main execution
try {
  const algoliaConfig = generateAlgoliaConfig();
  updateDocusaurusConfig(algoliaConfig);
} catch (error) {
  console.error('Error configuring Algolia for Docusaurus:');
  console.error(error.message);
  process.exit(1);
}
```
