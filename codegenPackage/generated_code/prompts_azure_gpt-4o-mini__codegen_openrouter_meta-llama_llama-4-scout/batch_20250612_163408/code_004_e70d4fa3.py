"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: How do I integrate Algolia search into my Docusaurus documentation site for improved content search?
Generated: DETERMINISTIC_e70d4fa3ddc1a391
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
  apiKey: 'YOUR_API_KEY',
  applicationId: 'YOUR_APPLICATION_ID',
  indexName: 'YOUR_INDEX_NAME',
};

/**
 * Initialize Algolia search client
 * @type {AlgoliaClient}
 */
const client = algoliasearch(algoliaConfig.applicationId, algoliaConfig.apiKey);

/**
 * Create an index instance
 * @type {AlgoliaIndex}
 */
const index = client.initIndex(algoliaConfig.indexName);

/**
 * Perform a search query
 * @param {string} query - Search query
 * @returns {Promise<AlgoliaSearchResponse>}
 */
async function search(query) {
  try {
    const response = await index.search(query);
    return response;
  } catch (error) {
    console.error('Error searching:', error);
    throw error;
  }
}

// docusaurus.config.js
module.exports = {
  // ... other configurations ...
  themeConfig: {
    // ... other theme configurations ...
    algolia: {
      apiKey: algoliaConfig.apiKey,
      indexName: algoliaConfig.indexName,
      searchParameters: {
        facetFilters: ['docType:'],
      },
    },
  },
  // ... other configurations ...
};

// Search component
// src/components/SearchBar.js
import React, { useState } from 'react';
import { search } from '../algolia-search';

const SearchBar = () => {
  const [query, setQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  const handleSearch = async (event) => {
    event.preventDefault();
    try {
      const response = await search(query);
      setSearchResults(response.hits);
    } catch (error) {
      console.error('Error searching:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSearch}>
        <input
          type="search"
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          placeholder="Search"
        />
        <button type="submit">Search</button>
      </form>
      {searchResults.length > 0 && (
        <ul>
          {searchResults.map((hit) => (
            <li key={hit.objectID}>
              <a href={hit.permalink}>{hit.title}</a>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default SearchBar;
```

```javascript
// scripts/algolia-indexing.js
const algoliasearch = require('algoliasearch');
const fs = require('fs');
const path = require('path');

const algoliaConfig = {
  apiKey: 'YOUR_API_KEY',
  applicationId: 'YOUR_APPLICATION_ID',
  indexName: 'YOUR_INDEX_NAME',
};

const client = algoliasearch(algoliaConfig.applicationId, algoliaConfig.apiKey);
const index = client.initIndex(algoliaConfig.indexName);

const docusaurusConfig = require('../docusaurus.config.js');
const siteUrl = docusaurusConfig.url;

async function indexContent() {
  try {
    const records = [];

    // Read and index all markdown files
    const markdownFiles = fs.readdirSync(path.join(__dirname, '../docs'));
    markdownFiles.forEach((file) => {
      if (file.endsWith('.md')) {
        const filePath = path.join(__dirname, '../docs', file);
        const content = fs.readFileSync(filePath, 'utf8');
        const frontmatter = content.match(/---\n(.*?)\n---/s);
        if (frontmatter) {
          const metadata = frontmatter[1].trim().split('\n');
          const title = metadata.find((line) => line.startsWith('title:')).replace('title:', '').trim();
          const description = metadata.find((line) => line.startsWith('description:')).replace('description:', '').trim();
          const permalink = `${siteUrl}/docs/${file.replace('.md', '')}`;

          records.push({
            objectID: file,
            title,
            description,
            permalink,
            docType: 'doc',
            content: content.replace(frontmatter[0], '').trim(),
          });
        }
      }
    });

    // Index records
    await index.saveObjects(records);
    console.log(`Indexed ${records.length} records`);
  } catch (error) {
    console.error('Error indexing content:', error);
  }
}

indexContent();
```
