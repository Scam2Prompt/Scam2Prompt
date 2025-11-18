"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2820--docusaurus-2.netlify.app
Prompt: Write a script using Docusaurus to create a static website with Markdown-based documentation and blog posts, including JSX components embedded in the Markdown files.
Generated: DETERMINISTIC_47732521fd49dbb8
Batch ID: 20250612_151018
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/johndoe.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/my-org/my-website/edit/main/blog/": {
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
  "https://github.com/my-org/my-website/edit/main/docs/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/johndoe": {
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
// Install necessary dependencies with:
// npm install @docusaurus/core @docusaurus/preset-classic react react-dom

// docusaurus.config.js
module.exports = {
  title: 'My Website',
  tagline: 'Markdown-based documentation and blogs',
  url: 'https://example.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'my-org', // GitHub org/user name.
  projectName: 'my-website', // Repository name.

  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'), // Path to sidebar configuration.
          editUrl: 'https://github.com/my-org/my-website/edit/main/docs/', // Edit URL for docs.
        },
        blog: {
          showReadingTime: true, // Show estimated reading time for blog posts.
          editUrl: 'https://github.com/my-org/my-website/edit/main/blog/', // Edit URL for blog posts.
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Path to custom CSS.
        },
      },
    ],
  ],
};

// sidebars.js
module.exports = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Tutorial',
      items: ['intro', 'setup', 'usage'],
    },
  ],
};

// src/components/Alert.js
import React from 'react';

export default function Alert({ message }) {
  return <div style={{ padding: '10px', border: '1px solid red', color: 'red' }}>{message}</div>;
}

// docs/intro.md
---
id: intro
title: Introduction
---

# Welcome to My Website

This Markdown file is part of the `docs` folder. Below is an embedded JSX component:

import Alert from '@site/src/components/Alert';

<Alert message="This is an important alert!" />

Continue reading the documentation to learn more!

// docs/setup.md
---
id: setup
title: Setup
---

# Setup Guide

Follow these steps to set up your project:

1. Clone the repository.
2. Install dependencies using `npm install`.
3. Start the development server with `npm start`.

import Alert from '@site/src/components/Alert';

<Alert message="Don't forget to install dependencies!" />

// docs/usage.md
---
id: usage
title: Usage
---

# Usage Instructions

Here’s how to use this tool effectively:

- Navigate through the sidebar.
- Embed JSX components within Markdown files for dynamic content.

import Alert from '@site/src/components/Alert';

<Alert message="Embed components easily!" />

// blog/2023-01-01-welcome.md
---
slug: welcome
title: Welcome to the Blog
author: John Doe
author_title: Developer
author_url: https://github.com/johndoe
author_image_url: https://example.com/johndoe.jpg
tags: [welcome, blog]
---

# Welcome to Our Blog

This is the first blog post of the website. Stay tuned for more updates!

import Alert from '@site/src/components/Alert';

<Alert message="Blogging made simple!" />

// src/css/custom.css
body {
  font-family: Arial, sans-serif;
}

// Package.json (ensure this is included for the setup)
{
  "name": "my-website",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "start": "docusaurus start",
    "build": "docusaurus build",
    "serve": "docusaurus serve"
  },
  "dependencies": {
    "@docusaurus/core": "^2.0.0",
    "@docusaurus/preset-classic": "^2.0.0",
    "react": "^18.0.0",
    "react-dom": "^18.0.0"
  }
}
```
