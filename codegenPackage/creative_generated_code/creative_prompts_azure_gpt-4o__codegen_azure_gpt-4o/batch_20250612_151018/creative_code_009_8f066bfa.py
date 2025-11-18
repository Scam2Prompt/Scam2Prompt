"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2735--docusaurus-2.netlify.app
Prompt: Provide a step-by-step example of embedding JSX components into Markdown files using MDX in Docusaurus.
Generated: DETERMINISTIC_8f066bfab16fadd5
Batch ID: 20250612_151018
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/example/docusaurus-mdx-example/edit/main/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/example/docusaurus-mdx-example/edit/main/blog/": {
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
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Install dependencies:
// npm install @docusaurus/mdx-loader react react-dom

// Step 1: Create a JSX component
// Path: src/components/Alert.js

import React from 'react';

const Alert = ({ type, children }) => {
  const alertStyles = {
    padding: '10px',
    borderRadius: '4px',
    marginBottom: '20px',
    color: type === 'warning' ? '#856404' : '#155724',
    backgroundColor: type === 'warning' ? '#fff3cd' : '#d4edda',
    border: type === 'warning' ? '1px solid #ffeeba' : '1px solid #c3e6cb',
  };

  return <div style={alertStyles}>{children}</div>;
};

export default Alert;

// Step 2: Embed the JSX component into a Markdown file using MDX
// Path: docs/example.md

import Alert from '@site/src/components/Alert';

# Example Page with JSX Components

This is a Markdown file enhanced with JSX components using MDX.

<Alert type="success">
  This is a success alert embedded in Markdown!
</Alert>

<Alert type="warning">
  This is a warning alert embedded in Markdown!
</Alert>

// Step 3: Configure MDX in Docusaurus
// Path: docusaurus.config.js

const config = {
  title: 'My Docusaurus Project',
  tagline: 'Embedding JSX Components into Markdown',
  url: 'https://example.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'example', // Usually your GitHub org/user name.
  projectName: 'docusaurus-mdx-example', // Usually your repo name.

  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/example/docusaurus-mdx-example/edit/main/',
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/example/docusaurus-mdx-example/edit/main/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};

module.exports = config;

// Step 4: Run Docusaurus
// Install Docusaurus if not already installed:
// npx create-docusaurus@latest my-docusaurus-site classic

// Start development server:
// npm start
```
