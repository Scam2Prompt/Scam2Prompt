"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2689--docusaurus-2.netlify.app
Prompt: Provide an example of how to use Docusaurus to build documentation for an open-source project, including setup steps and code snippets for customization.
Generated: DETERMINISTIC_e5dd5d78966d4eb7
Batch ID: 20250612_151018
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://myopensourceproject.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/GitHubOrgName/my-open-source-project/edit/main/website/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/GitHubOrgName/my-open-source-project": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://discord.gg/myproject": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/GitHubOrgName/my-open-source-project/issues": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
# Install Docusaurus CLI globally
npm install -g @docusaurus/init

# Create a new Docusaurus project
docusaurus-init

# Change into the new project directory
cd my-website

# Install dependencies
npm install
```

```json
// package.json
{
  "scripts": {
    "start": "docusaurus start",
    "build": "docusaurus build",
    "deploy": "docusaurus deploy"
  },
  "dependencies": {
    "@docusaurus/core": "^2.0.0-beta.20",
    "@docusaurus/preset-classic": "^2.0.0-beta.20"
  }
}
```

```javascript
// docusaurus.config.js
module.exports = {
  title: 'My Open Source Project',
  tagline: 'Documentation for My Open Source Project',
  url: 'https://myopensourceproject.com',
  baseUrl: '/',
  favicon: 'img/favicon.ico',
  organizationName: 'GitHubOrgName', // GitHub organization or user name
  projectName: 'my-open-source-project', // Repository name
  themeConfig: {
    navbar: {
      title: 'My Project',
      logo: {
        alt: 'My Project Logo',
        src: 'img/logo.png',
      },
      items: [
        { to: 'docs/', label: 'Docs', position: 'left' },
        { href: 'https://github.com/GitHubOrgName/my-open-source-project', label: 'GitHub', position: 'right' },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            { label: 'Getting Started', to: 'docs/getting-started' },
          ],
        },
        {
          title: 'Community',
          items: [
            { label: 'GitHub Issues', href: 'https://github.com/GitHubOrgName/my-open-source-project/issues' },
            { label: 'Discord', href: 'https://discord.gg/myproject' },
          ],
        },
        {
          title: 'More',
          items: [
            { label: 'GitHub', href: 'https://github.com/GitHubOrgName/my-open-source-project' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Open Source Project.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'), // Define sidebar structure
          editUrl: 'https://github.com/GitHubOrgName/my-open-source-project/edit/main/website/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Custom CSS
        },
      },
    ],
  ],
};
```

```javascript
// sidebars.js
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
      items: ['getting-started'],
    },
    {
      type: 'category',
      label: 'Features',
      items: ['feature-a', 'feature-b'],
    },
  ],
};
```

```markdown
// docs/getting-started.md
---
id: getting-started
title: Getting Started
---

# Getting Started

Welcome to the documentation for My Open Source Project!

## Installation

Run the following command to install:

```bash
npm install my-open-source-project
```

## Usage

Here's a basic example of how to use the library:

```javascript
const { doSomething } = require('my-open-source-project');
doSomething();
```
```

```css
/* src/css/custom.css */
:root {
  --ifm-color-primary: #4CAF50; /* Set primary color */
}
```

```bash
# Start the development server
npm run start

# Build the production site
npm run build

# Deploy the site (requires GitHub Pages or similar hosting setup)
npm run deploy
```
