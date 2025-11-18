"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: Create a configuration file for a Docusaurus project that includes both documentation and blog sections.
Generated: DETERMINISTIC_61ddde855cb513e0
Batch ID: 20250612_151018
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://your-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-org/your-project-name": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-org/your-project-name/edit/main/blog/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-org/your-project-name/edit/main/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://twitter.com/your-profile": {
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
// Note: Type annotations provide better IDE support and ensure type safety

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

module.exports = {
  // Site metadata
  title: 'My Docusaurus Project',
  tagline: 'Documentation and Blog made easy',
  url: 'https://your-site.com',
  baseUrl: '/',
  favicon: 'img/favicon.ico',
  organizationName: 'your-org', // Usually your GitHub org/user name.
  projectName: 'your-project-name', // Usually your repo name.

  onBrokenLinks: 'throw', // Throw error on broken links
  onBrokenMarkdownLinks: 'warn', // Warn about broken markdown links

  i18n: {
    defaultLocale: 'en',
    locales: ['en'], // Add more locales if needed
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'), // Path to the sidebar configuration
          editUrl: 'https://github.com/your-org/your-project-name/edit/main/', // URL for doc edits
        },
        blog: {
          showReadingTime: true, // Display estimated reading time on blogs
          editUrl: 'https://github.com/your-org/your-project-name/edit/main/blog/', // URL for blog edits
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Custom CSS for further styling
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'My Project',
        logo: {
          alt: 'My Project Logo',
          src: 'img/logo.svg',
        },
        items: [
          { to: '/docs/intro', label: 'Docs', position: 'left' },
          { to: '/blog', label: 'Blog', position: 'left' },
          {
            href: 'https://github.com/your-org/your-project-name',
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
                href: 'https://github.com/your-org/your-project-name',
              },
              {
                label: 'Twitter',
                href: 'https://twitter.com/your-profile',
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
        copyright: `Copyright © ${new Date().getFullYear()} Your Organization. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme, // Syntax highlighting theme for light mode
        darkTheme: darkCodeTheme, // Syntax highlighting theme for dark mode
      },
    }),
};
```
