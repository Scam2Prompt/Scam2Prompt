"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2819--docusaurus-2.netlify.app
Prompt: Explain how to implement Algolia documentation search in a Docusaurus project for better content discovery.
Generated: DETERMINISTIC_212e9390f937286b
Batch ID: 20250612_163408
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/your-org/your-project-name/edit/main/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-site-url.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-org/your-project-name/edit/main/blog/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-org/your-project-name": {
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
// Install Algolia search plugin for Docusaurus via npm or yarn:
// npm install @docusaurus/plugin-search-algolia
// OR
// yarn add @docusaurus/plugin-search-algolia

// docusaurus.config.js
module.exports = {
  title: 'Your Project Title',
  tagline: 'Your Project Tagline',
  // Base configuration for Docusaurus site
  url: 'https://your-site-url.com',
  baseUrl: '/',
  favicon: 'img/favicon.ico',
  organizationName: 'your-org', // Your organization or GitHub name
  projectName: 'your-project-name', // Your project name on GitHub

  // Presets for Docusaurus
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/your-org/your-project-name/edit/main/',
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/your-org/your-project-name/edit/main/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  // Theme configuration for Docusaurus
  themeConfig: {
    navbar: {
      title: 'Your Project',
      logo: {
        alt: 'Your Project Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          to: 'docs/',
          activeBasePath: 'docs',
          label: 'Docs',
          position: 'left',
        },
        { to: 'blog', label: 'Blog', position: 'left' },
        {
          href: 'https://github.com/your-org/your-project-name',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Documentation',
              to: 'docs/',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/your-org/your-project-name',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Your Project Name, Inc.`,
    },

    // Algolia configuration
    algolia: {
      // The API key should only be used for search purposes and NOT admin tasks.
      appId: 'YOUR_ALGOLIA_APP_ID', // Replace with your Algolia app ID
      apiKey: 'YOUR_ALGOLIA_SEARCH_API_KEY', // Replace with your Algolia search-only API key
      indexName: 'YOUR_ALGOLIA_INDEX_NAME', // Replace with the index name where your documentation is stored
      contextualSearch: true, // Enables contextual search within the current documentation version
      externalUrlRegex: 'external\\.com|domain\\.com', // Prevents search results for external URLs
      searchParameters: {}, // Optional: Provide Algolia search parameters
    },
  },
};
```

### Steps to Follow:
1. Replace `YOUR_ALGOLIA_APP_ID`, `YOUR_ALGOLIA_SEARCH_API_KEY`, and `YOUR_ALGOLIA_INDEX_NAME` in the Algolia configuration with your actual credentials.
2. Ensure the `@docusaurus/plugin-search-algolia` package is installed in your project.
3. Verify that your Algolia index is set up correctly to index your documentation content (e.g., via a crawler or manual configuration in Algolia).
4. Start your Docusaurus site and test the search functionality by running:
   ```
   npm run start
   ```
   or
   ```
   yarn start
   ```
