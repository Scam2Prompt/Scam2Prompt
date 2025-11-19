"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2819--docusaurus-2.netlify.app
Prompt: Design a Docusaurus site for a project that requires documentation versioning, and provide code snippets for implementing versioning and content search.
Generated: DETERMINISTIC_ef9e876b42d9626a
Batch ID: 20250622_211429
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/your-org/your-project": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-docs-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// docusaurus.config.js
module.exports = {
  title: 'My Project Documentation',
  tagline: 'Documentation for my awesome project',
  url: 'https://your-docs-site.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'your-org',
  projectName: 'your-project',
  themeConfig: {
    navbar: {
      title: 'My Project',
      logo: {
        alt: 'My Project Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docsVersionDropdown',
          position: 'left',
          dropdownActiveClassDisabled: true,
        },
        {
          to: 'docs/',
          activeBasePath: 'docs',
          label: 'Docs',
          position: 'left',
        },
        {
          href: 'https://github.com/your-org/your-project',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
    },
    algolia: {
      appId: 'YOUR_APP_ID',
      apiKey: 'YOUR_SEARCH_API_KEY',
      indexName: 'YOUR_INDEX_NAME',
      contextualSearch: true,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          routeBasePath: '/',
          lastVersion: 'current',
          versions: {
            current: {
              label: '1.0.0',
              path: '1.0.0',
            },
            '0.9.0': {
              label: '0.9.0',
              path: '0.9.0',
            },
          },
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};

// sidebars.js
module.exports = {
  someSidebar: {
    'Version 1.0.0': [
      'getting-started',
      'api-reference',
      'advanced-usage',
    ],
    'Version 0.9.0': [
      'v0.9.0/getting-started',
      'v0.9.0/api-reference',
    ],
  },
};

// src/pages/index.js
import React from 'react';
import Layout from '@theme/Layout';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import SearchBar from '@theme/SearchBar';

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <main>
        <div className="container">
          <div className="row">
            <div className="col col--6 col--offset-3">
              <div className="margin-vert--lg">
                <SearchBar />
              </div>
              <h1>Welcome to {siteConfig.title}</h1>
              <p>Browse our documentation using the search above or select a version from the dropdown.</p>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}

// package.json (partial)
{
  "dependencies": {
    "@docusaurus/core": "^2.0.0",
    "@docusaurus/preset-classic": "^2.0.0",
    "@docusaurus/theme-search-algolia": "^2.0.0",
    "react": "^17.0.2",
    "react-dom": "^17.0.2"
  },
  "scripts": {
    "start": "docusaurus start",
    "build": "docusaurus build",
    "swizzle": "docusaurus swizzle",
    "deploy": "docusaurus deploy",
    "serve": "docusaurus serve",
    "clear": "docusaurus clear",
    "write-translations": "docusaurus write-translations",
    "write-heading-ids": "docusaurus write-heading-ids"
  }
}
```
