"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2785--docusaurus-2.netlify.app
Prompt: Generate a configuration file for Docusaurus to enable localization using Crowdin for translating documentation into multiple languages.
Generated: DETERMINISTIC_f787667ed15558f3
Batch ID: 20250612_151018
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://twitter.com/myproject": {
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
  "https://crowdin.com/project/myproject": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/myproject": {
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

// Import necessary modules
const path = require('path');

/** 
 * Docusaurus Configuration File
 * This configuration enables localization using Crowdin for translating documentation
 * into multiple languages.
 * @type {import('@docusaurus/types').Config}
 */
const config = {
  title: 'My Project', // Title of your project
  tagline: 'Documentation translated into multiple languages',
  url: 'https://example.com', // Your website URL
  baseUrl: '/', // Base URL for the site
  onBrokenLinks: 'throw', // Error handling for broken links
  onBrokenMarkdownLinks: 'warn', // Warn about broken markdown links
  favicon: 'img/favicon.ico', // Path to your site's favicon

  // Internationalization configuration
  i18n: {
    defaultLocale: 'en', // Default language
    locales: ['en', 'es', 'fr', 'de'], // Supported languages
    localeConfigs: {
      en: {
        label: 'English', // Label for English
        direction: 'ltr', // Text direction (Left-to-right)
      },
      es: {
        label: 'Español', // Label for Spanish
        direction: 'ltr',
      },
      fr: {
        label: 'Français', // Label for French
        direction: 'ltr',
      },
      de: {
        label: 'Deutsch', // Label for German
        direction: 'ltr',
      },
    },
  },

  // Crowdin integration for translations
  presets: [
    [
      'classic', // Using the classic preset
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'), // Path to the sidebar configuration
          editUrl:
            'https://crowdin.com/project/myproject', // Crowdin-powered edit URL
        },
        blog: {
          showReadingTime: true, // Show reading time for blog posts
          editUrl:
            'https://crowdin.com/project/myproject', // Crowdin edit URL for blog posts
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Path to custom CSS
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'My Project',
      logo: {
        alt: 'My Project Logo',
        src: 'img/logo.svg', // Path to the site's logo
      },
      items: [
        { to: '/docs/intro', label: 'Docs', position: 'left' },
        { to: '/blog', label: 'Blog', position: 'left' },
        {
          type: 'localeDropdown', // Dropdown menu for selecting language
          position: 'right',
        },
        {
          href: 'https://github.com/myproject', // External link to GitHub
          label: 'GitHub',
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
            {
              label: 'Getting Started',
              to: '/docs/intro',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/myproject',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/myproject',
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
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Project.`,
    },
  },

  // Plugin for Crowdin integration
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        path: 'docs',
        routeBasePath: 'docs',
        editUrl: 'https://crowdin.com/project/myproject', // Edit URL for Crowdin
      },
    ],
    [
      '@docusaurus/plugin-sitemap', // Sitemap generation plugin
      {
        cacheTime: 600000, // Cache time for sitemap in milliseconds
        changefreq: 'weekly',
        priority: 0.5,
      },
    ],
  ],
};

module.exports = config;
```
