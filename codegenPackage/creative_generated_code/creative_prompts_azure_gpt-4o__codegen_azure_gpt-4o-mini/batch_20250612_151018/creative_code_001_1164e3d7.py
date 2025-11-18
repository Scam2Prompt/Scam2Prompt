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
  "https://github.com/your-org/your-project/edit/main/README.md": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://discord.com/invite/docusaurus": {
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
  "https://stackoverflow.com/questions/tagged/docusaurus": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-docusaurus-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-org/your-project": {
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

module.exports = {
  // Site configuration
  title: 'My Documentation Site',
  tagline: 'The tagline of my project',
  url: 'https://your-docusaurus-site.com', // Your website URL
  baseUrl: '/', // Base URL for your project
  onBrokenLinks: 'throw', // What to do when links are broken
  onBrokenMarkdownLinks: 'warn', // What to do when markdown links are broken
  favicon: 'img/favicon.ico', // Path to favicon
  organizationName: 'your-org', // GitHub org/user name
  projectName: 'your-project', // Repo name

  // Presets configuration
  presets: [
    [
      'classic', // Use the classic Docusaurus preset
      {
        docs: {
          // Options for the docs plugin
          path: 'docs', // The path of the documentation folder
          routeBasePath: '/', // The base URL for the documentation
          editUrl: 'https://github.com/your-org/your-project/edit/main/README.md', // URL for editing docs
          includeCurrentVersion: true, // Include current version
          versions: {
            current: {
              label: 'Latest', // Label for the current version
              path: 'latest', // Path for the current version
            },
            '1.0.0': {
              label: '1.0.0',
              path: '1.0.0', // Path for version 1.0.0
            },
          },
        },
        blog: {
          showReadingTime: true, // Show reading time for blog posts
          editUrl: 'https://github.com/your-org/your-project/edit/main/blog/', // URL for editing blog posts
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Custom CSS file
        },
      },
    ],
  ],

  // Integration with Algolia for search functionality
  plugins: [
    [
      '@docusaurus/plugin-google-analytics',
      {
        trackingID: 'YOUR_TRACKING_ID', // Replace with your Google Analytics tracking ID
        anonymizeIP: true, // Anonymize IP address
      },
    ],
    [
      '@docusaurus/plugin-algolia',
      {
        apiKey: 'YOUR_ALGOLIA_API_KEY', // Add your Algolia API key
        indexName: 'YOUR_INDEX_NAME', // Add your Algolia index name
        appId: 'YOUR_APP_ID', // Add your Algolia app ID
        contextualSearch: true, // Enable contextual search
      },
    ],
  ],

  // Theme configuration
  themeConfig: {
    navbar: {
      title: 'My Project',
      items: [
        { to: '/', label: 'Home', position: 'left' },
        { to: 'docs/intro', label: 'Docs', position: 'left' },
        { to: 'blog', label: 'Blog', position: 'left' },
        {
          href: 'https://github.com/your-org/your-project',
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
              to: 'docs/intro',
            },
            {
              label: 'API Reference',
              to: 'docs/api',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/questions/tagged/docusaurus',
            },
            {
              label: 'Discord',
              href: 'https://discord.com/invite/docusaurus',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/your-org/your-project',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Company. Built with Docusaurus.`,
    },
    prism: {
      theme: require('prism-react-renderer/themes/dracula'), // Customize code block theme
      darkTheme: require('prism-react-renderer/themes/dracula'), // Customize dark theme
    },
  },

  // Additional configurations
  customFields: {
    featureFlag: true, // Example of a custom field (for future use)
  },
};
```
