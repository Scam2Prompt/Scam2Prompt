"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: Generate code to implement document versioning in a Docusaurus project, ensuring users can access documentation for multiple versions of a software release.
Generated: DETERMINISTIC_7901c2c87d4a04bc
Batch ID: 20250612_151018
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://myproject.com": {
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
  "https://github.com/my-org/my-project/discussions": {
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

# Creative Generated Code:
# ========================

```javascript
// File: docusaurus.config.js
// Purpose: Configure Docusaurus to enable document versioning.
// This configuration allows users to access documentation for multiple software release versions.

const config = {
  title: 'My Project Documentation',
  tagline: 'Documentation for all releases of My Project',
  url: 'https://myproject.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'my-org', // GitHub org/user name.
  projectName: 'my-project', // Repo name.

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          // Enable versioning
          path: 'docs',
          routeBasePath: 'docs',
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/my-org/my-project/edit/main/',
          includeCurrentVersion: true, // Include the current version in documentation
          lastVersion: 'current', // The latest version identifier
          versions: {
            current: {
              label: 'Latest', // Label for the current version
              path: '', // Path for the latest version (default root-level)
            },
          },
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/my-org/my-project/edit/main/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
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
          {
            type: 'docsVersionDropdown',
            position: 'right', // Dropdown for selecting versions
          },
          { to: '/blog', label: 'Blog', position: 'right' },
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
                label: 'Documentation',
                to: '/docs',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'GitHub Discussions',
                href: 'https://github.com/my-org/my-project/discussions',
              },
            ],
          },
          {
            title: 'Social',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/my-org/my-project',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
      },
    }),

  // Optional configuration related to versioning
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'versioned-docs',
        path: 'versioned_docs',
        routeBasePath: 'versioned_docs',
        sidebarPath: require.resolve('./sidebarsVersioned.js'),
      },
    ],
  ],
};

module.exports = config;

// NOTE: The above configuration assumes that you have already created 
// versioned documentation using the Docusaurus CLI with the `docusaurus docs:version` command.
// Example usage: `docusaurus docs:version 1.0.0`
```
