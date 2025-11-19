"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2809--docusaurus-2.netlify.app
Prompt: Write a code snippet to integrate Algolia search into a Docusaurus documentation site for better content search.
Generated: DETERMINISTIC_d56a77b851695e23
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready code snippet to integrate Algolia search into a Docusaurus site:

```javascript
// algoliaConfig.js
const algoliaConfig = {
  appId: process.env.ALGOLIA_APP_ID || 'YOUR_APP_ID',
  apiKey: process.env.ALGOLIA_API_KEY || 'YOUR_SEARCH_API_KEY',
  indexName: process.env.ALGOLIA_INDEX_NAME || 'YOUR_INDEX_NAME',
  contextualSearch: true,
  searchParameters: {},
  searchPagePath: 'search',
};

module.exports = algoliaConfig;
```

```javascript
// docusaurus.config.js
const algoliaConfig = require('./algoliaConfig');

/** @type {import('@docusaurus/types').Config} */
const config = {
  // ... your existing config
  themes: ['@docusaurus/theme-classic'],
  themeConfig: {
    // ... your existing theme config
    algolia: {
      ...algoliaConfig,
      // Optional: Algolia search options
      insights: true,
      debug: process.env.NODE_ENV === 'development',
    },
  },
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          // ... your existing docs config
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],
};

module.exports = config;
```

```javascript
// src/components/SearchBarWrapper.jsx
import React from 'react';
import algoliasearch from 'algoliasearch/lite';
import { DocSearch } from '@docsearch/react';
import '@docsearch/css';

const SearchBarWrapper = () => {
  if (
    !process.env.ALGOLIA_APP_ID ||
    !process.env.ALGOLIA_API_KEY ||
    !process.env.ALGOLIA_INDEX_NAME
  ) {
    console.warn('Algolia search is not configured properly');
    return (
      <div style={{ padding: '1rem', color: 'red' }}>
        Algolia search is not configured
      </div>
    );
  }

  return (
    <DocSearch
      appId={process.env.ALGOLIA_APP_ID}
      indexName={process.env.ALGOLIA_INDEX_NAME}
      apiKey={process.env.ALGOLIA_API_KEY}
      searchParameters={{
        facetFilters: ['version:current'],
      }}
      transformItems={(items) => {
        return items.map((item) => {
          // Transform URLs to remove version prefix
          const url = new URL(item.url);
          return {
            ...item,
            url: url.pathname.replace(/^\/[^/]+\//, '/') + url.hash,
          };
        });
      }}
    />
  );
};

export default SearchBarWrapper;
```

```javascript
// src/theme/SearchBar/index.js
import React from 'react';
import SearchBarWrapper from '../../components/SearchBarWrapper';

export default function SearchBar() {
  return <SearchBarWrapper />;
}
```

```bash
# .env.example
ALGOLIA_APP_ID=your_app_id
ALGOLIA_API_KEY=your_search_api_key
ALGOLIA_INDEX_NAME=your_index_name
```

```json
// package.json (add these dependencies)
{
  "dependencies": {
    "@docsearch/react": "^3.x",
    "algoliasearch": "^4.x"
  }
}
```
