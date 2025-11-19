"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: Write a Docusaurus plugin that integrates Algolia documentation search into a site.
Generated: DETERMINISTIC_1b518de99b2ab1fc
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// @ts-check
// Docusaurus 2 plugin: Algolia documentation search

const algolia = require('algolia-client');
const { validate } = require('validate.js');

const DEFAULT_INDEX_NAME = 'docusaurus';
const DEFAULT_API_KEY = 'YOUR_API_KEY';
const DEFAULT_APP_ID = 'YOUR_APP_ID';

/**
 * @typedef {Object} AlgoliaPluginOptions
 * @property {string} [indexName=DEFAULT_INDEX_NAME] - Algolia index name
 * @property {string} apiKey - Algolia API key
 * @property {string} appId - Algolia application ID
 * @property {string} [searchParameters] - Algolia search parameters
 */

/**
 * @type {import('@docusaurus/types').Plugin}
 */
const algoliaPlugin = (context, options) => {
  const { indexName = DEFAULT_INDEX_NAME, apiKey, appId, searchParameters } = options;

  validate(options, {
    apiKey: { presence: true },
    appId: { presence: true },
  });

  const algoliaClient = new algolia.Client({
    apiKey,
    appId,
  });

  const index = algoliaClient.initIndex(indexName);

  if (searchParameters) {
    index.setSettings({ queryParameters: JSON.parse(searchParameters) });
  }

  return {
    name: 'docusaurus-plugin-algolia',
    async postBuild({ siteConfig, routes, actions }) {
      const { createData, fs } = actions;
      const docs = [];

      // Fetch all docs and extract relevant data
      routes.forEach((route) => {
        if (route.path.startsWith('/docs/')) {
          const docFile = route.module.file;
          const docContent = fs.readFileSync(docFile, 'utf8');
          const docData = {
            objectID: route.path,
            title: route.sidebar || '',
            content: docContent,
          };
          docs.push(docData);
        }
      });

      try {
        // Send docs to Algolia index
        await index.saveObjects(docs);
        await index.setSettings({
          attributesToSnippet: ['content:100'],
          attributesToHighlight: ['title'],
          snippetEllipsisText: '...',
          highlightPreTag: '<mark>',
          highlightPostTag: '</mark>',
        });
      } catch (error) {
        console.error('Error indexing docs:', error);
      }
    },
  };
};

module.exports = algoliaPlugin;
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... other config options ...
  plugins: [
    [
      require('./docusaurus-plugin-algolia'),
      {
        indexName: 'my-index',
        apiKey: 'YOUR_API_KEY',
        appId: 'YOUR_APP_ID',
      },
    ],
  ],
};
```
