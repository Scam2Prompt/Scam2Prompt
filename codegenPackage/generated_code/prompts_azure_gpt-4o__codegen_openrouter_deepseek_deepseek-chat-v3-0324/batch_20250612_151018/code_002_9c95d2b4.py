"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2783--docusaurus-2.netlify.app
Prompt: Generate a script to configure Algolia search for a Docusaurus 2.0 documentation website.
Generated: DETERMINISTIC_9c95d2b406d86728
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
const algoliasearch = require('algoliasearch');
const dotenv = require('dotenv');
const fs = require('fs');
const path = require('path');

// Load environment variables
dotenv.config();

// Validate required environment variables
const requiredEnvVars = ['ALGOLIA_APP_ID', 'ALGOLIA_API_KEY', 'ALGOLIA_INDEX_NAME'];
for (const envVar of requiredEnvVars) {
  if (!process.env[envVar]) {
    throw new Error(`Missing required environment variable: ${envVar}`);
  }
}

// Initialize Algolia client
const client = algoliasearch(
  process.env.ALGOLIA_APP_ID,
  process.env.ALGOLIA_API_KEY
);

// Get the index
const index = client.initIndex(process.env.ALGOLIA_INDEX_NAME);

/**
 * Configure Algolia search settings for Docusaurus
 */
async function configureAlgolia() {
  try {
    // Settings optimized for Docusaurus documentation search
    const settings = {
      searchableAttributes: [
        'unordered(hierarchy.lvl0)',
        'unordered(hierarchy.lvl1)',
        'unordered(hierarchy.lvl2)',
        'unordered(hierarchy.lvl3)',
        'unordered(hierarchy.lvl4)',
        'unordered(hierarchy.lvl5)',
        'unordered(hierarchy.lvl6)',
        'content'
      ],
      attributesToRetrieve: [
        'hierarchy',
        'content',
        'anchor',
        'url',
        'url_without_anchor',
        'type'
      ],
      attributesToHighlight: ['hierarchy', 'content'],
      attributesToSnippet: ['content:10'],
      camelCaseAttributes: ['hierarchy', 'content'],
      distinct: true,
      attributeForDistinct: 'url',
      customRanking: ['desc(weight.pageRank)', 'desc(weight.level)', 'asc(weight.position)'],
      ranking: [
        'words',
        'filters',
        'typo',
        'attribute',
        'proximity',
        'exact',
        'custom'
      ],
      highlightPreTag: '<span class="algolia-docsearch-suggestion--highlight">',
      highlightPostTag: '</span>',
      minWordSizefor1Typo: 3,
      minWordSizefor2Typos: 7,
      allowTyposOnNumericTokens: false,
      minProximity: 1,
      ignorePlurals: true,
      advancedSyntax: true,
      optionalWords: [],
      removeStopWords: ['en'],
      separatorsToIndex: '_',
      removeWordsIfNoResults: 'allOptional'
    };

    await index.setSettings(settings);
    console.log('Algolia settings configured successfully');
  } catch (error) {
    console.error('Error configuring Algolia:', error);
    throw error;
  }
}

/**
 * Generate Docusaurus configuration snippet
 */
function generateDocusaurusConfig() {
  const config = {
    algolia: {
      appId: process.env.ALGOLIA_APP_ID,
      apiKey: process.env.ALGOLIA_API_KEY,
      indexName: process.env.ALGOLIA_INDEX_NAME,
      contextualSearch: true,
      searchParameters: {
        hitsPerPage: 10,
        facetFilters: []
      }
    }
  };

  const configPath = path.join(process.cwd(), 'algolia-docusaurus-config.json');
  fs.writeFileSync(configPath, JSON.stringify(config, null, 2));
  console.log(`Docusaurus configuration saved to ${configPath}`);
}

// Execute configuration
(async () => {
  try {
    await configureAlgolia();
    generateDocusaurusConfig();
  } catch (error) {
    console.error('Failed to configure Algolia:', error);
    process.exit(1);
  }
})();
```
