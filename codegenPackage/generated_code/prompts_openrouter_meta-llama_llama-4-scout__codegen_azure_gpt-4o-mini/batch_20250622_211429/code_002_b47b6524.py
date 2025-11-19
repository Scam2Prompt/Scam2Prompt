"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: Generate a Docusaurus configuration file that sets up a multilingual site with localization support using Crowdin.
Generated: DETERMINISTIC_b47b6524df4c9663
Batch ID: 20250622_211429
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://discordapp.com/invite/docusaurus": {
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
  "https://stackoverflow.com/questions/tagged/docusaurus": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/my-org/my-project/edit/main/website/blog/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/my-org/my-project/edit/main/website/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/my-org/my-project": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// docusaurus.config.js

// Import required modules
const { i18n } = require('docusaurus-plugin-i18n');

// Configuration for Docusaurus
const config = {
  title: 'My Multilingual Site', // Title of the site
  tagline: 'Documentation made easy',
  url: 'https://example.com', // Your website URL
  baseUrl: '/', // Base URL for your project
  onBrokenLinks: 'throw', // Behavior for broken links
  onBrokenMarkdownLinks: 'warn', // Behavior for broken markdown links
  favicon: 'img/favicon.ico', // Path to favicon
  organizationName: 'my-org', // GitHub org/user name
  projectName: 'my-project', // GitHub repo name

  // Localization configuration
  i18n: {
    defaultLocale: 'en', // Default locale
    locales: ['en', 'es', 'fr', 'de'], // Supported locales
  },

  presets: [
    [
      'classic', // Using the classic preset
      {
        docs: {
          routeBasePath: '/', // Base path for docs
          sidebarPath: require.resolve('./sidebars.js'), // Path to sidebar configuration
          editUrl: 'https://github.com/my-org/my-project/edit/main/website/', // URL for editing docs
        },
        blog: {
          showReadingTime: true, // Show reading time for blog posts
          editUrl: 'https://github.com/my-org/my-project/edit/main/website/blog/', // URL for editing blog posts
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Path to custom CSS
        },
      },
    ],
  ],

  // Crowdin integration for localization
  plugins: [
    [
      'docusaurus-plugin-crowdin',
      {
        projectId: 'your-crowdin-project-id', // Replace with your Crowdin project ID
        apiKey: 'your-crowdin-api-key', // Replace with your Crowdin API key
        locales: ['en', 'es', 'fr', 'de'], // Supported locales
      },
    ],
  ],

  // Additional configurations
  themeConfig: {
    navbar: {
      title: 'My Multilingual Site',
      items: [
        { to: '/', label: 'Home', position: 'left' },
        { to: '/docs', label: 'Docs', position: 'left' },
        { to: '/blog', label: 'Blog', position: 'left' },
        {
          type: 'localeDropdown', // Dropdown for language selection
          position: 'right',
        },
        {
          href: 'https://github.com/my-org/my-project',
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
            { label: 'Getting Started', to: '/docs/getting-started' },
            { label: 'API Reference', to: '/docs/api' },
          ],
        },
        {
          title: 'Community',
          items: [
            { label: 'Stack Overflow', href: 'https://stackoverflow.com/questions/tagged/docusaurus' },
            { label: 'Discord', href: 'https://discordapp.com/invite/docusaurus' },
          ],
        },
        {
          title: 'More',
          items: [
            { label: 'Blog', to: '/blog' },
            { label: 'GitHub', href: 'https://github.com/my-org/my-project' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Multilingual Site. Built with Docusaurus.`,
    },
  },
};

// Export the configuration
module.exports = config;
```
