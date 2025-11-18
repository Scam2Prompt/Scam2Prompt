"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2820--docusaurus-2.netlify.app
Prompt: Generate a configuration file for Docusaurus that integrates Algolia for documentation search functionality.
Generated: DETERMINISTIC_72d041c1bdef7de3
Batch ID: 20250612_151018
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/my-org/my-docs/edit/main/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/my-org/my-docs/edit/main/blog/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/my-org/my-docs": {
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
// Configuration file for Docusaurus
// This file includes Algolia integration for documentation search functionality.

module.exports = {
  // Basic site information
  title: 'My Documentation Site',
  tagline: 'Documentation powered by Docusaurus and Algolia',
  url: 'https://example.com', // Your website URL
  baseUrl: '/', // Base URL for your site
  onBrokenLinks: 'throw', // Throw error for broken links
  onBrokenMarkdownLinks: 'warn', // Warn for broken markdown links
  favicon: 'img/favicon.ico', // Path to your favicon

  // Project metadata
  organizationName: 'my-org', // GitHub organization or user name
  projectName: 'my-docs', // Repository name
  trailingSlash: false,

  // Localization settings
  i18n: {
    defaultLocale: 'en',
    locales: ['en'], // List of supported locales
  },

  // Presets configuration (theme and docs)
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'), // Path to your sidebar config
          editUrl: 'https://github.com/my-org/my-docs/edit/main/', // Link to edit pages on GitHub
        },
        blog: {
          showReadingTime: true, // Display estimated reading time for blog posts
          editUrl: 'https://github.com/my-org/my-docs/edit/main/blog/', // Link to edit blog posts on GitHub
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Path to your custom CSS file
        },
      }),
    ],
  ],

  // Theme configuration including Algolia search integration
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'My Documentation Site',
        logo: {
          alt: 'Site Logo',
          src: 'img/logo.svg', // Path to your logo image
        },
        items: [
          {
            to: '/docs/intro',
            label: 'Docs',
            position: 'left',
          },
          {
            to: '/blog',
            label: 'Blog',
            position: 'left',
          },
          {
            href: 'https://github.com/my-org/my-docs',
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
                label: 'Getting Started',
                to: '/docs/intro',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/my-org/my-docs',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'Blog',
                to: '/blog',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} My Documentation Site, Inc.`,
      },
      prism: {
        theme: require('prism-react-renderer/themes/dracula'), // Syntax highlighting theme
      },
      // Algolia search configuration
      algolia: {
        appId: 'YOUR_APP_ID', // Replace with your Algolia App ID
        apiKey: 'YOUR_SEARCH_API_KEY', // Replace with your Algolia Search API Key
        indexName: 'YOUR_INDEX_NAME', // Replace with your Algolia index name
        contextualSearch: true, // Enables contextual search
        searchPagePath: 'search', // Path to a dedicated search page (optional)
      },
    }),
};
```
