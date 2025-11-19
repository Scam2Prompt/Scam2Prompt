"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: Implement a search function in a Docusaurus site using Algolia documentation search.
Generated: DETERMINISTIC_b67c0bc39f0861b7
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// algolia-search.js
import algoliasearch from 'algoliasearch/lite';
import { docSearch } from '@docsearch/react';
import '@docsearch/css';

// Initialize Algolia search client
const searchClient = algoliasearch(
  process.env.ALGOLIA_APP_ID,
  process.env.ALGOLIA_SEARCH_API_KEY
);

// DocSearch configuration
const docSearchConfig = {
  appId: process.env.ALGOLIA_APP_ID,
  apiKey: process.env.ALGOLIA_SEARCH_API_KEY,
  indexName: process.env.ALGOLIA_INDEX_NAME,
  container: '#docsearch',
  debug: process.env.NODE_ENV === 'development',
};

// Search component
function Search() {
  return docSearch({
    ...docSearchConfig,
    transformItems(items) {
      return items.map((item) => {
        // Transform URLs to remove hash links
        const url = new URL(item.url);
        if (url.hash === '#__docusaurus') {
          url.hash = '';
        }
        return {
          ...item,
          url: url.href,
        };
      });
    },
  });
}

// Error handling wrapper component
function SafeSearch() {
  try {
    return <Search />;
  } catch (error) {
    console.error('Algolia search failed to initialize:', error);
    return (
      <div className="search-error">
        Search functionality is currently unavailable. Please try again later.
      </div>
    );
  }
}

export default SafeSearch;
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... other config
  themeConfig: {
    // ... other theme config
    algolia: {
      appId: 'YOUR_APP_ID',
      apiKey: 'YOUR_SEARCH_API_KEY',
      indexName: 'YOUR_INDEX_NAME',
      contextualSearch: true,
      searchParameters: {},
      searchPagePath: 'search',
    },
  },
};
```

```css
/* src/css/custom.css */
:root {
  --docsearch-primary-color: var(--ifm-color-primary);
  --docsearch-text-color: var(--ifm-font-color-base);
}

.DocSearch-Button {
  margin: 0;
  width: 100%;
  background: var(--ifm-color-secondary-lightest);
  border-radius: 4px;
  padding: 0.5rem 1rem;
}

.DocSearch-Button-Placeholder {
  font-size: 0.9rem;
}

.DocSearch-Button-Keys {
  display: none;
}

.DocSearch-Container {
  z-index: 1000;
}
```
