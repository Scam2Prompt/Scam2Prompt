"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Generate an example of how to implement Algolia search in a Docusaurus documentation site for better content discoverability.
Generated: DETERMINISTIC_a66e86268cab0095
Batch ID: 20250612_163408
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/example-org/example-repo/edit/main/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/example-org/example-repo": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://my-doc-site.com": {
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
// docusaurus.config.js
// This is the main configuration file for your Docusaurus project.
// The following code shows how to integrate Algolia search for better content discoverability.

module.exports = {
  title: 'My Documentation Site', // Title of your site
  tagline: 'Documentation for everything', // Tagline
  url: 'https://my-doc-site.com', // URL of your site
  baseUrl: '/', // Base URL path
  onBrokenLinks: 'throw', // Error handling for broken links
  onBrokenMarkdownLinks: 'warn', // Error handling for broken markdown links
  favicon: 'img/favicon.ico', // Path to favicon
  organizationName: 'example-org', // GitHub org/user name
  projectName: 'example-repo', // GitHub repo name

  // Theme configuration
  themeConfig: {
    navbar: {
      title: 'My Site',
      logo: {
        alt: 'Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        { to: 'docs/', label: 'Docs', position: 'left' },
        { to: 'blog', label: 'Blog', position: 'left' },
        { href: 'https://github.com/example-org/example-repo', label: 'GitHub', position: 'right' },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Getting Started',
              to: 'docs/getting-started',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/example-org/example-repo',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Documentation Site`,
    },
    prism: {
      theme: require('prism-react-renderer/themes/dracula'),
    },

    // Algolia configuration
    algolia: {
      // Replace the following with your Algolia credentials
      appId: 'YOUR_ALGOLIA_APP_ID', // Algolia App ID
      apiKey: 'YOUR_ALGOLIA_SEARCH_API_KEY', // Search-only API key
      indexName: 'YOUR_ALGOLIA_INDEX_NAME', // Index name
      contextualSearch: true, // Enables contextual search
      externalUrlRegex: 'external\\.com|docs\\.another-domain\\.com', // Regex for external URLs
      searchParameters: {}, // Optional search parameters
      debug: false, // Enable when debugging
    },
  },

  // Presets configuration
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/example-org/example-repo/edit/main/',
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/example-org/example-repo/edit/main/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
```

Note:
1. Replace `YOUR_ALGOLIA_APP_ID`, `YOUR_ALGOLIA_SEARCH_API_KEY`, and `YOUR_ALGOLIA_INDEX_NAME` with your actual Algolia credentials.
2. Install the required dependencies: `npm install @docusaurus/theme-search-algolia prism-react-renderer`.
