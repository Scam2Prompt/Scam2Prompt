"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2785--docusaurus-2.netlify.app
Prompt: Provide an example of integrating Algolia search into a Docusaurus documentation site to enhance content search functionality.
Generated: DETERMINISTIC_c969dcd679a43808
Batch ID: 20250612_151018
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
  applicationId: 'YOUR_APPLICATION_ID',
  apiKey: 'YOUR_API_KEY',
  indexName: 'YOUR_INDEX_NAME',
};

/**
 * Initialize Algolia search client
 * @type {AlgoliaSearchClient}
 */
const searchClient = algoliasearch(algoliaConfig.applicationId, algoliaConfig.apiKey);

/**
 * Create a search index
 * @type {AlgoliaIndex}
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
        // Optional parameters to customize search results
        facetFilters: ['docType:doc'],
      },
    },
  },
  // ... other configurations ...
};

// SearchBar.js
import React, { useState } from 'react';
import { InstantSearch, SearchBox, Hits, Highlight } from 'react-instantsearch-dom-react';

const SearchBar = () => {
  const [searchQuery, setSearchQuery] = useState('');

  const handleSearch = (event) => {
    setSearchQuery(event.target.value);
  };

  return (
    <InstantSearch
      searchClient={searchClient}
      indexName={algoliaConfig.indexName}
      onSearchParameters={ (searchState, searchResults) => {
        // Optional callback to customize search parameters
      }}
    >
      <SearchBox
        value={searchQuery}
        onChange={handleSearch}
        placeholder="Search documentation"
      />
      <Hits
        hitComponent={({ hit }) => (
          <div>
            <Highlight attribute="title" hit={hit} />
            <p>
              <Highlight attribute="content" hit={hit} />
            </p>
          </div>
        )}
      />
    </InstantSearch>
  );
};

export default SearchBar;

// _document.js (for Docusaurus 2)
import React from 'react';
import { Html, Head, Main, NextScript } from '@docusaurus/typography';
import SearchBar from './SearchBar';

const Document = (props) => {
  return (
    <Html {...props.htmlAttributes}>
      <Head {...props.headAttributes}>
        {/* Add custom meta tags or stylesheets here */}
      </Head>
      <body {...props.bodyAttributes}>
        {props.preBodyTags}
        <Main />
        <NextScript />
        <SearchBar />
      </body>
    </Html>
  );
};

export default Document;

// script to add docs to Algolia index
// add-to-algolia-index.js
const axios = require('axios');
const { searchClient, searchIndex } = require('./algolia-search');

const docusaurusContent = [
  // retrieve your Docusaurus content here
  // for example:
  {
    objectID: 'doc-1',
    title: 'Doc 1 title',
    content: 'This is the content of doc 1',
    docType: 'doc',
  },
];

const addDocumentsToIndex = async () => {
  try {
    const response = await searchIndex.saveObjects(docusaurusContent);
    console.log(`Indexed ${response.objectIDs.length} documents`);
  } catch (error) {
    console.error('Error indexing documents:', error);
  }
};

addDocumentsToIndex();
```
