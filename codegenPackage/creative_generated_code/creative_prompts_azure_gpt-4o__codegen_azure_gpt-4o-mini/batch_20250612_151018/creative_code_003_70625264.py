"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2728--docusaurus-2.netlify.app
Prompt: Write a Docusaurus configuration file to enable Crowdin-based localization for translating documentation into multiple languages.
Generated: DETERMINISTIC_70625264843ddac0
Batch ID: 20250612_151018
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/your-repo/edit/main/docs/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://discord.gg/your-invite": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-repo/edit/main/blog/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-repo": {
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

const path = require('path');

module.exports = {
  // Basic site details
  title: 'My Documentation', // Your documentation title
  tagline: 'Documentation made easy',
  url: 'https://yourwebsite.com', // Your website URL
  baseUrl: '/', // Base URL for your project
  onBrokenLinks: 'throw', // Configures behavior for broken links
  onBrokenMarkdownLinks: 'warn', // Configures behavior for broken Markdown links

  // Localization configuration
  i18n: {
    defaultLocale: 'en', // Default locale
    locales: ['en', 'fr', 'es', 'de', 'zh'], // Supported locales
  },

  // Crowdin configuration for localization
  plugins: [
    [
      '@docusaurus/plugin-i18n',
      {
        // Configuration for Crowdin integration
        crowdin: {
          projectId: 'YOUR_CROWDIN_PROJECT_ID', // Replace with your Crowdin project ID
          apiKey: 'YOUR_CROWDIN_API_KEY', // Replace with your Crowdin API key
          locales: ['en', 'fr', 'es', 'de', 'zh'], // Supported locales
          // Optional: Set the path where translations will be stored
          outputPath: path.join(__dirname, 'i18n'), // Output path for translated files
        },
      },
    ],
  ],

  // Configuration for themes and presets
  presets: [
    [
      'classic', // Using the classic preset
      {
        docs: {
          path: 'docs', // Path to your documentation source
          routeBasePath: '/', // Base path for documentation pages
          editUrl: 'https://github.com/your-repo/edit/main/docs/', // Edit URL for documentation
        },
        blog: {
          path: 'blog', // Path to your blog source
          routeBasePath: 'blog', // Base path for blog pages
          editUrl: 'https://github.com/your-repo/edit/main/blog/', // Edit URL for blog
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Path to custom CSS
        },
      },
    ],
  ],

  // Additional configuration options
  themeConfig: {
    navbar: {
      title: 'My Documentation',
      items: [
        { to: '/', label: 'Home', position: 'left' },
        { to: 'docs', label: 'Docs', position: 'left' },
        { to: 'blog', label: 'Blog', position: 'left' },
        {
          type: 'localeDropdown', // Dropdown for language selection
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark', // Footer style
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
            { label: 'GitHub', href: 'https://github.com/your-repo' },
            { label: 'Discord', href: 'https://discord.gg/your-invite' },
          ],
        },
      ],
    },
  },

  // Error handling for missing configurations
  validateConfig: function () {
    if (!process.env.CROWDIN_API_KEY || !process.env.CROWDIN_PROJECT_ID) {
      throw new Error("Crowdin API Key and Project ID must be provided in environment variables.");
    }
  },
};

// Run validation on configuration
module.exports.validateConfig();
```
