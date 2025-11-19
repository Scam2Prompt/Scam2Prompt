"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: What are the steps to implement document versioning in Docusaurus for maintaining documentation across multiple project releases?
Generated: DETERMINISTIC_cfc98155385f3c21
Batch ID: 20250612_163408
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://mywebsite.com": {
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
  "https://github.com/my-org/my-project/edit/main/blog/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/my-org/my-project/edit/main/docs/": {
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
// Docusaurus configuration for document versioning
// Ensure you have Docusaurus installed and properly set up.
// This code configures versioning for your documentation site.

// Import required modules
const config = {
  // Site metadata
  title: 'My Project Documentation',
  tagline: 'Documentation for multiple versions of My Project',
  url: 'https://mywebsite.com',
  baseUrl: '/',
  favicon: 'img/favicon.ico',
  organizationName: 'my-org', // Your GitHub org/user name.
  projectName: 'my-project', // Your repo name.

  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // Enable versioning
          versions: {
            current: {
              label: 'Next', // Label for the current version
            },
          },
          sidebarPath: require.resolve('./sidebars.js'), // Path to docs sidebar configuration
          editUrl: 'https://github.com/my-org/my-project/edit/main/docs/', // Edit link for documentation files
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/my-org/my-project/edit/main/blog/',
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
        src: 'img/logo.svg',
      },
      items: [
        {
          to: 'docs/', // Default documentation link
          activeBasePath: 'docs',
          label: 'Documentation',
          position: 'left',
        },
        {
          to: 'docs/versioned_docs/', // Versioned documentation links
          label: 'Versions',
          position: 'left',
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
              to: 'docs/',
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
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Organization.`,
    },
  },
};

// Export the configuration object
module.exports = config;

// Steps to manage versions:
// 1. Run `yarn docusaurus docs:version <version>` to create a versioned copy of current docs.
//    For example: `yarn docusaurus docs:version 1.0.0`
// 2. Manage versioned docs in the `versioned_docs` folder.
// 3. Ensure the `versions.json` file reflects the updated version history.
```
