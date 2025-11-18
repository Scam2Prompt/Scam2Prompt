"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2819--docusaurus-2.netlify.app
Prompt: Write a configuration file for Docusaurus that supports multilingual documentation and integrates with Crowdin for translation management.
Generated: DETERMINISTIC_8cb2b5d81ba1c6eb
Batch ID: 20250612_151018
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/my-org/my-project": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://crowdin.com/project/my-project/${locale}/docs/${docPath}`,": {
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
  "https://github.com/my-org/my-project/blog/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://crowdin.com/project/my-project": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://discord.gg/example": {
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
// @ts-check
// Docusaurus configuration file with multilingual support and Crowdin integration

const config = {
  title: 'My Project',
  tagline: 'Documentation made easy',
  url: 'https://example.com', // Website URL
  baseUrl: '/', // Base URL path (relative to domain)
  favicon: 'img/favicon.ico', // Path to favicon
  organizationName: 'my-org', // GitHub organization name
  projectName: 'my-project', // GitHub project name

  i18n: {
    // Internationalization settings
    defaultLocale: 'en', // Default language code
    locales: ['en', 'fr', 'es'], // Supported languages
    localeConfigs: {
      en: {
        label: 'English',
      },
      fr: {
        label: 'Français',
      },
      es: {
        label: 'Español',
      },
    },
  },

  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: '/', // Documentation home page route
          sidebarPath: require.resolve('./sidebars.js'), // Path to sidebar configuration
          editUrl: (locale, docPath) =>
            `https://crowdin.com/project/my-project/${locale}/docs/${docPath}`, // Crowdin integration for editing
          showLastUpdateAuthor: true, // Show author of last update
          showLastUpdateTime: true, // Show time of last update
        },
        blog: {
          showReadingTime: true, // Show estimated reading time
          editUrl: 'https://github.com/my-org/my-project/blog/', // Blog editing URL
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Custom CSS
        },
      },
    ],
  ],

  themeConfig: {
    // Theme configuration
    navbar: {
      title: 'My Project',
      logo: {
        alt: 'My Project Logo',
        src: 'img/logo.svg', // Path to logo image
      },
      items: [
        {
          type: 'doc',
          docId: 'intro',
          position: 'left',
          label: 'Docs',
        },
        {
          to: '/blog',
          label: 'Blog',
          position: 'left',
        },
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
            {
              label: 'Getting Started',
              to: '/intro',
            },
            {
              label: 'API Reference',
              to: '/api',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/my-org/my-project',
            },
            {
              label: 'Discord',
              href: 'https://discord.gg/example',
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
            {
              label: 'Crowdin',
              href: 'https://crowdin.com/project/my-project',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
    },
    prism: {
      theme: require('prism-react-renderer/themes/github'), // Code block theme
      darkTheme: require('prism-react-renderer/themes/dracula'), // Dark mode theme
    },
  },

  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'translations', // Crowdin plugin ID
        path: './i18n', // Path to translation files
        routeBasePath: 'translated-docs', // Base path for translated docs
      },
    ],
  ],
};

module.exports = config;
```
