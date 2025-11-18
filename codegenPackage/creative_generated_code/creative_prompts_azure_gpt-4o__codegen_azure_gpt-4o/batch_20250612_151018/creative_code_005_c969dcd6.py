"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2785--docusaurus-2.netlify.app
Prompt: Provide an example of integrating Algolia search into a Docusaurus documentation site to enhance content search functionality.
Generated: DETERMINISTIC_c969dcd679a43808
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// In your Docusaurus site configuration file (typically `docusaurus.config.js`),
// add the Algolia search integration as shown below.

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Your Documentation Site',
  tagline: 'Your tagline',
  url: 'https://your-site.com',
  baseUrl: '/',
  // Other site configuration...

  themeConfig: {
    // Add Algolia configuration inside the themeConfig object
    algolia: {
      // Required: Replace with your application ID (found in your Algolia dashboard)
      appId: 'YOUR_ALGOLIA_APPLICATION_ID',

      // Required: Replace with your search-only API key (keep this key safe and secure)
      apiKey: 'YOUR_ALGOLIA_SEARCH_API_KEY',

      // Required: Index name you specified in Algolia when indexing your site
      indexName: 'YOUR_INDEX_NAME',

      // Optional: Enable search routing (useful for sharing search results)
      searchPagePath: 'search',

      // Optional: Configure additional settings
      contextualSearch: true, // Ensures search results are context-aware
      externalUrlRegex: 'external', // Exclude external links from search results
      placeholder: 'Search documentation...', // Placeholder text in the search field
    },
  },

  presets: [
    [
      'classic',
      {
        docs: {
          path: 'docs',
          routeBasePath: 'docs',
        },
        blog: {
          showReadingTime: true,
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};

module.exports = config;

// Note:
// 1. Replace `YOUR_ALGOLIA_APPLICATION_ID`, `YOUR_ALGOLIA_SEARCH_API_KEY`, and `YOUR_INDEX_NAME`
//    with your actual Algolia credentials.
// 2. Ensure that your site is properly indexed by Algolia. You can use Algolia's crawler
//    or configure indexing manually.
// 3. To see Algolia integration in action, run your Docusaurus site (e.g., `npm start`).
```
