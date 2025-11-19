"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2785--docusaurus-2.netlify.app
Prompt: How can I build optimized websites using Docusaurus and Markdown for my project documentation?
Generated: DETERMINISTIC_eaf3cfa7c20e5899
Batch ID: 20250612_163408
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://yourwebsite.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://twitter.com/youraccount": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/YourOrg/YourProject/edit/main/docs/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/YourOrg/YourProject/edit/main/blog/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/YourOrg/YourProject": {
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
// Import necessary modules for configuring Docusaurus
const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** 
 * @type {import('@docusaurus/types').Config} 
 * Docusaurus configuration object to build optimized websites
 */
const config = {
  title: 'Project Documentation',
  tagline: 'Optimized, fast, and Markdown-powered documentation',
  url: 'https://yourwebsite.com', // Your website's base URL
  baseUrl: '/', // Base URL for your documentation
  favicon: 'img/favicon.ico', // Path to favicon
  organizationName: 'YourOrg', // GitHub org/user name
  projectName: 'YourProject', // Repository name

  // Presets configuration for Docusaurus
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'), // Path to sidebar configuration
          editUrl:
            'https://github.com/YourOrg/YourProject/edit/main/docs/', // Edit URL for GitHub
        },
        blog: {
          showReadingTime: true, // Display estimated reading time for posts
          editUrl:
            'https://github.com/YourOrg/YourProject/edit/main/blog/', // Blog edit URL
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Path to custom CSS
        },
      }),
    ],
  ],

  // Theme configuration for light/dark modes
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Project Documentation',
        logo: {
          alt: 'Logo',
          src: 'img/logo.svg', // Path to your logo image
        },
        items: [
          { to: '/docs/intro', label: 'Docs', position: 'left' },
          { to: '/blog', label: 'Blog', position: 'left' },
          {
            href: 'https://github.com/YourOrg/YourProject',
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
                href: 'https://github.com/YourOrg/YourProject',
              },
              {
                label: 'Twitter',
                href: 'https://twitter.com/youraccount',
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
        copyright: `Copyright © ${new Date().getFullYear()} YourOrg. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

// Export the configuration object
module.exports = config;
```

This code defines the configuration file (`docusaurus.config.js`) for setting up an optimized documentation website using Docusaurus and Markdown. Save this file in the root directory of your Docusaurus project.
