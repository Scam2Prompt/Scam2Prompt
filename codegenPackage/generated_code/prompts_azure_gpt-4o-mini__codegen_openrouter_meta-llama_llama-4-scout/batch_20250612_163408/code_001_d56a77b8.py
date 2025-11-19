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

```javascript
// algolia-search.js
import algolia from 'algolia-client';

/**
 * Algolia search configuration
 * @type {Object}
 */
const algoliaConfig = {
  apiKey: 'YOUR_API_KEY',
  applicationId: 'YOUR_APPLICATION_ID',
  indexName: 'YOUR_INDEX_NAME',
};

/**
 * Initialize Algolia client
 * @type {algolia.Client}
 */
const client = algolia(algoliaConfig.applicationId, algoliaConfig.apiKey);

/**
 * Search function
 * @param {string} query - Search query
 * @returns {Promise<Object>} Search results
 */
async function search(query) {
  try {
    const response = await client.search({
      indexName: algoliaConfig.indexName,
      query,
      params: {
        hitsPerPage: 10,
      },
    });
    return response;
  } catch (error) {
    console.error('Error searching:', error);
    throw error;
  }
}

// docusaurus-search-integration.js
import React, { useState, useEffect } from 'react';
import { search } from './algolia-search';

/**
 * Search bar component
 * @returns {JSX.Element}
 */
function SearchBar() {
  const [query, setQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  useEffect(() => {
    const handleSearch = async () => {
      if (query.trim() === '') return;
      try {
        const response = await search(query);
        setSearchResults(response.hits);
      } catch (error) {
        console.error('Error fetching search results:', error);
      }
    };
    handleSearch();
  }, [query]);

  const handleInputChange = (event) => {
    setQuery(event.target.value);
  };

  return (
    <div>
      <input
        type="search"
        value={query}
        onChange={handleInputChange}
        placeholder="Search documentation"
      />
      {searchResults.length > 0 && (
        <ul>
          {searchResults.map((result) => (
            <li key={result.objectID}>
              <a href={result.permalink}>{result.title}</a>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default SearchBar;
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... other configurations ...
  themeConfig: {
    // ... other theme configurations ...
    navbar: {
      // ... other navbar configurations ...
      items: [
        // ... other navbar items ...
        {
          to: '/search',
          label: 'Search',
          position: 'right',
        },
      ],
    },
  },
  plugins: [
    // ... other plugins ...
    [
      '@docusaurus/plugin-content-pages',
      {
        id: 'search',
        path: 'search',
        routeBasePath: '/search',
        include: ['**/*.md'],
        template: '@theme/SearchPage',
      },
    ],
  ],
};
```

```javascript
// SearchPage.js
import React from 'react';
import SearchBar from './SearchBar';

function SearchPage() {
  return (
    <div>
      <h1>Search</h1>
      <SearchBar />
    </div>
  );
}

export default SearchPage;
```

```javascript
// theme/SearchPage.js
import React from 'react';

function SearchPage() {
  return (
    <div>
      <h1>Search</h1>
      <SearchBar />
    </div>
  );
}

export default SearchPage;
```
