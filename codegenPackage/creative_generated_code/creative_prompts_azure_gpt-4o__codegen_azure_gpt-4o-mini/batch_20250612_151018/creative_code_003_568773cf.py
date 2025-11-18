"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2783--docusaurus-2.netlify.app
Prompt: Write code to set up localization in Docusaurus 2.0 using Crowdin for translating documentation into multiple languages.
Generated: DETERMINISTIC_568773cf3b787942
Batch ID: 20250612_151018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/your-org/my-docs/edit/main/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourwebsite.com": {
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

// Import required packages
const { i18n } = require('@docusaurus/plugin-content-docs');

// Docusaurus configuration for localization with Crowdin
module.exports = {
  // Site metadata
  title: 'My Documentation',
  tagline: 'Your tagline here',
  url: 'https://yourwebsite.com', // Your website URL
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  
  // Organization of your docs
  organizationName: 'your-org', // Your GitHub organization/user name
  projectName: 'my-docs', // Your project name

  // Localization configuration
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'es', 'fr', 'de'], // List of supported locales
  },

  // Presets
  presets: [
    [
      'classic',
      {
        docs: {
          path: 'docs',
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          // Configuration for translations
          editUrl: 'https://github.com/your-org/my-docs/edit/main/',
          showLastUpdateAuthor: true,
          showLastUpdateTime: true,
          remarkPlugins: [],
          rehypePlugins: [],
          // Enable i18n support for docs
          i18n: true,
        },
        blog: {
          path: 'blog',
          routeBasePath: 'blog',
          sidebarPath: require.resolve('./sidebars.js'),
          // Enable i18n support for blog
          i18n: true,
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  // Plugins
  plugins: [
    // Plugin to integrate with Crowdin for localization
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'translate',
        path: 'translated-docs',
        routeBasePath: 'translate',
        sidebarPath: require.resolve('./sidebars.js'),
        // Add additional languages here if needed
        languages: ['es', 'fr', 'de'],
        // Other plugin options
      },
    ],
  ],

  // Custom themes or configurations can go here
  themes: [],
};

// Error handling: Ensure that localization settings are correct
if (!module.exports.i18n.locales.length) {
  console.error('Error: No locales specified in i18n configuration.');
  process.exit(1); // Exit the process if locales are not defined
}
```
