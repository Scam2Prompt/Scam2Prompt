"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2728--docusaurus-2.netlify.app
Prompt: What is the process for integrating Algolia documentation search into my Docusaurus site for improved content search?
Generated: DETERMINISTIC_761c75ce390dd080
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's the code to integrate Algolia search into a Docusaurus site:

```javascript
// docusaurus.config.js
module.exports = {
  // ... existing config ...
  themeConfig: {
    // ... existing theme config ...
    algolia: {
      // Algolia search configuration
      appId: 'YOUR_APP_ID', // Replace with your Algolia app ID
      apiKey: 'YOUR_SEARCH_API_KEY', // Replace with your Algolia search API key (public)
      indexName: 'YOUR_INDEX_NAME', // Replace with your Algolia index name
      contextualSearch: true, // Enable contextual search
      searchParameters: {}, // Additional search parameters
      searchPagePath: 'search', // Path for the search page
    },
  },
};
```

```javascript
// src/theme/SearchBar/index.js
import React from 'react';
import algoliasearch from 'algoliasearch/lite';
import { DocSearch } from '@docsearch/react';
import '@docsearch/css';

export default function SearchBar() {
  return (
    <DocSearch
      appId="YOUR_APP_ID" // Same as above
      apiKey="YOUR_SEARCH_API_KEY" // Same as above
      indexName="YOUR_INDEX_NAME" // Same as above
      placeholder="Search docs..."
      transformItems={(items) => {
        return items.map((item) => {
          // Transform the items to remove the hash or query parameters from the URL
          const url = new URL(item.url);
          if (url.hash === '#__docusaurus') {
            url.hash = '';
          }
          return {
            ...item,
            url: url.href,
          };
        });
      }}
    />
  );
}
```

```json
// package.json
{
  "dependencies": {
    "@docsearch/react": "^3.x",
    "algoliasearch": "^4.x"
  }
}
```

```javascript
// scripts/algolia.js
const algoliasearch = require('algoliasearch');
const { JSDOM } = require('jsdom');
const fs = require('fs');
const path = require('path');

const client = algoliasearch('YOUR_APP_ID', 'YOUR_ADMIN_API_KEY'); // Replace with admin API key
const index = client.initIndex('YOUR_INDEX_NAME'); // Same index name as above

async function extractContent(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const dom = new JSDOM(content);
  const document = dom.window.document;
  
  return {
    title: document.title,
    content: document.body.textContent
      .replace(/\s+/g, ' ')
      .trim(),
    url: filePath
      .replace(process.cwd(), '')
      .replace('/build/', ''),
    objectID: path.basename(filePath),
  };
}

async function indexAllFiles() {
  const files = await fs.promises.readdir(path.join(process.cwd(), 'build'));
  const records = [];
  
  for (const file of files) {
    if (file.endsWith('.html')) {
      const record = await extractContent(path.join(process.cwd(), 'build', file));
      records.push(record);
    }
  }
  
  try {
    await index.saveObjects(records);
    console.log('Successfully indexed content to Algolia');
  } catch (error) {
    console.error('Error indexing content:', error);
  }
}

indexAllFiles();
```
