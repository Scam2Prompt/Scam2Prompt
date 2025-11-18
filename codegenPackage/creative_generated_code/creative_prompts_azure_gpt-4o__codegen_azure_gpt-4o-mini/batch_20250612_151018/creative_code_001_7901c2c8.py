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
  "https://github.com/myorg/myproject": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://myproject.github.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://discord.gg/myorg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/myorg/myproject/edit/main/website/": {
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

/**
 * @type {import('@docusaurus/types').DocusaurusConfig}
 */
const config = {
  title: 'My Project Documentation',
  url: 'https://myproject.github.io',
  baseUrl: '/',
  organizationName: 'myorg', // Your GitHub org/user name
  projectName: 'myproject', // Your repo name
  trailingSlash: false,
  presets: [
    [
      'classic',
      {
        docs: {
          path: 'docs',
          routeBasePath: '/', // Serve docs at the base URL
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/myorg/myproject/edit/main/website/',
          versions: {
            current: {
              label: 'Latest',
              path: 'latest',
              banner: 'none',
            },
            '1.0.0': {
              label: 'v1.0.0',
              path: '1.0.0',
              banner: 'none',
            },
            '2.0.0': {
              label: 'v2.0.0',
              path: '2.0.0',
              banner: 'none',
            },
          },
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/myorg/myproject/edit/main/website/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
  themeConfig: {
    navbar: {
      title: 'My Project',
      items: [
        {to: '/', label: 'Docs', position: 'left'},
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          type: 'docVersionDropdown',
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
            {
              label: 'API Reference',
              to: '/docs/api-reference',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/myorg/myproject',
            },
            {
              label: 'Discord',
              href: 'https://discord.gg/myorg',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Project`,
    },
  },
};

module.exports = config;
```

```json
// package.json

{
  "name": "myproject",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "start": "docusaurus start",
    "build": "docusaurus build",
    "deploy": "docusaurus deploy",
    "serve": "docusaurus serve"
  },
  "dependencies": {
    "@docusaurus/core": "^2.0.0",
    "@docusaurus/preset-classic": "^2.0.0"
  },
  "devDependencies": {
    "docusaurus-asset": "^2.0.0"
  }
}
```

```javascript
// sidebars.js

/**
 * Creating a sidebar for the documentation.
 * 
 * This configuration determines how the documentation is organized and displayed
 * on the site. Each version's sidebar can be customized individually.
 */

module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
      items: ['getting-started/introduction'],
    },
    {
      type: 'category',
      label: 'API Reference',
      items: ['api-reference/api-usage', 'api-reference/api-advanced'],
    },
    {
      type: 'category',
      label: 'Version 1.0.0',
      items: [
        '1.0.0/overview',
        '1.0.0/usage',
        '1.0.0/faq',
      ],
    },
    {
      type: 'category',
      label: 'Version 2.0.0',
      items: [
        '2.0.0/overview',
        '2.0.0/new-features',
        '2.0.0/faq',
      ],
    },
  ],
};
```

```markdown
<!-- docs/getting-started/introduction.md -->

# Introduction

Welcome to the documentation for My Project. Here you will find everything you need to get started!

## Versioning

This documentation supports multiple versions of the software. Use the version dropdown in the navbar to navigate between versions.
```

```markdown
<!-- docs/1.0.0/overview.md -->

# Overview of Version 1.0.0

This section provides an overview of the features and functionalities available in version 1.0.0.

## Key Features

- Feature A
- Feature B
- Feature C
```

```markdown
<!-- docs/2.0.0/new-features.md -->

# New Features in Version 2.0.0

This section outlines the new features introduced in version 2.0.0.

## What's New

- Feature D
- Feature E
- Improved performance
```

This code structure sets up a Docusaurus project for document versioning, allowing users to switch between different versions of documentation seamlessly. Each version has its own set of documents organized in a clear manner, with essential configurations and scripts included for building and deploying the documentation.
