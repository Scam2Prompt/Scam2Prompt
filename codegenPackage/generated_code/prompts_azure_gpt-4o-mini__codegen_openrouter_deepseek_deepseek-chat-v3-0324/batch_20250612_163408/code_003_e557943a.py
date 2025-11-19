"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2619--docusaurus-2.netlify.app
Prompt: How do I integrate Algolia search into my Docusaurus documentation for better content discovery?
Generated: DETERMINISTIC_e557943a2088415d
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation for integrating Algolia search into Docusaurus:

```javascript
// algoliaConfig.js
const algoliaConfig = {
  appId: process.env.ALGOLIA_APP_ID || 'YOUR_APP_ID',
  apiKey: process.env.ALGOLIA_API_KEY || 'YOUR_SEARCH_API_KEY',
  indexName: process.env.ALGOLIA_INDEX_NAME || 'YOUR_INDEX_NAME',
  contextualSearch: true,
  searchParameters: {
    hitsPerPage: 10,
    attributesToSnippet: ['description:30'],
    snippetEllipsisText: '...',
  },
};

module.exports = algoliaConfig;
```

```javascript
// docusaurus.config.js
const algoliaConfig = require('./algoliaConfig');

module.exports = {
  // ... other Docusaurus config
  themeConfig: {
    // ... other theme config
    algolia: {
      ...algoliaConfig,
      // Optional: Algolia search options
      searchPagePath: 'search',
      // Optional: Transform search items for better display
      transformItems(items) {
        return items.map((item) => ({
          ...item,
          url: item.url.replace('#__docusaurus', ''),
        }));
      },
    },
  },
};
```

```javascript
// scripts/algoliaDocSearch.js
const fs = require('fs');
const path = require('path');
const matter = require('gray-matter');
const algoliasearch = require('algoliasearch');

const algoliaConfig = require('../algoliaConfig');

const client = algoliasearch(algoliaConfig.appId, algoliaConfig.apiKey);
const index = client.initIndex(algoliaConfig.indexName);

async function indexDocs(docsDir) {
  try {
    const files = getMarkdownFiles(docsDir);
    const records = [];

    for (const file of files) {
      const content = fs.readFileSync(file, 'utf8');
      const { data, content: body } = matter(content);
      const relativePath = path.relative(docsDir, file);
      const url = `/docs/${relativePath.replace('.md', '')}`;

      records.push({
        objectID: relativePath,
        title: data.title || path.basename(file, '.md'),
        description: data.description || '',
        content: body,
        url,
        headings: data.headings || [],
      });
    }

    await index.saveObjects(records);
    console.log(`Successfully indexed ${records.length} documents`);
  } catch (error) {
    console.error('Error indexing documents:', error);
    process.exit(1);
  }
}

function getMarkdownFiles(dir) {
  return fs.readdirSync(dir).reduce((files, file) => {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      return [...files, ...getMarkdownFiles(fullPath)];
    } else if (path.extname(file) === '.md') {
      return [...files, fullPath];
    }
    return files;
  }, []);
}

// Run indexing if this script is called directly
if (require.main === module) {
  const docsDir = path.join(__dirname, '..', 'docs');
  indexDocs(docsDir);
}

module.exports = indexDocs;
```

```json
// package.json (partial)
{
  "scripts": {
    "index-docs": "node scripts/algoliaDocSearch.js",
    "build": "docusaurus build && npm run index-docs"
  },
  "dependencies": {
    "algoliasearch": "^4.0.0",
    "gray-matter": "^4.0.0"
  }
}
```

```env
# .env.example
ALGOLIA_APP_ID=your_app_id
ALGOLIA_API_KEY=your_admin_api_key
ALGOLIA_INDEX_NAME=your_index_name
```

```javascript
// src/theme/SearchBar/index.js
import React from 'react';
import { DocSearch } from '@docsearch/react';
import '@docsearch/css';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

export default function SearchBar() {
  const { siteConfig } = useDocusaurusContext();
  
  return (
    <DocSearch
      appId={siteConfig.themeConfig.algolia.appId}
      apiKey={siteConfig.themeConfig.algolia.apiKey}
      indexName={siteConfig.themeConfig.algolia.indexName}
      searchParameters={siteConfig.themeConfig.algolia.searchParameters}
      transformItems={siteConfig.themeConfig.algolia.transformItems}
    />
  );
}
```
