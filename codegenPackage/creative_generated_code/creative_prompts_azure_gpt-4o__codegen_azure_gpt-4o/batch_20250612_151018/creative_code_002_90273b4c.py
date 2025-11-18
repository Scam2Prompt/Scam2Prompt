"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: Create a Docusaurus configuration file to enable Algolia-powered content search for documentation.
Generated: DETERMINISTIC_90273b4cb23251ec
Batch ID: 20250612_151018
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/my-org/my-docs/edit/main/website/": {
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
  },
  "https://example.com": {
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
// Docusaurus configuration file with Algolia search enabled

module.exports = {
  title: 'My Documentation Site', // The title of your site
  tagline: 'Learn everything here!', // A brief tagline
  url: 'https://example.com', // Base site URL
  baseUrl: '/', // Base URL for the project
  onBrokenLinks: 'throw', // Throws an error if there are broken links
  onBrokenMarkdownLinks: 'warn', // Warns about broken markdown links
  favicon: 'img/favicon.ico', // Path to the favicon
  organizationName: 'my-org', // GitHub organization name
  projectName: 'my-docs', // Repository name

  // Theme configuration
  themeConfig: {
    // Algolia search configuration
    algolia: {
      appId: 'YOUR_ALGOLIA_APP_ID', // Replace with your Algolia App ID
      apiKey: 'YOUR_ALGOLIA_API_KEY', // Replace with your Algolia API Key
      indexName: 'YOUR_INDEX_NAME', // Replace with your Algolia Index Name
      contextualSearch: true, // Enables contextual search
      // Optional: Custom search parameters (e.g., to filter results)
      searchParameters: {
        facetFilters: ['version:v1'], // Example filter
      },
    },
    navbar: {
      title: 'Documentation', // Title in the navigation bar
      logo: {
        alt: 'Logo', // Alternative text for the logo
        src: 'img/logo.svg', // Path to the logo image
      },
      items: [
        {
          to: 'docs/', // Path to the documentation
          label: 'Docs', // Label for the navigation item
          position: 'left', // Position of the item in the navbar
        },
        {
          href: 'https://github.com/my-org/my-docs', // External link (e.g., GitHub repo)
          label: 'GitHub', // Label for the link
          position: 'right', // Position of the item in the navbar
        },
      ],
    },
    footer: {
      style: 'dark', // Footer style
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Getting Started',
              to: 'docs/getting-started', // Link to a specific doc
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/my-org/my-docs', // External link
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Organization. Built with Docusaurus.`,
    },
  },

  presets: [
    [
      '@docusaurus/preset-classic', // Classic preset
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'), // Path to the sidebar configuration
          editUrl: 'https://github.com/my-org/my-docs/edit/main/website/', // URL for the "edit this page" button
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Path to custom CSS
        },
      },
    ],
  ],

  // Optional: Plugins and custom configuration
  plugins: [
    // Add plugins if needed
  ],
};
```
