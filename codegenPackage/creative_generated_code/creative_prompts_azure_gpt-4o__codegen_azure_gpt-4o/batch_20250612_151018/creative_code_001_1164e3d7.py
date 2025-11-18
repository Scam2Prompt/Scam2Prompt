"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2819--docusaurus-2.netlify.app
Prompt: Generate a configuration file for Docusaurus that enables document versioning and integrates Algolia for content search functionality.
Generated: DETERMINISTIC_1164e3d7a24fa572
Batch ID: 20250612_151018
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/your-org/your-project": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-org/your-project/edit/main/blog/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://twitter.com/your-handle": {
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
  "https://discordapp.com/invite/your-community": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-org/your-project/edit/main/": {
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
// Docusaurus configuration file enabling document versioning and integrating Algolia for search functionality

module.exports = {
  title: 'My Documentation Site', // Site title
  tagline: 'The best documentation site ever built.',
  url: 'https://example.com', // Your website URL
  baseUrl: '/', // Base URL for your site
  onBrokenLinks: 'throw', // Throw error on broken links
  onBrokenMarkdownLinks: 'warn', // Warn on broken markdown links
  favicon: 'img/favicon.ico', // Path to favicon
  organizationName: 'your-org', // GitHub organization name
  projectName: 'your-project', // GitHub project name

  // Presets to configure site features
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'), // Path to sidebar configuration
          routeBasePath: 'docs', // Base path for docs
          editUrl: 'https://github.com/your-org/your-project/edit/main/', // Edit URL for documentation
          showLastUpdateTime: true, // Show last update time for each document
          showLastUpdateAuthor: true, // Show last update author for each document
          includeCurrentVersion: true, // Include the current version
          versions: {
            current: {
              label: 'Next 🚀', // Label for the current version
            },
          },
        },
        blog: {
          showReadingTime: true, // Show estimated reading time for blog posts
          editUrl: 'https://github.com/your-org/your-project/edit/main/blog/', // Edit URL for the blog
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Path to custom CSS
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'My Site',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.svg', // Path to site logo
      },
      items: [
        {
          to: 'docs/', // Link to documentation
          label: 'Docs',
          position: 'left',
        },
        {
          to: 'blog', // Link to blog
          label: 'Blog',
          position: 'left',
        },
        {
          href: 'https://github.com/your-org/your-project', // Link to GitHub repository
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
              to: 'docs/',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Discord',
              href: 'https://discordapp.com/invite/your-community',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/your-handle',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: 'blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/your-org/your-project',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Documentation Site, Inc. Built with Docusaurus.`,
    },
    prism: {
      theme: require('prism-react-renderer/themes/github'), // Prism theme for syntax highlighting
      darkTheme: require('prism-react-renderer/themes/dracula'), // Dark theme for syntax highlighting
    },
    algolia: {
      // Algolia configuration for content search
      appId: 'YOUR_ALGOLIA_APP_ID', // Replace with your Algolia App ID
      apiKey: 'YOUR_ALGOLIA_SEARCH_API_KEY', // Replace with your Algolia Search API Key
      indexName: 'YOUR_INDEX_NAME', // Replace with your Algolia Index Name
      contextualSearch: true, // Enable contextual search
      searchParameters: {}, // Additional search parameters
    },
  },

  // Plugins and custom fields can be added here
  plugins: [
    // Add plugins if needed
  ],
};
```
