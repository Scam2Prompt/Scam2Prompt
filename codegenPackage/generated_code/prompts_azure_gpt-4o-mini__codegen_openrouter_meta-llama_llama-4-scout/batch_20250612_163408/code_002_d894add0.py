"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: Can you provide a code example for setting up Algolia search in a Docusaurus documentation site?
Generated: DETERMINISTIC_d894add0ee251a3a
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// algolia-search.js
import algoliasearch from 'algoliasearch';

/**
 * Algolia search configuration
 * @type {Object}
 */
const algoliaConfig = {
  apiKey: 'YOUR_API_KEY', // Replace with your Algolia API key
  indexName: 'YOUR_INDEX_NAME', // Replace with your Algolia index name
  appId: 'YOUR_APP_ID', // Replace with your Algolia app ID
};

/**
 * Initialize Algolia search client
 * @type {algoliasearch.Client}
 */
const searchClient = algoliasearch(algoliaConfig.appId, algoliaConfig.apiKey);

/**
 * Create a search index
 * @type {algoliasearch.Index}
 */
const searchIndex = searchClient.initIndex(algoliaConfig.indexName);

// docusaurus.config.js
module.exports = {
  // ... other configurations ...
  themeConfig: {
    // ... other theme configurations ...
    algolia: {
      apiKey: algoliaConfig.apiKey,
      indexName: algoliaConfig.indexName,
      searchParameters: {
        // Optional parameters to pass to Algolia's search API
        facetFilters: ['docType:docs'],
      },
    },
  },
  // ... other configurations ...
};

// script to index documents
const fs = require('fs');
const path = require('path');
const { DocusaurusConfig } = require('./docusaurus.config');

const indexDocuments = async () => {
  try {
    // Get all documents
    const documents = [];
    const dirPath = path.join(DocusaurusConfig.outDir, 'docs');
    const files = fs.readdirSync(dirPath);
    files.forEach((file) => {
      if (file.endsWith('.json')) {
        const filePath = path.join(dirPath, file);
        const fileContent = fs.readFileSync(filePath, 'utf8');
        const fileData = JSON.parse(fileContent);
        documents.push({
          objectID: fileData.id,
          title: fileData.title,
          content: fileData.content,
          docType: 'docs',
        });
      }
    });

    // Index documents in Algolia
    const index = searchClient.initIndex(algoliaConfig.indexName);
    await index.saveObjects(documents);
    console.log('Indexed documents in Algolia');
  } catch (error) {
    console.error('Error indexing documents:', error);
  }
};

indexDocuments();
```
