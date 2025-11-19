"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2758--docusaurus-2.netlify.app
Prompt: Explain how to configure localization in Docusaurus to translate documentation into multiple languages using Crowdin.
Generated: DETERMINISTIC_a33bfa4ee7eebea8
Batch ID: 20250612_163408
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/my-org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://my-website.com": {
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
  "https://crowdin.com/project/my-project": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/my-org/my-docs/edit/main/": {
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
  title: 'My Documentation',
  tagline: 'Documentation for my project',
  url: 'https://my-website.com',
  baseUrl: '/',
  favicon: 'img/favicon.ico',
  organizationName: 'my-org', // Your GitHub org/user name
  projectName: 'my-docs', // Your repo name
  i18n: {
    defaultLocale: 'en', // Default locale
    locales: ['en', 'fr', 'es'], // List of locales supported
  },
  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: '/', // Serve the docs at the site's root
          editUrl: 'https://github.com/my-org/my-docs/edit/main/',
          path: 'docs', // Path to the documentation files
          sidebarPath: require.resolve('./sidebars.js'),
          // Add localization support
          remarkPlugins: [require('remark-linguas')],
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/my-org/my-docs/edit/main/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
  // Crowdin integration configuration
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'crowdin',
        path: path.resolve(__dirname, 'crowdin-translations'), // Path for Crowdin translations
        routeBasePath: 'translations', // Base path for translations
        sidebarPath: require.resolve('./sidebars.js'),
        // Enable separate localization for Crowdin
        editUrl: 'https://crowdin.com/project/my-project',
      },
    ],
  ],
  themeConfig: {
    navbar: {
      title: 'My Docs',
      items: [
        {to: '/', label: 'Home', position: 'left'},
        {to: '/docs', label: 'Docs', position: 'left'},
        {
          to: 'translations',
          label: 'Translations',
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
              to: '/docs/getting-started',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/my-org',
            },
          ],
        },
      ],
    },
  },
};

```

```bash
# .crowdin.yml
project_id: your_crowdin_project_id
api_token: your_crowdin_api_token

# Specify the localization source files path
files:
  - source: /docs/**/*.md
    translation: /crowdin-translations/{locale}/{filename}
    type: markdown
    export: true

# List the supported languages
languages:
  - code: en
    name: English
  - code: fr
    name: French
  - code: es
    name: Spanish
```

```bash
# Instructions to integrate with Crowdin
# 1. Create a Crowdin project and set up your languages.
# 2. Add your Crowdin API token to the .crowdin.yml file.
# 3. Configure your source files in the .crowdin.yml to point to your docs folder.
# 4. Sync the files to Crowdin using the Crowdin CLI:
#    crowdin upload
# 5. After translations are done, pull the translations to your local environment:
#    crowdin download
```
