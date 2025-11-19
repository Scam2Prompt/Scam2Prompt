"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2809--docusaurus-2.netlify.app
Prompt: Write code to set up a Docusaurus project using React and Markdown/MDX for documentation, ensuring support for JSX components embedded in Markdown files.
Generated: DETERMINISTIC_1660bf9fef44a0e9
Batch ID: 20250612_151018
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://stackoverflow.com/questions/tagged/your-project": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://discordapp.com/invite/your-project": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-org/your-project": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-docusaurus-site.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```bash
# Initialize a new Docusaurus project
npx create-docusaurus@latest my-docs-website classic

# Navigate to the project directory
cd my-docs-website
```

```javascript
// docusaurus.config.js
/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'My Documentation Site',
  tagline: 'Documentation with JSX components',
  url: 'https://your-docusaurus-site.example.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'your-org',
  projectName: 'your-project',

  presets: [
    [
      '@docusaurus/preset-classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          remarkPlugins: [require('mdx-mermaid')],
          // Enable MDX support
          docLayoutComponent: '@theme/DocPage',
          docItemComponent: '@theme/MDXPage',
        },
        blog: {
          showReadingTime: true,
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
        title: 'My Site',
        logo: {
          alt: 'My Site Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'doc',
            docId: 'intro',
            position: 'left',
            label: 'Docs',
          },
          {to: '/blog', label: 'Blog', position: 'left'},
          {
            href: 'https://github.com/your-org/your-project',
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
                href: 'https://stackoverflow.com/questions/tagged/your-project',
              },
              {
                label: 'Discord',
                href: 'https://discordapp.com/invite/your-project',
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
              {
                label: 'GitHub',
                href: 'https://github.com/your-org/your-project',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
      },
    }),

  plugins: [
    // Enable MDX support
    async function myPlugin(context, options) {
      return {
        name: 'docusaurus-mdx-plugin',
        configureWebpack(config, isServer) {
          return {
            module: {
              rules: [
                {
                  test: /\.mdx?$/,
                  use: [
                    {
                      loader: require.resolve('@mdx-js/loader'),
                      options: {
                        remarkPlugins: [require('remark-math')],
                        rehypePlugins: [require('rehype-katex')],
                      },
                    },
                  ],
                },
              ],
            },
          };
        },
      };
    },
  ],
};

module.exports = config;
```

```javascript
// src/components/ExampleComponent.jsx
import React from 'react';

/**
 * Example React component that can be used in MDX files
 */
export default function ExampleComponent({ children }) {
  return (
    <div style={{
      padding: '1rem',
      backgroundColor: '#f0f0f0',
      borderRadius: '4px',
      margin: '1rem 0'
    }}>
      <h3>Example Component</h3>
      {children}
    </div>
  );
}
```

```markdown
# docs/intro.md
---
title: Introduction
---

import ExampleComponent from '../components/ExampleComponent';

# Welcome to My Documentation

This is a regular markdown file with embedded JSX components.

<ExampleComponent>
  This content is rendered inside our custom React component!
</ExampleComponent>

## Math Equations

You can also use LaTeX math:

$$
E = mc^2
$$

## Mermaid Diagrams

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

```bash
# Install required dependencies
npm install @mdx-js/react @mdx-js/loader remark-math rehype-katex mdx-mermaid
```

```javascript
// babel.config.js
module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          node: 'current',
        },
      },
    ],
    '@babel/preset-react',
  ],
  plugins: [
    '@babel/plugin-proposal-class-properties',
    '@babel/plugin-proposal-object-rest-spread',
  ],
};
```
