"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: Create a code example for a custom Docusaurus theme that reuses the default header and footer.
Generated: DETERMINISTIC_8e34b972dff86075
Batch ID: 20250622_211429
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://stackoverflow.com/questions/tagged/docusaurus": {
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
  },
  "https://your-docusaurus-site.com": {
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
  "https://twitter.com/docusaurus": {
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
// src/theme/CustomLayout/index.js
// This file defines a custom Docusaurus theme layout that reuses the default header and footer.

import React from 'react';
import Layout from '@theme/Layout'; // Import the default Layout component
import useDocusaurusContext from '@docusaurus/useDocusaurusContext'; // Hook to access Docusaurus context

// CustomLayout component
export default function CustomLayout({ children }) {
  const { siteConfig } = useDocusaurusContext(); // Access site configuration

  return (
    <Layout>
      {/* Reuse the default header and footer provided by Docusaurus */}
      <div style={{ padding: '2rem', backgroundColor: '#f9f9f9' }}>
        {/* Custom content goes here */}
        <h1>Welcome to {siteConfig.title}</h1>
        <p>This is a custom layout that reuses the default header and footer.</p>
        <div>{children}</div>
      </div>
    </Layout>
  );
}
```

```javascript
// docusaurus.config.js
// Configuration file for Docusaurus. This file registers the custom theme.

module.exports = {
  title: 'My Custom Docusaurus Site',
  tagline: 'Dinosaurs are cool',
  url: 'https://your-docusaurus-site.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'your-org', // Usually your GitHub org/user name.
  projectName: 'your-project', // Usually your repo name.

  themeConfig: {
    navbar: {
      title: 'My Site',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        { to: 'docs/', label: 'Docs', position: 'left' },
        { to: 'blog', label: 'Blog', position: 'left' },
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
              label: 'Style Guide',
              to: 'docs/',
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
          ],
        },
        {
          title: 'Social',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/facebook/docusaurus',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/docusaurus',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
    },
  },

  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
        },
        blog: {
          showReadingTime: true,
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  // Register the custom theme
  themes: ['@docusaurus/theme-classic'],
};
```

```javascript
// src/css/custom.css
/* Custom CSS for the custom layout */
body {
  font-family: Arial, sans-serif;
}

h1 {
  color: #333;
}

p {
  color: #555;
}
```
