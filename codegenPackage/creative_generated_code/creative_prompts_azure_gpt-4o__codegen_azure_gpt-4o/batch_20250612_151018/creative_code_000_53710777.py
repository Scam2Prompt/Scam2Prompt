"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2803--docusaurus-2.netlify.app
Prompt: Write a script using Docusaurus to generate a static website with Markdown-based documentation and embedded JSX components.
Generated: DETERMINISTIC_537107771959db55
Batch ID: 20250612_151018
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/my-org/my-static-site": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://my-static-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/my-org/my-static-site/edit/main/blog/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/my-org/my-static-site/edit/main/docs/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://twitter.com/myorg": {
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
# Install Docusaurus CLI globally if not already installed
npm install -g @docusaurus/init

# Create a new Docusaurus project
docusaurus init my-static-site
```

### Directory Layout after `docusaurus init`
```
my-static-site/
├── blog/
├── docs/
├── src/
├── static/
└── docusaurus.config.js
```

Below is the code for the Docusaurus configuration file (`docusaurus.config.js`).

```javascript
// docusaurus.config.js
module.exports = {
  title: 'My Static Docs Website', // Website title
  tagline: 'Markdown & JSX Documentation',
  url: 'https://my-static-site.com', // Your site URL
  baseUrl: '/', // Base URL for deployments
  favicon: 'img/favicon.ico', // Favicon for branding
  organizationName: 'my-org', // GitHub org/user for deployment
  projectName: 'my-static-site', // Repo name for deployment
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          routeBasePath: 'docs', // Path for documentation
          sidebarPath: require.resolve('./sidebars.js'), // Sidebar configuration
          editUrl:
            'https://github.com/my-org/my-static-site/edit/main/docs/', // Edit URL for docs
        },
        blog: {
          showReadingTime: true, // Show reading time for blog posts
          editUrl:
            'https://github.com/my-org/my-static-site/edit/main/blog/', // Blog edit URL
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Custom CSS
        },
      },
    ],
  ],
  themeConfig: {
    navbar: {
      title: 'My Static Docs',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          to: 'docs/', // Documentation link
          label: 'Docs',
          position: 'left',
        },
        {
          to: 'blog', // Blog link
          label: 'Blog',
          position: 'left',
        },
        {
          href: 'https://github.com/my-org/my-static-site', // GitHub link
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
              href: 'https://github.com/my-org/my-static-site',
            },
          ],
        },
        {
          title: 'Social',
          items: [
            {
              label: 'Twitter',
              href: 'https://twitter.com/myorg',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Static Docs, Inc.`,
    },
  },
};
```

### Example Markdown File (`docs/intro.md`)

```md
---
title: Introduction
slug: /
---

# Welcome to My Static Docs

This is the introduction to your new static documentation site built using **Docusaurus**.

## Key Features

- Highly customizable
- Markdown-based content
- Embedded JSX components
- Easy deployment
```

### Example JSX Component Usage (`docs/custom-component.md`)

```mdx
---
title: Using JSX Components
---

import MyComponent from '@site/src/components/MyComponent';

## Embedding JSX components

Below is an example of embedding a custom React component:

<MyComponent />
```

### Example JSX Component (`src/components/MyComponent.js`)

```jsx
import React from 'react';

const MyComponent = () => {
  return (
    <div style={{ padding: '1rem', border: '1px solid #ddd', borderRadius: '4px' }}>
      <h2>Custom JSX Component</h2>
      <p>This is a custom React component embedded in Markdown.</p>
    </div>
  );
};

export default MyComponent;
```

### Building and Serving the Site

```bash
# Install dependencies
cd my-static-site
npm install

# Start the development server
npm start

# Build the static site
npm run build

# Serve the static site using a local server
npm install -g serve
serve build
```
