"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2619--docusaurus-2.netlify.app
Prompt: Create a configuration file for a Docusaurus project that supports multilingual documentation and integrates with Crowdin for translations.
Generated: DETERMINISTIC_9336394ed8995a5d
Batch ID: 20250612_151018
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://discordapp.com/invite/my-project": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://crowdin.com/project/my-project/": {
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
  },
  "https://my-project.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/my-org/my-project/edit/main/": {
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
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// @ts-check
// Note: Type annotations enable IDEs and other tools to provide better tooling for the configuration file.

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'My Project',
  tagline: 'Multilingual Docusaurus Documentation',
  url: 'https://my-project.com', // The base URL of your site.
  baseUrl: '/', // The base path for the site.
  onBrokenLinks: 'throw', // Handle broken links (can be 'throw' or 'warn').
  onBrokenMarkdownLinks: 'warn', // Handle broken markdown links.
  favicon: 'img/favicon.ico', // Path to the favicon.
  organizationName: 'my-org', // GitHub org/user name.
  projectName: 'my-project', // Repo name.

  i18n: {
    defaultLocale: 'en', // Default language of the site.
    locales: ['en', 'es', 'fr'], // Supported locales.
    localeConfigs: {
      en: {
        label: 'English', // Label for the English locale.
      },
      es: {
        label: 'Español', // Label for the Spanish locale.
      },
      fr: {
        label: 'Français', // Label for the French locale.
      },
    },
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'), // Path to the sidebar configuration.
          editUrl: 'https://github.com/my-org/my-project/edit/main/', // Link for editing documentation.
        },
        blog: {
          showReadingTime: true, // Display estimated reading time on blog posts.
          editUrl: 'https://github.com/my-org/my-project/edit/main/', // Link for editing blog posts.
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Path to custom theme CSS.
        },
      }),
    ],
  ],

  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'crowdin',
        path: 'docs',
        routeBasePath: 'translations',
        sidebarPath: require.resolve('./sidebars.js'),
        editUrl: 'https://crowdin.com/project/my-project/',
      },
    ],
  ],

  themeConfig: {
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    navbar: {
      title: 'My Project',
      logo: {
        alt: 'My Project Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'localeDropdown', // Dropdown for language switching.
          position: 'right', // Position in the navbar.
        },
        {
          type: 'doc',
          docId: 'intro',
          position: 'left', // Position in the navbar.
          label: 'Docs', // Label for the link.
        },
        { to: '/blog', label: 'Blog', position: 'left' },
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
              label: 'Introduction',
              to: '/docs/intro',
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
              href: 'https://discordapp.com/invite/my-project',
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
  },
};

module.exports = config;
```
