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
// algolia-config.js

const algoliasearch = require('algoliasearch');

/**
 * Configuration for Algolia Search
 * @module AlgoliaConfig
 */

class AlgoliaConfig {
  constructor(appId, apiKey, indexName) {
    if (!appId || !apiKey || !indexName) {
      throw new Error('Algolia appId, apiKey, and indexName must be provided');
    }

    this.client = algoliasearch(appId, apiKey);
    this.index = this.client.initIndex(indexName);
  }

  /**
   * Uploads documents to the Algolia index
   * @param {Array} documents - Array of documents to index
   * @returns {Promise} - Promise indicating the result of the indexing operation
   */
  async uploadDocuments(documents) {
    if (!Array.isArray(documents) || documents.length === 0) {
      throw new Error('Documents must be a non-empty array');
    }

    try {
      const response = await this.index.saveObjects(documents, {
        autoGenerateObjectIDIfNotExist: true,
      });
      console.log('Documents indexed successfully:', response);
      return response;
    } catch (error) {
      console.error('Error indexing documents:', error);
      throw new Error('Document indexing failed');
    }
  }

  /**
   * Clears the current index
   * @returns {Promise} - Promise indicating the result of the clearing operation
   */
  async clearIndex() {
    try {
      const response = await this.index.clearObjects();
      console.log('Index cleared successfully:', response);
      return response;
    } catch (error) {
      console.error('Error clearing index:', error);
      throw new Error('Failed to clear the index');
    }
  }
}

// Example usage (uncomment to use):
// const algoliaConfig = new AlgoliaConfig('YourApplicationID', 'YourAdminAPIKey', 'YourIndexName');
// const documents = [
//   { objectID: '1', title: 'Document 1', content: 'Content for document 1' },
//   { objectID: '2', title: 'Document 2', content: 'Content for document 2' },
// ];

// (async () => {
//   await algoliaConfig.clearIndex();
//   await algoliaConfig.uploadDocuments(documents);
// })();

module.exports = AlgoliaConfig;
```

Make sure to replace `'YourApplicationID'`, `'YourAdminAPIKey'`, and `'YourIndexName'` with the actual values from your Algolia account.
