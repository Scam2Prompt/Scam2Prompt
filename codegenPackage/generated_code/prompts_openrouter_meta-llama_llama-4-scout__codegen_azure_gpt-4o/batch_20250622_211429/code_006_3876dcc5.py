"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2783--docusaurus-2.netlify.app
Prompt: Design a Docusaurus theme that integrates with Algolia documentation search and supports multiple languages.
Generated: DETERMINISTIC_3876dcc5e2bac6bc
Batch ID: 20250622_211429
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/example/documentation-site": {
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
  },
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/example/documentation-site/edit/main/blog/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/example/documentation-site/edit/main/": {
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
// Configuration file for Docusaurus with Algolia search and multi-language support.

module.exports = {
  title: 'My Documentation Site',
  tagline: 'Documentation made easy',
  url: 'https://example.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'example', // GitHub org/user name.
  projectName: 'documentation-site', // Repo name.

  i18n: {
    // Internationalization settings for multi-language support.
    defaultLocale: 'en',
    locales: ['en', 'fr', 'es'], // Supported languages.
    localeConfigs: {
      en: { label: 'English' },
      fr: { label: 'Français' },
      es: { label: 'Español' },
    },
  },

  themeConfig: {
    // Theme configuration for Docusaurus.
    navbar: {
      title: 'My Site',
      logo: {
        alt: 'Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        { to: 'docs/', label: 'Docs', position: 'left' },
        { to: 'blog', label: 'Blog', position: 'left' },
        {
          type: 'localeDropdown', // Dropdown for language selection.
          position: 'right',
        },
        {
          href: 'https://github.com/example/documentation-site',
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
            { label: 'Getting Started', to: 'docs/getting-started' },
            { label: 'API Reference', to: 'docs/api' },
          ],
        },
        {
          title: 'Community',
          items: [
            { label: 'GitHub', href: 'https://github.com/example/documentation-site' },
            { label: 'Discord', href: 'https://discord.gg/example' },
          ],
        },
        {
          title: 'More',
          items: [
            { label: 'Blog', to: 'blog' },
            { label: 'Privacy Policy', to: 'privacy-policy' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Documentation Site.`,
    },
    algolia: {
      // Algolia search configuration.
      appId: 'YOUR_ALGOLIA_APP_ID', // Replace with your Algolia App ID.
      apiKey: 'YOUR_ALGOLIA_API_KEY', // Replace with your Algolia API Key.
      indexName: 'YOUR_INDEX_NAME', // Replace with your Algolia index name.
      contextualSearch: true, // Enable contextual search.
      searchParameters: {}, // Additional search parameters.
    },
  },

  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/example/documentation-site/edit/main/',
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/example/documentation-site/edit/main/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
```

```css
/* src/css/custom.css */
/* Custom CSS for Docusaurus theme styling. */

:root {
  --ifm-color-primary: #0078d4; /* Primary color for the theme. */
  --ifm-color-secondary: #2e8555; /* Secondary color for the theme. */
}

body {
  font-family: 'Arial', sans-serif; /* Set a clean font for the site. */
}

.navbar__logo {
  max-height: 40px; /* Adjust logo size in the navbar. */
}

.footer {
  background-color: #282c34; /* Footer background color. */
  color: #ffffff; /* Footer text color. */
}
```

```javascript
// sidebars.js
// Sidebar configuration for Docusaurus documentation.

module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
      items: ['getting-started/introduction', 'getting-started/setup'],
    },
    {
      type: 'category',
      label: 'API Reference',
      items: ['api/authentication', 'api/endpoints'],
    },
  ],
};
```

```json
// package.json
// Ensure dependencies for Docusaurus and Algolia are installed.

{
  "name": "documentation-site",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "start": "docusaurus start",
    "build": "docusaurus build",
    "serve": "docusaurus serve",
    "deploy": "docusaurus deploy"
  },
  "dependencies": {
    "@docusaurus/core": "^3.0.0",
    "@docusaurus/preset-classic": "^3.0.0",
    "@docusaurus/theme-search-algolia": "^3.0.0"
  }
}
```

This code is ready to be used for a Docusaurus site with Algolia search and multi-language support. Replace placeholders like `YOUR_ALGOLIA_APP_ID`, `YOUR_ALGOLIA_API_KEY`, and `YOUR_INDEX_NAME` with your actual Algolia credentials.
