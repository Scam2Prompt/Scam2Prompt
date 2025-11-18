"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2803--docusaurus-2.netlify.app
Prompt: Write a script using Docusaurus to generate a static website with Markdown-based documentation and embedded JSX components.
Generated: DETERMINISTIC_537107771959db55
Batch ID: 20250612_151018
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://twitter.com/docusaurus": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourwebsite.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackoverflow.com/questions/tagged/docusaurus": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/facebook/docusaurus": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/classic/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://discordapp.com/invite/docusaurus": {
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
// Install necessary packages
// npm install --save docusaurus@latest

// Create a new Docusaurus project
// npx create-docusaurus@latest my-website classic

// Navigate into the project directory
// cd my-website

// Update the following files:

// 1. docusaurus.config.js
const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

module.exports = {
  title: 'My Documentation',
  tagline: 'Dinosaurs are cool',
  url: 'https://yourwebsite.com', // Your website URL
  baseUrl: '/my-website/', // Base URL for your project
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'your-org', // Your GitHub org/user name
  projectName: 'my-website', // Your repo name
  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: '/', // Serve the docs at the site's root
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/classic/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/classic/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
  themeConfig: {
    navbar: {
      title: 'My Docs',
      items: [
        {
          type: 'doc',
          docId: 'intro',
          position: 'left',
          label: 'Docs',
        },
        { to: '/blog', label: 'Blog', position: 'left' },
        {
          href: 'https://github.com/facebook/docusaurus',
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
              to: '/docs/intro',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/questions/tagged/docusaurus',
            },
            {
              label: 'Discord',
              href: 'https://discordapp.com/invite/docusaurus',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/docusaurus',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Company, Inc. Built with Docusaurus.`,
    },
    prism: {
      theme: lightCodeTheme,
      darkTheme: darkCodeTheme,
    },
  },
};

// 2. Create a Markdown file (intro.md) in the docs folder
/**
 * @file intro.md
 * @description Introduction to the documentation.
 */

# Introduction

Welcome to the documentation for My Project! This guide will help you understand how to use our software.

### Table of Contents

- [Getting Started](getting-started)
- [API Reference](api-reference)

<!-- JSX Component Example -->
<MyComponent />

// 3. Create a JSX Component (MyComponent.js) in the src/components folder
import React from 'react';

/**
 * MyComponent - A simple JSX component.
 * @returns {JSX.Element} The rendered component.
 */
const MyComponent = () => {
  return (
    <div>
      <h2>This is my custom component!</h2>
      <p>It can include any React logic or styles.</p>
    </div>
  );
};

export default MyComponent;

// 4. Include the JSX component in your Markdown file (intro.md)
import MyComponent from '@site/src/components/MyComponent';

<MyComponent />

// 5. Build and serve your Docusaurus site
// npm run build
// npm run serve
```
Make sure to replace placeholders like `yourwebsite.com`, `your-org`, and `my-website` with your actual information before running the code.
