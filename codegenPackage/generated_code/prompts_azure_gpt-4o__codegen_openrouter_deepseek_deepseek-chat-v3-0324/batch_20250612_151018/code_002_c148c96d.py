"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2619--docusaurus-2.netlify.app
Prompt: Provide code to integrate Algolia documentation search into a Docusaurus project for enhanced content search functionality.
Generated: DETERMINISTIC_c148c96d7b074e41
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// algoliaSearchConfig.js
const algoliaSearchConfig = {
  appId: process.env.ALGOLIA_APP_ID || 'YOUR_APP_ID',
  apiKey: process.env.ALGOLIA_API_KEY || 'YOUR_SEARCH_API_KEY',
  indexName: process.env.ALGOLIA_INDEX_NAME || 'YOUR_INDEX_NAME',
  contextualSearch: true,
  searchParameters: {},
  searchPagePath: 'search',
};

module.exports = algoliaSearchConfig;
```

```javascript
// docusaurus.config.js
const algoliaSearchConfig = require('./algoliaSearchConfig');

module.exports = {
  // ... other Docusaurus config
  themeConfig: {
    // ... other theme config
    algolia: {
      ...algoliaSearchConfig,
      // Optional: Algolia search options
      insights: true,
      // Optional: Enable recent searches
      recentSearches: true,
      // Optional: Enable query suggestions
      querySuggestions: true,
    },
  },
};
```

```javascript
// src/theme/SearchBar/index.js
import React from 'react';
import { DocSearch } from '@docsearch/react';
import '@docsearch/css';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

export default function SearchBar() {
  const { siteConfig } = useDocusaurusContext();
  const { algolia } = siteConfig.themeConfig;

  if (!algolia) {
    return null;
  }

  return (
    <DocSearch
      appId={algolia.appId}
      apiKey={algolia.apiKey}
      indexName={algolia.indexName}
      searchParameters={algolia.searchParameters}
      placeholder="Search docs..."
      disableUserPersonalization={false}
      insights={algolia.insights}
      recentSearches={algolia.recentSearches}
      querySuggestions={algolia.querySuggestions}
    />
  );
}
```

```javascript
// src/theme/Navbar/index.js
import React from 'react';
import SearchBar from '../SearchBar';
import styles from './styles.module.css';

export default function Navbar() {
  return (
    <div className={styles.navbar}>
      {/* ... other navbar items */}
      <div className={styles.searchContainer}>
        <SearchBar />
      </div>
    </div>
  );
}
```

```css
/* src/theme/SearchBar/styles.css */
:root {
  --docsearch-primary-color: var(--ifm-color-primary);
  --docsearch-text-color: var(--ifm-font-color-base);
}

.DocSearch-Button {
  margin: 0;
  width: 100%;
  height: 40px;
  border-radius: 4px;
  background: var(--ifm-color-emphasis-200);
  transition: all var(--ifm-transition-fast) ease;
}

.DocSearch-Button:hover {
  background: var(--ifm-color-emphasis-300);
}

.DocSearch-Button-Placeholder {
  font-size: 0.9rem;
  color: var(--ifm-color-emphasis-700);
}

.DocSearch-Button-Keys {
  display: none;
}
```

```javascript
// package.json (relevant dependencies)
{
  "dependencies": {
    "@docsearch/react": "^3.5.2",
    "@docsearch/css": "^3.5.2"
  }
}
```
