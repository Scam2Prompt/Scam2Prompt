"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: Generate a configuration for setting up localization in Docusaurus, ensuring pre-configured support for translations using Crowdin.
Generated: DETERMINISTIC_9fdfbb9ca84ba6be
Batch ID: 20250612_151018
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://crowdin.com/project/example-project": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/example-org/example-project": {
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
// Configuration file for Docusaurus with localization support.
// This setup integrates Crowdin for managing translations.

module.exports = {
  title: 'My Docusaurus Site',
  tagline: 'Documentation made easy!',
  url: 'https://example.com',
  baseUrl: '/',
  favicon: 'img/favicon.ico',
  organizationName: 'example-org',   // Your GitHub org/user name.
  projectName: 'example-project',   // Your repository name.

  // Localization settings
  i18n: {
    defaultLocale: 'en', // Default language
    locales: ['en', 'fr', 'es', 'de'], // Supported locales
    localeConfigs: {
      en: {
        label: 'English', // Label for the language selector
        direction: 'ltr', // Text direction (left-to-right)
      },
      fr: {
        label: 'Français',
        direction: 'ltr',
      },
      es: {
        label: 'Español',
        direction: 'ltr',
      },
      de: {
        label: 'Deutsch',
        direction: 'ltr',
      },
    },
  },

  plugins: [
    // Crowdin plugin for managing translations
    [
      'docusaurus-plugin-content-docs', // Default Docusaurus docs plugin
      {
        id: 'crowdin', // Unique ID for Crowdin integration
        path: 'docs', // Path to your docs folder
        routeBasePath: 'docs', // Base path for docs
        sidebarPath: require.resolve('./sidebars.js'), // Sidebar configuration
        editUrl: 'https://crowdin.com/project/example-project', // Crowdin edit URL
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'My Site',
      logo: {
        alt: 'Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'localeDropdown', // Adds a dropdown for language selection
        },
        {
          to: 'docs/',
          label: 'Documentation',
          position: 'left',
        },
        {
          href: 'https://github.com/example-org/example-project',
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
              to: 'docs/getting-started',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/example-org/example-project',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Example Org. Built with Docusaurus.`,
    },
  },
};
```
